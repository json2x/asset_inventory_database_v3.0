from django.db import models, transaction, Error
from django.http.response import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse, request
from django.views import View
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import generics
from dal import autocomplete
import json

from .forms import DailyActivityForm
from .models import Activity, MobileTechnology, MobileFrequencyBand, SiteStatus
from .models import DailyActivity, DailyActivity_Device, DailyActivity_Cell, DailyActivity_Trx
from .serializers import CellsDeviceTrxSerializer, CellsDeviceTrxNMSDataSerializer, DailyActivitySerializer

from api.models import SmartSite, Device, Cell, Trx
from api.serializers import DevicesSerializer, CellsSerializer, TrxSerializer

from nmsdata import models as Nms
from nmsdata.serializers import NmsDevicesSerializer, NmsCellsSerializer, NmsTrxSerializer


# Create your views here.
#-------------------------------------
def home(request):

    return render(request, 'edrar/home.html')
    #return HttpResponse("eDRAR Home Page.")

# def activity_add(request):

#     if request.method == 'POST':
#         pass

#     context= {'form': DailyActivityForm}

#     if request.user.is_authenticated:
#         context['user'] = request.user

#     return render(request, 'edrar/activity_add.html', context)

class AddActivity(View):
    template_name = 'edrar/activity_add.html'
    form_class = DailyActivityForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        activity = post_data['activity'] or None 
        devices = post_data['devices'] or None
        cells = post_data['cells'] or None
        trxs = post_data['trxs'] or None

        saved_data = {}
        try:
            with transaction.atomic():
                if devices:
                    rfs_counter = 0
                    if activity['activity'] == 'Rollout':
                        rfs_counter = 1
                    elif activity['activity'] == 'Site Deletion':
                        rfs_counter = -1
                    selected_activity = Activity.objects.get(pk=int(activity['activity']))
                    selected_user = User.objects.get(pk=int(activity['user']))
                    selected_site_status = SiteStatus.objects.get(pk=int(activity['site_status']))
                    selected_site_id = SmartSite.objects.get(siteid=activity['siteid'])

                    activity_data = DailyActivity(
                        date_logged = timezone.now(), tech = activity['tech'], user = selected_user, counterpart = activity['counterpart'],
                        activity = selected_activity, site_status = selected_site_status, rfs_count = rfs_counter, siteid = selected_site_id,
                        band = activity['band'], vendor = activity['vendor'], homing = activity['homing'], bts_id = activity['bts_id'], 
                        device_name = activity['device_name'], equipment_type = activity['equipment_type'], trx_config = activity['trx_config'], 
                        iub_type = activity['iub_type'], bandwidth = activity['bandwidth'], sac = activity['sac'], cell_id = activity['cell_id'], 
                        cell_name = activity['cell_name'], lac = activity['lac'], pci = activity['pci'],  omip = activity['omip'], s1_c = activity['s1_c'], 
                        s1_u = activity['s1_u'], remarks = activity['remarks']
                    )
                    activity_data.save()
                    saved_data['activity'] = DailyActivitySerializer(activity_data).data

                    saved_data['devices'] = []
                    for device in devices:
                        record_status = self.get_record_status('device', activity_data)
                        create_flag = self.get_create_flag('device', activity_data)
                        update_flag = self.get_update_flag(activity_data)

                        device_data = Device(
                            dn = device['dn'], device_id = device['device_id'], ems_device_id = device['ems_device_id'], device_alias = device['device_alias'],
                            device_ip = device['device_ip'], ems_id = device['ems_id'], vendor_id = device['vendor_id'], ne_type = device['ne_type'],
                            model = device['model'], hardware_description = device['hardware_description'], functional_description = device['functional_description'],
                            parent_device_id = device['parent_device_id'], parentdn = device['parentdn'], site_id = device['site_id'], device_state = device['device_state'],
                            software_version = device['software_version'], integration_date = device['integration_date'], end_of_support = device['end_of_support'],
                            tsa_scope = device['tsa_scope'], product_id = device['product_id'], serial_number = device['serial_number'], freq_tx_rx_field = device['freq_tx_rx_field'],
                            hardware_capacity = device['hardware_capacity'], domain = device['domain'], ne_owner = device['ne_owner'], tx_clusterimg = device['tx_clusterimg'],
                            tx_type = device['tx_type'], natspcode = device['natspcode'], admin_state = device['admin_state'], subdomain = device['subdomain'], 
                            function = device['function'], iubce_dl_lic = device['iubce_dl_lic'], iubce_ul_lic = device['iubce_ul_lic'], s1cu_lic = device['s1cu_lic'],
                            cluster_region = device['cluster_region'], cluster_sub_region = device['cluster_sub_region'], cluster_province = device['cluster_province'],
                            cluster_city = device['cluster_city'], mw_hub = device['mw_hub'], record_status = record_status
                        )
                        device_data.save()
                        saved_data['devices'].append(DevicesSerializer(device_data).data)

                        activity_device_data = DailyActivity_Device(
                            daily_activity = activity_data, device = device_data,
                            create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                            update_flag = update_flag #True if update False if create
                        )
                        activity_device_data.save()
                    
                        saved_data['cells'] = []
                        for cell in cells:
                            record_status = self.get_record_status('cell', activity_data)
                            create_flag = self.get_create_flag('cell', activity_data)
                            update_flag = self.get_update_flag(activity_data)
                                    
                            if cell['ems_id'] == device_data.ems_id and  cell['parent_id'] == device_data.device_id \
                            and cell['site'] == device_data.site_id and cell['subdomain'] == device_data.subdomain:
                                cell_data = Cell(
                                    domain = cell['domain'], ems_cell_id = cell['ems_cell_id'], ems_id = cell['ems_id'], cell_name = cell['cell_name'], dn = cell['dn'],
                                    site = cell['site'], parent_id = cell['parent_id'], parent_dn = cell['parent_dn'], tech = cell['tech'], band = cell['band'], 
                                    admin_state = cell['admin_state'], alias = cell['alias'], lac_tac = cell['lac_tac'], sac_ci_eutra = cell['sac_ci_eutra'], 
                                    rnc_cid = cell['rnc_cid'], phy_cid = cell['phy_cid'], lcr_cid = cell['lcr_cid'], mcc = cell['mcc'], mnc = cell['mnc'], 
                                    nodeid = cell['nodeid'], sector_id = cell['sector_id'], carrier = cell['carrier'], ne_type = cell['ne_type'], 
                                    subdomain = cell['subdomain'], function = cell['function'], sdcch_cap = cell['sdcch_cap'], tch_cap = cell['tch_cap'], 
                                    azimuth = cell['azimuth'], record_status = record_status, device = device_data
                                )
                                cell_data.save()
                                saved_data['cells'].append(CellsSerializer(cell_data).data)

                                activity_cell_data = DailyActivity_Cell(
                                    daily_activity = activity_data, cell = cell_data,
                                    create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                                    update_flag = update_flag #True if update False if create
                                )
                                activity_cell_data.save()

                            saved_data['trxs'] = []
                            for trx in trxs:
                                record_status = self.get_record_status('trx', activity_data)
                                create_flag = self.get_create_flag('trx', activity_data)
                                update_flag = self.get_update_flag(activity_data)

                                if trx['ems_id'] == cell_data.ems_id and trx['parent_id'] == cell_data.cell_name and trx['homing_bts'] == cell_data.parent_id:
                                    trx_data = Trx(
                                        ems_trx_id = trx['ems_trx_id'], ems_id = trx['ems_id'], trx_name = trx['trx_name'], dn = trx['dn'], site_id = trx['site_id'],
                                        parent_id = trx['parent_id'], parent_dn = trx['parent_dn'], admin_state = trx['admin_state'], e1_assignment = trx['e1_assignment'],
                                        homing_bts = trx['homing_bts'], record_status = record_status, cell = cell_data, device = device_data
                                    )
                                    trx_data.save()
                                    saved_data['trxs'].append(TrxSerializer(trx_data).data)

                                    activity_trx_data = DailyActivity_Trx(
                                        daily_activity = activity_data, trx = trx_data,
                                        create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                                        update_flag = update_flag #True if update False if create
                                    )
                                    activity_trx_data.save()

        except transaction.TransactionManagementError as err:
            saved_data = {}
            return JsonResponse({'error': err})
        except Error as err:
            saved_data = {}
            return JsonResponse({'error': err})
        
        #return JsonResponse(activity)
        return JsonResponse(saved_data)

    def get_record_status(self, table, activity):
        record_status = 1
        if table == 'device':
            if activity.activity == 'On-Air':
                record_status = 2
            elif activity.activity == 'Site Deletion':
                record_status = 0
        elif table == 'cell':
            if activity.activity == 'On-Air':
                record_status = 2
            elif activity.activity == 'Site Deletion' or activity.activity == 'Delete Cell':
                record_status = 0
        elif table == 'trx':
            if activity.activity == 'On-Air':
                record_status = 2
            elif activity.activity == 'Site Deletion' or activity.activity == 'Delete Cell' \
            or activity.activity == 'TRX Downgrade':
                record_status = 0
        
        return record_status

    def get_create_flag(self, table, activity):
        create_flag = 0
        if table == 'device':
            if activity.activity == 'Rollout':
                create_flag = 1
            elif activity.activity == 'Site Deletion':
                create_flag = -1
        elif table == 'cell':
            if activity.activity == 'Rollout' or activity.activity == 'Expansion':
                create_flag = 1
            elif activity.activity == 'Site Deletion' or activity.activity == 'Delete Cell':
                create_flag = -1
        elif table == 'trx':
            if activity.activity == 'Rollout' or activity.activity == 'Expansion' \
            or activity.activity == 'TRX Expansion':
                create_flag = 1
            elif activity.activity == 'Site Deletion' or activity.activity == 'Delete Cell' \
            or activity.activity == 'TRX Downgrade':
                create_flag = -1
        
        return create_flag

    def get_update_flag(self, activity):
        update_flag = True
        if activity.activity == 'Rollout' or activity.activity == 'Expansion' \
        or activity.activity == 'TRX Expansion':
            update_flag = False

        return update_flag



class ActivityAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Activity.objects.none()

        qs = Activity.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

class SiteIdAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SmartSite.objects.none()

        qs = SmartSite.objects.all()

        if self.q:
            qs = qs.filter(siteid__icontains=self.q)

        return qs

class MobileTechAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return MobileTechnology.objects.none()

        qs = MobileTechnology.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

class MobileFreqBandAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return MobileFrequencyBand.objects.none()

        qs = MobileFrequencyBand.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

class DeviceDatatableView(BaseDatatableView):
    model = Device
    columns = [
        'id', 'ems_id',  'dn', 'device_id', 'parent_device_id', 'ne_type', 
        'site_id', 'subdomain', 'vendor_id', 'domain', 'model', 
        'record_status'
    ]

    def filter_queryset(self, qs):
        site = self.request.GET.get('columns[5][search][value]', None)
        tech = self.request.GET.get('columns[6][search][value]', None)
        tbl_ids = self.request.GET.get('columns[11][search][value]', None)
        
        if tbl_ids:
            if tbl_ids.find(';') > 0:
                tbl_ids = tbl_ids.split(';')
                qs_params = None
                for tbl_id in tbl_ids:
                    if qs_params:
                        qs_params = qs_params | Q(id=int(tbl_id))
                    else:
                        qs_params = Q(id=int(tbl_id))
                qs = qs.filter(qs_params)
            else:
                 qs = qs.filter(id=int(tbl_ids))
        else:
            qs = qs.filter(site_id=site).filter(subdomain=tech)

        return qs

