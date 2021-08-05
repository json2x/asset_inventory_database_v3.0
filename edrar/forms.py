
from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth.models import User
from .models import DailyActivity, Activity, SiteStatus
from api.models import SmartSite

class DailyActivityModelForm(ModelForm):

    class Meta:
        model = DailyActivity
        fields = [
            'date_logged', 'tech', 'user', 'counterpart', 'activity', 'site_status',
            'rfs_count', 'siteid', 'vendor', 'homing', 'bts_id', 'device_name',
            'equipment_type', 'trx_config', 'iub_type', 'bandwidth', 'sac', 'cell_id',
            'cell_name', 'lac', 'pci', 'omip', 's1_c', 's1_u', 'remarks'
        ]

class DailyActivityForm(Form):
    activity = forms.ModelChoiceField(queryset=Activity.objects.all())
    siteid = forms.ModelChoiceField(queryset=SmartSite.objects.all())

    device_name = forms.CharField(max_length=250)
    tech = forms.CharField(max_length=250)
    band = forms.CharField(max_length=250)
    vendor = forms.CharField(max_length=250)
    homing = forms.CharField(max_length=250)
    bts_id = forms.CharField(max_length=250)
    
    equipment_type = forms.CharField(max_length=250)
    trx_config = forms.CharField(max_length=250)
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
    remarks = forms.CharField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(DailyActivityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

