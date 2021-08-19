from django.db import models
from django.contrib.auth import get_user_model
from api.models import SmartSite, Device, Cell, Trx

# Create your models here.
User = get_user_model()

class Activity(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'

class MobileTechnology(models.Model):
    name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Mobile Technologies'

class SiteStatus(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Site Statuses'

class DailyActivityModified(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    field = models.CharField(max_length=250, blank=True, null=True)
    old_value = models.CharField(max_length=250, blank=True, null=True)
    new_value = models.CharField(max_length=250, blank=True, null=True)

class DailyActivity(models.Model):
    date_logged = models.DateTimeField()
    tech = models.CharField(max_length=250)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    counterpart = models.CharField(max_length=250, blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    site_status = models.ForeignKey(SiteStatus, on_delete=models.PROTECT)
    rfs_count = models.IntegerField(blank=True, null=True)
    siteid = models.ForeignKey(SmartSite, models.SET_NULL, blank=True, null=True)
    band = models.CharField(max_length=250, blank=True, null=True)
    vendor = models.CharField(max_length=250, blank=True, null=True)
    homing = models.CharField(max_length=250, blank=True, null=True)
    bts_id = models.CharField(max_length=250, blank=True, null=True)
    device_name = models.CharField(max_length=250, blank=True, null=True)
    equipment_type = models.CharField(max_length=250, blank=True, null=True) #model field in device?
    trx_config = models.CharField(max_length=250, blank=True, null=True)
    #trx_count = models.IntegerField(max_length=3, blank=True, null=True)
    iub_type = models.CharField(max_length=250, blank=True, null=True)
    bandwidth = models.IntegerField(blank=True, null=True)
    sac = models.CharField(max_length=250, blank=True, null=True)
    cell_id = models.CharField(max_length=250, blank=True, null=True)
    cell_name = models.CharField(max_length=250, blank=True, null=True)
    lac = models.CharField(max_length=250, blank=True, null=True)
    #cell_count = models.IntegerField(max_length=2, blank=True, null=True)
    pci = models.CharField(max_length=250, blank=True, null=True)
    omip = models.CharField(max_length=250, blank=True, null=True)
    s1_c = models.CharField(max_length=250, blank=True, null=True)
    s1_u = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    modified = models.ForeignKey(DailyActivityModified, models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Daily Activities'

class DailyActivity_SmartSite(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    daily_activity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    site = models.ForeignKey(SmartSite, on_delete=models.CASCADE)
    create_flag = models.IntegerField(blank=True, null=True) #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
    update_flag = models.BooleanField()

class DailyActivity_Device(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    daily_activity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    create_flag = models.IntegerField(blank=True, null=True) #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
    update_flag = models.BooleanField()

class DailyActivity_Cell(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    daily_activity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    create_flag = models.IntegerField(blank=True, null=True) #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
    update_flag = models.BooleanField()

class DailyActivity_Trx(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    daily_activity = models.ForeignKey(DailyActivity, on_delete=models.CASCADE)
    trx = models.ForeignKey(Trx, on_delete=models.CASCADE)
    create_flag = models.IntegerField(blank=True, null=True) #Values can be -1, 0, 1 for deleted, no-addition, new rollout respectively
    update_flag = models.BooleanField()