class NmsDeviceDatatableView(BaseDatatableView):
    model = Nms.Device #Change to nmsdata Device data model
    columns = [
        'id', 'ems_id',  'dn', 'device_id', 'parent_device_id', 'ne_type', 
        'site_id', 'subdomain', 'vendor_id', 'domain', 'model', 
        'record_status'
    ]

    def filter_queryset(self, qs):
        site = self.request.GET.get('columns[5][search][value]', None)
        tech = self.request.GET.get('columns[6][search][value]', None)
        tbl_ids = self.request.GET.get('columns[11][search][value]', None)
        if tbl_ids:
            if tbl_ids.find(';') > 0:
                tbl_ids = tbl_ids.split(';')

            if type(tbl_ids) is list:
                qs_params = None
                for tbl_id in tbl_ids:
                    if qs_params:
                        qs_params = qs_params | Q(id=int(tbl_id))
                    else:
                        qs_params = Q(id=int(tbl_id))
                qs = qs.filter(qs_params)
            else:
                 qs = qs.filter(id=int(tbl_ids))
        else:
            qs = qs.filter(site_id=site).filter(subdomain=tech)

        return qs

class CellDatatableView(BaseDatatableView):
    model = Cell
    columns = [
        'id', 'domain', 'ems_id', 'nodeid', 'cell_name', 'parent_id', 'parent_dn', 
        'site', 'tech', 'subdomain', 'band', 'ne_type', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
        'lcr_cid', 'sector_id', 'function', 'sdcch_cap', 'tch_cap', 'record_status'
    ]

class NmsCellDatatableView(BaseDatatableView):
    model = Nms.Cell #Change to nmsdata Cell data model
    columns = [
        'id', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
        'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
        'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
        'sdcch_cap', 'tch_cap', 'homing_id', 'dlear_fcn', 'ulear_dcn', 'dlc_hbw', 'ulc_hbw',
        'rac', 'ncc', 'bcc', 'nnode_id', 'nbscid', 'azimuth', 'psc', 'bcchno'
    ]

class TrxDatatableView(BaseDatatableView):
    model = Trx
    columns = [
        'id', 'ems_id', 'trx_name', 'parent_id', 'admin_state', 'e1_assignment', 'homing_bts', 'cell', 'device'
    ]

    def filter_queryset(self, qs):

        trx_ids = self.request.GET.get('columns[7][search][value]', None)
        if trx_ids.find(';') > 1:
            trx_ids = trx_ids.split(';')

        if type(trx_ids) is list:
            qs_params = None
            for trx_id in trx_ids:
                if qs_params:
                    qs_params = qs_params | Q(id=int(trx_id))
                else:
                    qs_params = Q(id=int(trx_id))
            qs = qs.filter(qs_params)
        else:
            qs = qs.filter(id=int(trx_ids))

        return qs

