
from django import forms
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import DailyActivity, Activity, SiteStatus, MobileTechnology, MobileFrequencyBand
from api.models import SmartSite

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

class DailyActivityReportGeneratorForm(forms.Form):
    activity = forms.ChoiceField()
    project_name = forms.CharField(max_length=250)
    start = forms.DateField()
    end = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(DailyActivityReportGeneratorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'my-form-control'
            if visible.field.label == 'activity':
                visible.field.widget.attrs['class'] = 'my-form-control select2'

class PasswordResetFormExtra(PasswordChangeForm):
    def __init__(self, *args, **kw):
        super(PasswordResetFormExtra, self).__init__(*args, **kw)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'edrar_user_change_password'
        self.helper.add_input(Submit('submit', 'Submit'))