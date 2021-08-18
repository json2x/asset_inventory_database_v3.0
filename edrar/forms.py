
from django import forms
from django.conf.urls import url
from django.contrib.auth.models import User
from .models import DailyActivity, Activity, SiteStatus
from api.models import SmartSite

from dal import autocomplete

class DailyActivityModelForm(forms.ModelForm):
    siteid = forms.ModelChoiceField(
        queryset=SmartSite.objects.all(),
        widget=autocomplete.ModelSelect2(url='siteid-autocomplete', attrs={'id': 'test2', 'class': 'form-control'})
    )

    class Meta:
        model = DailyActivity
        fields = [
            'activity', 'siteid', 'device_name', 'tech', 'band', 'vendor', 'homing', 'bts_id', 
            'equipment_type', 'trx_config', 'iub_type',  'bandwidth', 'sac', 'cell_id',
            'cell_name', 'lac', 'pci', 'omip', 's1_c', 's1_u', 
            'site_status', 'user', 'counterpart', 'rfs_count', 'remarks'
        ]


class DailyActivityForm(forms.Form):
    activity = forms.ModelChoiceField(label='activity', queryset=Activity.objects.all())
    siteid = forms.ModelChoiceField(label='siteid', queryset=SmartSite.objects.all())

    device_name = forms.CharField(max_length=250)
    tech = forms.CharField(max_length=250, widget=forms.HiddenInput())
    vendor = forms.CharField(max_length=250, widget=forms.HiddenInput())
    homing = forms.CharField(max_length=250, widget=forms.HiddenInput())
    equipment_type = forms.CharField(max_length=250, widget=forms.HiddenInput())
    
    bts_id = forms.CharField(max_length=250, widget=forms.HiddenInput())
    band = forms.CharField(max_length=250)
    trx_config = forms.CharField(max_length=250)
    iub_type = forms.CharField(max_length=250)
    bandwidth = forms.IntegerField()
    sac = forms.CharField(max_length=250)
    cell_id = forms.CharField(max_length=250)
    cell_name = forms.CharField(max_length=250)
    lac = forms.CharField(max_length=250)
    pci = forms.CharField(max_length=250)
    omip = forms.CharField(max_length=250)
    s1_c = forms.CharField(max_length=250)
    s1_u = forms.CharField(max_length=250)
    
    site_status = forms.ModelChoiceField(queryset=SiteStatus.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all())
    counterpart = forms.CharField(max_length=250)
    rfs_count = forms.IntegerField()
    remarks = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(DailyActivityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.field.label == 'siteid':
                visible.field.widget.attrs['class'] = 'form-control select2'

