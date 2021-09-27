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
from rest_framework import generics, status
from rest_framework.response import Response
from dal import autocomplete
import datetime
import json

from .forms import DailyActivityForm
from .models import Activity, MobileTechnology, MobileFrequencyBand, SiteStatus
from .models import DailyActivity, DailyActivity_Device, DailyActivity_Cell, DailyActivity_Trx
from .serializers import CellsDeviceTrxSerializer, CellsDeviceTrxNMSDataSerializer, DailyActivitySerializer, UpdateLogDailyActivitySerializer, SiteTechBandSerializer

from api.models import SmartSite, Device, Cell, Trx, SmartNe, SiteNeAsset
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
        context = {'form': self.form_class}

        return render(request, self.template_name, context)

    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        activity_data = post_data['activity'] or None 
        devices = post_data['devices'] or None
        cells = post_data['cells'] or None
        trxs = post_data['trxs'] or None
        rehome_data = post_data['rehome'] or None
        current_element = None
        saved_data = {'devices': [], 'cells': [], 'trxs': []}

        # SAVE ACTIVITY AND RELATED NE ELEMENTS AS A TRANSACTION TO ENSURE ACTIVITY AND NE ELEMENTS RELATIONSHIPS.
        try:
            with transaction.atomic():
                # Special handling for BTS Rehoming activity
                if int(activity_data['activity']) == 10: #'BTS Rehoming'
                    saved_data['activity'] = {'activity': 10, 'siteid': None, 'band': None, 'tech': None}
                    saved_data['devices'] = self.RehomeNEs(activity_data, rehome_data)
                    response = {'success': True, 'data': saved_data}

                # All other activities except BTS Rehoming
                elif devices:
                    rfs_counter = 0
                    if int(activity_data['activity']) == 4: #'Rollout'
                        rfs_counter = 1
                    elif int(activity_data['activity']) == 17: #'Site Deletion'
                        rfs_counter = -1

                    activity = self.InstantiateDailyActivity(activity_data, rfs_counter)
                    activity.save()
                    saved_data['activity'] = DailyActivitySerializer(activity).data

                    # SAVE Smart NE to Smart NE Table every rollout activity.
                    # THINK ABOUT HOW TO SAVE THE DEVICE, CELL, TRX DATA OF EACH NE (STB)
                    smart_ne = SmartNe.objects.filter(siteid=activity.siteid.siteid).filter(band=activity.band).filter(tech=activity.tech).filter(smartsite=activity.siteid)
                    if activity.activity.name == 'Rollout' and not smart_ne:
                        smart_ne = SmartNe(siteid = activity.siteid.siteid, band = activity.band, tech = activity.tech, smartsite = activity.siteid)
                        smart_ne.save()

                    for device_index, device_data in enumerate(devices):

                        create_flag = self.get_create_flag('device', activity)
                        update_flag = self.get_update_flag(activity)
                        current_element = f"{activity_data['siteid']}|{activity_data['tech']}|{activity_data['band']}|{device_data['device_id']}"
                        
                        device = self.get_device_instance_by_activity(device_index, device_data, activity)
                        saved_data['devices'].append(DevicesSerializer(device).data)

                        activity_device = DailyActivity_Device(
                            daily_activity = activity, device = device,
                            create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                            update_flag = update_flag #True if update False if create
                        )
                        activity_device.save()

                        for cell_index, cell_data in enumerate(cells):
                            create_flag = self.get_create_flag('cell', activity)
                            update_flag = self.get_update_flag(activity)
                            current_element += f"|{cell_data['ems_id']}"

                            if cell_data['ems_id'] == device.ems_id and  (cell_data['parent_id'] == device.device_id or cell_data['parent_id'] == device_data['device_id']) \
                            and cell_data['site'] == device.site_id and cell_data['subdomain'] == device.subdomain:
                                cell = self.get_cell_instance_by_activity(cell_data, activity, device)
                                saved_data['cells'].append(CellsSerializer(cell).data)

                                activity_cell = DailyActivity_Cell(
                                    daily_activity = activity, cell = cell,
                                    create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                                    update_flag = update_flag #True if update False if create
                                )
                                activity_cell.save()

                                if trxs:
                                    for trx_index, trx_data in enumerate(trxs):
                                        
                                        create_flag = self.get_create_flag('trx', activity)
                                        update_flag = self.get_update_flag(activity)
                                        current_element += f"|{trx_data['trx_name']}"

                                        if trx_data['ems_id'] == cell.ems_id and trx_data['parent_id'] == cell.cell_name and \
                                        (trx_data['homing_bts'] == device.device_id or trx_data['homing_bts'] == device_data['device_id']):
                                            trx = self.get_trx_instance_by_activity(trx_data, activity, device, cell)
                                            saved_data['trxs'].append(TrxSerializer(trx).data)

                                            activity_trx = DailyActivity_Trx(
                                                daily_activity = activity, trx = trx,
                                                create_flag = create_flag, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                                                update_flag = update_flag #True if update False if create
                                            )
                                            activity_trx.save()

                    response = {'success': True, 'data': saved_data}

                else:
                    response = {'success': False, 'message': 'No reference device submitted.', 'element': 'NA'}

        except transaction.TransactionManagementError as err:
            saved_data = {}
            return JsonResponse({'success': False, 'message': str(err), 'element': current_element}, safe=False)
        except Error as err:
            saved_data = {}
            return JsonResponse({'success': False, 'message': str(err), 'element': current_element}, safe=False)
        
        return JsonResponse(response)

    def get_device_instance_by_activity(self, device_index, device_data, activity):
        device = None
        if activity.activity.name == 'Rollout':
            # Device has a Meta of unique_together = (('dn', 'device_id', 'ems_id', 'ne_type'),)
            # check first if there is a deleted device (record_status=3) in the clean db that is similar to the device to be uploaded, if yes then delete first.
            device = Device.objects.filter(dn=device_data['dn']).filter(device_id=device_data['device_id'])\
                .filter(ems_id=device_data['ems_id']).filter(ne_type=device_data['ne_type']).filter(record_status=3)
            if device:
                device.delete()
            device = self.InstatiateDevice(device_data)
            device.save()
        
        elif activity.activity.name == 'On-Air' or activity.activity.name == 'Site Deletion' or activity.activity.name == 'Correction':
            record_status = activity.site_status.id
            device = Device.objects.select_for_update().get(pk=device_data['id'])
            device.record_status = record_status
            device.save()

        elif activity.activity.name == 'Expansion' or activity.activity.name == 'TRX Expansion' or activity.activity.name == 'Delete Cell'\
        or activity.activity.name == 'TRX Downgrade' or activity.activity.name == 'Site Reconfig':
            device = Device.objects.get(pk=device_data['id'])

        elif activity.activity.name == 'BTS Swap':
            # Device has a Meta of unique_together = (('dn', 'device_id', 'ems_id', 'ne_type'),)
            device = Device.objects.filter(dn=device_data['dn']).filter(device_id=device_data['device_id'])\
                .filter(ems_id=device_data['ems_id']).filter(ne_type=device_data['ne_type'])
            if device:
                device.delete()
            device = self.InstatiateDevice(device_data)
            device.save()

        elif activity.activity.name == 'Site Rename':
            device = Device.objects.select_for_update().get(pk=device_data['id'])
            new_device_id = activity.device_name.split(';')
            device.device_id = new_device_id[device_index]
            device.save()

        return device

    def get_cell_instance_by_activity(self, cell_data, activity, device):
        cell = None
        if activity.activity.name == 'Rollout' or activity.activity.name == 'Expansion':
            # Cell has a Meta of unique_together = (('ems_id', 'dn', 'site', 'band', 'subdomain'),)
            # check first if there is a deleted cell (record_status=3) in the clean db that is similar to the device to be uploaded, if yes then delete first.
            cell = Cell.objects.filter(ems_id=cell_data['ems_id']).filter(dn=cell_data['dn']).filter(site=cell_data['site'])\
                .filter(band=cell_data['band']).filter(subdomain=cell_data['subdomain']).filter(record_status=3)
            if cell:
                cell.delete()
            cell = self.InstantiateCell(cell_data, device)
            cell.save()

        elif activity.activity.name == 'On-Air' or activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell' or activity.activity.name == 'Correction':
            record_status = activity.site_status.id
            cell = Cell.objects.select_for_update().get(pk=cell_data['id'])
            cell.record_status = record_status
            cell.save()

        # elif activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell':
        #     record_status = activity.site_status.id
        #     cell = Cell.objects.select_for_update().get(pk=cell_data['id'])
        #     cell.record_status = record_status
        #     cell.save()

        elif activity.activity.name == 'TRX Expansion' or activity.activity.name == 'TRX Downgrade':
            cell = Cell.objects.get(pk=cell_data['id'])

        elif activity.activity.name == 'BTS Swap':
            # Cell has a Meta of unique_together = (('ems_id', 'dn', 'site', 'band', 'subdomain'),)
            cell = Cell.objects.filter(ems_id=cell_data['ems_id']).filter(dn=cell_data['dn']).filter(site=cell_data['site'])\
                    .filter(band=cell_data['band']).filter(subdomain=cell_data['subdomain'])
            if cell:
                cell.delete()
            cell = self.InstantiateCell(cell_data, device)
            cell.save()

        elif activity.activity.name == 'Site Rename':
            cell = Cell.objects.select_for_update().get(pk=cell_data['id'])
            cell.parent_id = device.device_id
            cell.save()

        elif activity.activity.name == 'Site Reconfig':
            cell = Cell.objects.get(pk=cell_data['id'])
            # Delete first all trx related to the current cell. then add each new trx.
            Trx.objects.filter(ems_id=cell.ems_id).filter(site_id=cell.site).filter(parent_id=cell.cell_name).filter(homing_bts=cell.parent_id).delete()

        return cell

    def get_trx_instance_by_activity(self, trx_data, activity, device, cell):
        trx = None
        if activity.activity.name == 'Rollout' or activity.activity.name == 'Expansion' or activity.activity.name == 'TRX Expansion':
            # Trx has a Meta of unique_together = (('ems_id', 'dn', 'trx_name', 'site_id', 'parent_id', 'homing_bts'),)
            # check first if there is a deleted trx (record_status=3) in the clean db that is similar to the device to be uploaded, if yes then delete first.
            trx = Trx.objects.filter(ems_id=trx_data['ems_id']).filter(dn=trx_data['dn']).filter(trx_name=trx_data['trx_name'])\
                .filter(site_id=trx_data['site_id']).filter(parent_id=trx_data['parent_id']).filter(homing_bts=trx_data['homing_bts']).filter(record_status=3)
            if trx:
                trx.delete()
            trx = self.InstantiateTrx(trx_data, cell, device)
            trx.save()

        elif activity.activity.name == 'On-Air' or activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell' \
        or activity.activity.name == 'TRX Downgrade' or activity.activity.name == 'Correction':
            record_status = activity.site_status.id
            trx = Trx.objects.select_for_update().get(pk=trx_data['id'])
            trx.record_status = record_status
            trx.save()
        
        # elif activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell' or activity.activity.name == 'TRX Downgrade' or activity.activity.name == 'Correction':
        #     record_status = activity.site_status.id
        #     trx = Trx.objects.select_for_update().get(pk=trx_data['id'])
        #     trx.record_status = record_status
        #     trx.save()

        elif activity.activity.name == 'BTS Swap':
            # Trx has a Meta of unique_together = (('ems_id', 'dn', 'trx_name', 'site_id', 'parent_id', 'homing_bts'),)
            trx = Trx.objects.filter(ems_id=trx_data['ems_id']).filter(dn=trx_data['dn']).filter(trx_name=trx_data['trx_name'])\
                .filter(site_id=trx_data['site_id']).filter(parent_id=trx_data['parent_id']).filter(homing_bts=trx_data['homing_bts'])
            if trx:
                trx.delete()
            trx = self.InstantiateTrx(trx_data, cell, device)
            trx.save()

        elif activity.activity.name == 'Site Rename':
            trx = Trx.objects.select_for_update().get(pk=trx_data['id'])
            trx.homing_bts = device.device_id
            trx.save()

        elif activity.activity.name == 'Site Reconfig':
            trx = self.InstantiateTrx(trx_data, cell, device)
            trx.save()
            
        return trx

    def InstantiateDailyActivity(self, activity_data, rfs_counter):
        selected_activity = Activity.objects.get(pk=int(activity_data['activity']))
        selected_user = User.objects.get(pk=int(activity_data['user']))
        selected_site_status = SiteStatus.objects.get(pk=int(activity_data['site_status']))
        selected_site_id = SmartSite.objects.get(siteid=activity_data['siteid'])

        activity = DailyActivity(
            date_logged = datetime.datetime.now(), tech = activity_data['tech'], user = selected_user, counterpart = activity_data['counterpart'],
            activity = selected_activity, site_status = selected_site_status, rfs_count = rfs_counter, siteid = selected_site_id,
            band = activity_data['band'], vendor = activity_data['vendor'], homing = activity_data['homing'], bts_id = activity_data['bts_id'], 
            device_name = activity_data['device_name'], equipment_type = activity_data['equipment_type'], trx_config = activity_data['trx_config'], 
            iub_type = activity_data['iub_type'], bandwidth = activity_data['bandwidth'], sac = activity_data['sac'], cell_id = activity_data['cell_id'], 
            cell_name = activity_data['cell_name'], lac = activity_data['lac'], pci = activity_data['pci'],  omip = activity_data['omip'], 
            s1_c = activity_data['s1_c'], s1_u = activity_data['s1_u'], remarks = activity_data['remarks']
        )

        return activity
        
    def InstatiateDevice(self, device_data):
        device = Device(
            dn = device_data['dn'], device_id = device_data['device_id'], ems_device_id = device_data['ems_device_id'], device_alias = device_data['device_alias'],
            device_ip = device_data['device_ip'], ems_id = device_data['ems_id'], vendor_id = device_data['vendor_id'], ne_type = device_data['ne_type'],
            model = device_data['model'], hardware_description = device_data['hardware_description'], functional_description = device_data['functional_description'],
            parent_device_id = device_data['parent_device_id'], parentdn = device_data['parentdn'], site_id = device_data['site_id'], device_state = device_data['device_state'],
            software_version = device_data['software_version'], integration_date = device_data['integration_date'], end_of_support = device_data['end_of_support'],
            tsa_scope = device_data['tsa_scope'], product_id = device_data['product_id'], serial_number = device_data['serial_number'], freq_tx_rx_field = device_data['freq_tx_rx_field'],
            hardware_capacity = device_data['hardware_capacity'], domain = device_data['domain'], ne_owner = device_data['ne_owner'], tx_clusterimg = device_data['tx_clusterimg'],
            tx_type = device_data['tx_type'], natspcode = device_data['natspcode'], admin_state = device_data['admin_state'], subdomain = device_data['subdomain'], 
            function = device_data['function'], iubce_dl_lic = device_data['iubce_dl_lic'], iubce_ul_lic = device_data['iubce_ul_lic'], s1cu_lic = device_data['s1cu_lic'],
            cluster_region = device_data['cluster_region'], cluster_sub_region = device_data['cluster_sub_region'], cluster_province = device_data['cluster_province'],
            cluster_city = device_data['cluster_city'], mw_hub = device_data['mw_hub']
        )
        return device

    def InstantiateCell(self, cell_data, device):
        cell = Cell(
            domain = cell_data['domain'], ems_cell_id = cell_data['ems_cell_id'], ems_id = cell_data['ems_id'], cell_name = cell_data['cell_name'], dn = cell_data['dn'],
            site = cell_data['site'], parent_id = cell_data['parent_id'], parent_dn = cell_data['parent_dn'], tech = cell_data['tech'], band = cell_data['band'], 
            admin_state = cell_data['admin_state'], alias = cell_data['alias'], lac_tac = cell_data['lac_tac'], sac_ci_eutra = cell_data['sac_ci_eutra'], 
            rnc_cid = cell_data['rnc_cid'], phy_cid = cell_data['phy_cid'], lcr_cid = cell_data['lcr_cid'], mcc = cell_data['mcc'], mnc = cell_data['mnc'], 
            nodeid = cell_data['nodeid'], sector_id = cell_data['sector_id'], carrier = cell_data['carrier'], ne_type = cell_data['ne_type'], 
            subdomain = cell_data['subdomain'], function = cell_data['function'], sdcch_cap = cell_data['sdcch_cap'], tch_cap = cell_data['tch_cap'], 
            azimuth = cell_data['azimuth'], device = device
        )
        return cell

    def InstantiateTrx(self, trx_data, cell, device):
        trx = Trx(
            ems_trx_id = trx_data['ems_trx_id'], ems_id = trx_data['ems_id'], trx_name = trx_data['trx_name'], dn = trx_data['dn'], site_id = trx_data['site_id'],
            parent_id = trx_data['parent_id'], parent_dn = trx_data['parent_dn'], admin_state = trx_data['admin_state'], e1_assignment = trx_data['e1_assignment'],
            homing_bts = trx_data['homing_bts'], cell = cell, device = device
        )
        return trx

    def RehomeNEs(self, activity_data, rehome_data):
        new_homing = rehome_data['homing']
        nes = rehome_data['nes']
        updated_devices = []
        for ne in nes:
            ne = ne.split('_')
            cells = Cell.objects.filter(site=ne[0]).filter(band=ne[1]).filter(subdomain=ne[2])
            for cell in cells:
                logged_activity = True
                device = Device.objects.get(pk=cell.device.id)
                if device.parent_device_id != new_homing:
                    device.parent_device_id = new_homing
                    device.save()
                    updated_devices.append(DevicesSerializer(device).data)
                    
                    if logged_activity: # Log only one activity per NE.
                        activity_data['user'] = self.request.user.id
                        activity_data['siteid'] = device.site_id
                        activity_data['band'] = cell.band
                        activity_data['tech'] = device.subdomain
                        activity_data['vendor'] = device.vendor_id
                        activity_data['site_status'] = device.record_status
                        activity = self.InstantiateDailyActivity(activity_data, 0)
                        activity.save()

                        activity_device = DailyActivity_Device(
                            daily_activity = activity, device = device,
                            create_flag = 0, #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
                            update_flag = 1 #True if update False if create
                        )
                        activity_device.save()
                        logged_activity = False
        return updated_devices


    def get_create_flag(self, table, activity):
        create_flag = 0
        if table == 'device':
            if activity.activity.name == 'Rollout':
                create_flag = 1
            elif activity.activity.name == 'Site Deletion':
                create_flag = -1
        elif table == 'cell':
            if activity.activity.name == 'Rollout' or activity.activity.name == 'Expansion':
                create_flag = 1
            elif activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell':
                create_flag = -1
        elif table == 'trx':
            if activity.activity.name == 'Rollout' or activity.activity.name == 'Expansion' \
            or activity.activity.name == 'TRX Expansion':
                create_flag = 1
            elif activity.activity.name == 'Site Deletion' or activity.activity.name == 'Delete Cell' \
            or activity.activity.name == 'TRX Downgrade':
                create_flag = -1
        
        return create_flag

    def get_update_flag(self, activity):
        update_flag = True
        if activity.activity.name == 'Rollout' or activity.activity.name == 'Expansion' \
        or activity.activity.name == 'TRX Expansion':
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

class BSCRNCAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Device.objects.none()

        qs = Device.objects.filter(domain='RAN').filter(Q(function='BC') or Q(function='RN'))

        if self.q:
            qs = qs.filter(device_id__icontains=self.q)

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

class DailyActivityDatatableView(BaseDatatableView):
    model = DailyActivity
    columns = [
        'id', 'date_logged', 'tech', 'user', 'counterpart', 'activity', 'site_status', 'rfs_count', 'siteid',
        'band', 'vendor', 'homing', 'bts_id', 'device_name', 'equipment_type', 'trx_config', 'iub_type',
        'bandwidth', 'sac', 'cell_id', 'cell_name', 'lac', 'pci', 'omip', 's1_c', 's1_u', 'remarks',
    ]

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'date_logged':
            return row.date_logged.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return super(DailyActivityDatatableView, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(activity__name__icontains=search) | Q(siteid__siteid__icontains=search) | Q(tech__icontains=search) | \
            Q(band__icontains=search) | Q(vendor__icontains=search) | Q(site_status__name__icontains=search) | Q(user__username__icontains=search))

        return qs

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
            # return Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band).filter(~Q(record_status=3)).order_by('cell_name')
            #Filter the deleted record status in the client side (JS)
            return Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band).order_by('cell_name')

class GetActivityData(generics.RetrieveAPIView):
    # serializer_class = DailyActivitySerializer

    def get(self, request, pk):
        edit = request.GET.get('edit', None)
        activity = get_object_or_404(DailyActivity, pk=pk)
        if edit:
            data = UpdateLogDailyActivitySerializer(activity).data
        else:
            data = DailyActivitySerializer(activity).data
        return Response(data, status=status.HTTP_200_OK)

class GetBSCRNCNEs(generics.ListAPIView):
    serializer_class = SiteTechBandSerializer
    # queryset = Cell.objects.filter(domain='RAN').filter(Q(function='BC') or Q(function='RN'))
    
    def get_queryset(self):
        device = self.request.GET.get('device_id', None)
        return Cell.objects.filter(device__parent_device_id=device).values('site', 'tech', 'band').order_by('site').distinct()

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