class NmsTrxDatatableView(BaseDatatableView):
    model = Nms.Trx #Change to nmsdata Trx data model
    columns = [
        'id', 'ems_trx_id', 'ems_id', 'trx_name', 'dn', 'site_id', 'parent_id', 
        'parent_dn', 'admin_state', 'e1_assignment', 'homing_bts', 'homing_id',
        'trxfreq', 'record_status'
    ]

    def filter_queryset(self, qs):

        trx_ids = self.request.GET.get('columns[7][search][value]', None)
        if trx_ids.find(';') > 1:
            trx_ids = trx_ids.split(';')

        if type(trx_ids) is list:
            qs_params = None
            for trx_id in trx_ids:
                if qs_params:
                    qs_params = qs_params | Q(id=int(trx_id))
                else:
                    qs_params = Q(id=int(trx_id))
            qs = qs.filter(qs_params)
        else:
            qs = qs.filter(id=int(trx_ids))
        
        return qs

# class ActivityLogTextFieldData(generics.ListAPIView):
#     serializer_class = CellsDeviceTrxSerializer
    
#     def get_queryset(self):
#         site = self.request.GET.get('site', None)
#         tech = self.request.GET.get('tech', None)
#         band = self.request.GET.get('band', None)
#         src = self.request.GET.get('src', None)

#         if src == 'nms':
#             self.serializer_class = CellsDeviceTrxNMSDataSerializer
#             return Nms.Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band)
#         else:
#             return Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band)

class GetNEData(generics.ListAPIView):
    serializer_class = CellsDeviceTrxSerializer
    
    def get_queryset(self):
        site = self.request.GET.get('site', None)
        tech = self.request.GET.get('tech', None)
        band = self.request.GET.get('band', None)
        src = self.request.GET.get('src', None)

        if src == 'nms':
            self.serializer_class = CellsDeviceTrxNMSDataSerializer
            return Nms.Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band).order_by('cell_name')
        else:
            return Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band).order_by('cell_name')

# class GetDeviceDataByID(generics.ListAPIView):
#     serializer_class = DevicesSerializer

#     def get_queryset(self):
#         id = self.request.GET.get('id', None)
#         self.serializer_class = self.get_serializer_class()

#         qs_params = None
#         if id.find(';'):
#             ids = id.split(';')
#             for id in ids:
#                 if qs_params:
#                     qs_params = qs_params | Q(id=id)
#                 else:
#                     qs_params = Q(id=id)
#             qs = Device.objects.filter(qs_params)
#         else:
#             qs = Device.objects.filter(id=id)

#         return qs

#     def get_serializer_class(self):
#         data_source = self.request.GET.get('src', None)
#         if data_source and data_source == 'nms':
#             return NmsDevicesSerializer
#         else:
#             return DevicesSerializer

# class GetCellDataByID(generics.ListAPIView):
#     serializer_class = CellsSerializer
    
#     def get_queryset(self):
#         id = self.request.GET.get('id', None)
#         self.serializer_class = self.get_serializer_class()

#         qs_params = None
#         if id.find(';'):
#             ids = id.split(';')
#             for id in ids:
#                 if qs_params:
#                     qs_params = qs_params | Q(id=id)
#                 else:
#                     qs_params = Q(id=id)
#             qs = Cell.objects.filter(qs_params)
#         else:
#             qs = Cell.objects.filter(id=id)

#         return qs

#     def get_serializer_class(self):
#         data_source = self.request.GET.get('src', None)
#         if data_source and data_source == 'nms':
#             return NmsCellsSerializer
#         else:
#             return CellsSerializer

# class GetTrxDataByID(generics.ListAPIView):
#     serializer_class = TrxSerializer
    
#     def get_queryset(self):
#         id = self.request.GET.get('id', None)
#         self.serializer_class = self.get_serializer_class()

#         qs_params = None
#         if id.find(';'):
#             ids = id.split(';')
#             for id in ids:
#                 if qs_params:
#                     qs_params = qs_params | Q(id=id)
#                 else:
#                     qs_params = Q(id=id)
#             qs = Trx.objects.filter(qs_params)
#         else:
#             qs = Trx.objects.filter(id=id)

#         return qs

#     def get_serializer_class(self):
#         data_source = self.request.GET.get('src', None)
#         if data_source and data_source == 'nms':
#             return NmsTrxSerializer
#         else:
#             return TrxSerializer