from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request
from django.views import View
from django.db.models import Q

from dal import autocomplete
from django_datatables_view.base_datatable_view import BaseDatatableView
from .forms import DailyActivityForm
from .models import Activity, MobileTechnology, MobileFrequencyBand
from api.models import SmartSite, Device, Cell, Trx
from api.serializers import DevicesSerializer, CellsSerializer, TrxSerializer
from .serializers import CellsDeviceTrxSerializer, NmsDevicesSerializer, NmsCellsSerializer, NmsTrxSerializer
from rest_framework import generics

from edrar import serializers

# Create your views here.
#-------------------------------------
def home(request):

    return render(request, 'edrar/home.html')
    #return HttpResponse("eDRAR Home Page.")

def activity_add(request):

    if request.method == 'POST':
        pass

    return render(request, 'edrar/activity_add.html', {'form': DailyActivityForm})

class AddActivity(View):
    template_name = 'edrar/activity_add.html'
    form_class = DailyActivityForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})


class ActivityAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Activity.objects.none()

        qs = Activity.objects.all()

        if self.q:
            qs = qs.filter(siteid__icontains=self.q)

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
            if tbl_ids.find(';') > 1:
                tbl_ids = tbl_ids.split(';')
                for tbl_id in tbl_ids:
                    qs_params = None
                    if qs_params:
                        qs_params = qs_params | Q(id=tbl_id)
                    else:
                        qs_params = Q(id=tbl_id)
                qs = qs.filter(qs_params)
            else:
                 qs = qs.filter(id=tbl_ids)
        else:
            qs = qs.filter(site_id=site).filter(subdomain=tech)

        return qs

class NmsDeviceDatatableView(BaseDatatableView):
    model = Device #Change to nmsdata Device data model
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
            if tbl_ids.find(';') > 1:
                tbl_ids = tbl_ids.split(';')
                for tbl_id in tbl_ids:
                    qs_params = None
                    if qs_params:
                        qs_params = qs_params | Q(id=tbl_id)
                    else:
                        qs_params = Q(id=tbl_id)
                qs = qs.filter(qs_params)
            else:
                 qs = qs.filter(id=tbl_ids)
        else:
            qs = qs.filter(site_id=site).filter(subdomain=tech)

        return qs

class CellDatatableView(BaseDatatableView):
    model = Cell
    columns = [
        'id', 'domain', 'ems_id', 'nodeid', 'cell_name', 'parent_id', 'parent_dn', 'site', 'tech', 'subdomain', 'band', 'ne_type',
        'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 'lcr_cid', 'sector_id',
        'function', 'sdcch_cap', 'tch_cap', 'record_status'
    ]

class NmsCellDatatableView(BaseDatatableView):
    model = Cell #Change to nmsdata Cell data model
    columns = [
        'id', 'domain', 'ems_id', 'nodeid', 'cell_name', 'parent_id', 'parent_dn', 'site', 'tech', 'subdomain', 'band', 'ne_type',
        'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 'lcr_cid', 'sector_id',
        'function', 'sdcch_cap', 'tch_cap', 'record_status'
    ]

class TrxDatatableView(BaseDatatableView):
    model = Trx
    columns = [
        'id', 'ems_id', 'trx_name', 'parent_id', 'admin_state', 'e1_assignment', 'homing_bts', 'cell', 'device'
    ]

    def filter_queryset(self, qs):

        search = self.request.GET.get('columns[5][search][value]', None)
        if search.find(';') > 1:
            search = search.split(';')

        if type(search) is list:
            qs_params = None
            for cellid in search:
                if qs_params:
                    qs_params = qs_params | Q(cell=int(cellid))
                else:
                    qs_params = Q(cell=int(cellid))
            qs = qs.filter(qs_params)
        else:
            qs = qs.filter(cell=int(search))

        return qs

class NmsTrxDatatableView(BaseDatatableView):
    model = Trx #Change to nmsdata Trx data model
    columns = [
        'id', 'ems_id', 'trx_name', 'parent_id', 'admin_state', 'e1_assignment', 'homing_bts', 'cell', 'device'
    ]

    def filter_queryset(self, qs):

        search = self.request.GET.get('columns[5][search][value]', None)
        if search.find(';') > 1:
            search = search.split(';')

        if type(search) is list:
            qs_params = None
            for cellid in search:
                if qs_params:
                    qs_params = qs_params | Q(cell=int(cellid))
                else:
                    qs_params = Q(cell=int(cellid))
            qs = qs.filter(qs_params)
        else:
            qs = qs.filter(cell=int(search))

        return qs

class ActivityLogTextFieldData(generics.ListAPIView):
    serializer_class = CellsDeviceTrxSerializer
    
    def get_queryset(self):
        site = self.request.GET.get('site', None)
        tech = self.request.GET.get('tech', None)
        band = self.request.GET.get('band', None)

        return Cell.objects.filter(site=site).filter(subdomain=tech).filter(band=band)

class GetDeviceDataByID(generics.ListAPIView):
    serializer_class = DevicesSerializer

    def get_queryset(self):
        id = self.request.GET.get('id', None)
        self.serializer_class = self.get_serializer_class()

        qs_params = None
        if id.find(';'):
            ids = id.split(';')
            for id in ids:
                if qs_params:
                    qs_params = qs_params | Q(id=id)
                else:
                    qs_params = Q(id=id)
            qs = Device.objects.filter(qs_params)
        else:
            qs = Device.objects.filter(id=id)

        return qs

    def get_serializer_class(self):
        data_source = self.request.GET.get('src', None)
        if data_source and data_source == 'nms':
            return NmsDevicesSerializer
        else:
            return DevicesSerializer

class GetCellDataByID(generics.ListAPIView):
    serializer_class = CellsSerializer
    
    def get_queryset(self):
        id = self.request.GET.get('id', None)
        self.serializer_class = self.get_serializer_class()

        qs_params = None
        if id.find(';'):
            ids = id.split(';')
            for id in ids:
                if qs_params:
                    qs_params = qs_params | Q(id=id)
                else:
                    qs_params = Q(id=id)
            qs = Cell.objects.filter(qs_params)
        else:
            qs = Cell.objects.filter(id=id)

        return qs

    def get_serializer_class(self):
        data_source = self.request.GET.get('src', None)
        if data_source and data_source == 'nms':
            return NmsCellsSerializer
        else:
            return CellsSerializer

class GetTrxDataByID(generics.ListAPIView):
    serializer_class = TrxSerializer
    
    def get_queryset(self):
        id = self.request.GET.get('id', None)
        self.serializer_class = self.get_serializer_class()

        qs_params = None
        if id.find(';'):
            ids = id.split(';')
            for id in ids:
                if qs_params:
                    qs_params = qs_params | Q(id=id)
                else:
                    qs_params = Q(id=id)
            qs = Trx.objects.filter(qs_params)
        else:
            qs = Trx.objects.filter(id=id)

        return qs

    def get_serializer_class(self):
        data_source = self.request.GET.get('src', None)
        if data_source and data_source == 'nms':
            return NmsTrxSerializer
        else:
            return TrxSerializer