from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from dal import autocomplete
from django_datatables_view.base_datatable_view import BaseDatatableView
from .forms import DailyActivityForm
from .models import MobileTechnology, MobileFrequencyBand
from api.models import SmartSite, Device, Cell

# Create your views here.
#-------------------------------------
def home(request):

    return render(request, 'edrar/home.html')
    #return HttpResponse("eDRAR Home Page.")

def activity_add(request):

    if request.method == 'POST':
        pass

    return render(request, 'edrar/activity_add.html', {'form': DailyActivityForm})

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

class SiteList(ListView):
    
    def get_queryset(self):
        self.site = get_object_or_404(SmartSite, siteid=self.kwargs['site'])
        return SmartSite.objects.filter(siteid=self.site)

class DeviceDatatableView(BaseDatatableView):
    model = Device
    columns = [
        'id', 'device_id', 'site_id', 'ems_id', 'vendor_id', 
        'parent_device_id', 'ne_type', 'subdomain', 'domain', 
        'model', 'function', 'record_status'
    ]

class CellDatatableView(BaseDatatableView):
    model = Cell
    columns = [
        'id', 'domain', 'cell_name', 'parent_id', 'site', 'tech', 'subdomain', 'band', 'ne_type',
        'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 'lcr_cid', 'sector_id',
        'function', 'sdcch_cap', 'tch_cap', 'record_status'
    ]

    def filter_queryset(self, qs):
        deviceStr = self.request.GET.get("columns[2][search][value]", None)
        techStr = self.request.GET.get("columns[4][search][value]", None)
        print(deviceStr)
        qs_params = None
        
        if techStr:
            qs = qs.filter(subdomain=techStr)

        if deviceStr:
            if "|" in deviceStr:
                devices = deviceStr.split('|')
                for device in devices:
                    q = Q(parent_id=device)
                    if qs_params:
                        qs_params = qs_params | q
                    else:
                        qs_params = q

                qs = qs.filter(qs_params)
            else:
                qs = qs.filter(parent_id=deviceStr)
        
        return qs

