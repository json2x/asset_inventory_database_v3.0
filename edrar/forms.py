
from django import forms
from django.conf.urls import url
from django.contrib.auth.models import User
from .models import DailyActivity, Activity, SiteStatus, MobileTechnology, MobileFrequencyBand
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
    tech = forms.ModelChoiceField(label='tech', queryset=MobileTechnology.objects.all())
    band = forms.ModelChoiceField(label='band', queryset=MobileFrequencyBand.objects.all())

    device_name = forms.CharField(max_length=250)
    vendor = forms.CharField(max_length=250)
    homing = forms.CharField(max_length=250)
    equipment_type = forms.CharField(max_length=250)
    
    bts_id = forms.CharField(max_length=250)
    cell_name = forms.CharField(max_length=250)
    cell_id = forms.CharField(max_length=250)
    lac = forms.CharField(max_length=250)
    sac = forms.CharField(max_length=250)
    pci = forms.CharField(max_length=250)

    iub_type = forms.CharField(max_length=250)
    trx_config = forms.CharField(max_length=250)
    bandwidth = forms.IntegerField()
    omip = forms.CharField(max_length=250)
    abis = forms.CharField(max_length=250)
    iubip = forms.CharField(max_length=250)
    s1_c = forms.CharField(max_length=250)
    s1_u = forms.CharField(max_length=250)
    
    site_status = forms.ModelChoiceField(queryset=SiteStatus.objects.all())
    user = forms.ModelChoiceField(queryset=User.objects.all())
    counterpart = forms.CharField(max_length=250)
    rfs_count = forms.IntegerField()
    project_name = forms.CharField(max_length=250)
    remarks = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(DailyActivityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.field.label == 'activity' or visible.field.label == 'siteid' \
                or visible.field.label == 'tech' or visible.field.label == 'band':
                visible.field.widget.attrs['class'] = 'form-control select2'

