# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Device(models.Model):
    dn = models.CharField(db_column='DN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    device_id = models.CharField(db_column='Device ID', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ems_device_id = models.CharField(db_column='EMS Device ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    device_alias = models.CharField(db_column='Device Alias', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    device_ip = models.CharField(db_column='Device IP', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ems_id = models.CharField(db_column='EMS ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_id = models.CharField(db_column='Vendor ID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ne_type = models.CharField(db_column='NE Type', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hardware_description = models.CharField(db_column='Hardware Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    functional_description = models.CharField(db_column='Functional Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parent_device_id = models.CharField(db_column='Parent Device ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parentdn = models.CharField(db_column='ParentDN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    site_id = models.CharField(db_column='Site ID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    device_state = models.CharField(db_column='Device State', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    software_version = models.CharField(db_column='Software Version', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    integration_date = models.CharField(db_column='Integration Date', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_of_support = models.CharField(db_column='End of Support', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tsa_scope = models.CharField(db_column='TSA Scope', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_id = models.CharField(db_column='Product ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_number = models.CharField(db_column='Serial Number', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    freq_tx_rx_field = models.CharField(db_column='FREQ (TX_RX)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hardware_capacity = models.CharField(db_column='Hardware Capacity', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    domain = models.CharField(db_column='Domain', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ne_owner = models.CharField(db_column='NE Owner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tx_clusterimg = models.CharField(db_column='TX Clusterimg', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tx_type = models.CharField(db_column='TX Type', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    natspcode = models.CharField(db_column='NATSPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    admin_state = models.CharField(db_column='Admin State', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subdomain = models.CharField(db_column='SUBDOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function = models.CharField(db_column='FUNCTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iubce_dl_lic = models.CharField(db_column='IUBCE DL LIC', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iubce_ul_lic = models.CharField(db_column='IUBCE UL LIC', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    s1cu_lic = models.CharField(db_column='S1CU LIC', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cluster_region = models.CharField(db_column='Cluster Region', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cluster_sub_region = models.CharField(db_column='Cluster Sub Region', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cluster_province = models.CharField(db_column='Cluster Province', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cluster_city = models.CharField(db_column='Cluster City', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mw_hub = models.CharField(db_column='MW HUB', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    record_status = models.IntegerField(default=1)

    def __str__(self):
        return self.device_id

    @property
    def cells(self):
        return self.cell_set.all()

    @property
    def has_invalid_chars_in_device_name(self):
        device_name = self.device_id
        return not device_name.isalnum()

    class Meta:
        #managed = False
        db_table = 'device'
        unique_together = (('dn', 'device_id', 'ems_id', 'ne_type'),)
        verbose_name_plural = 'Devices'


class Cell(models.Model):
    domain = models.CharField(db_column='Domain', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ems_cell_id = models.CharField(db_column='EMS Cell ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ems_id = models.CharField(db_column='EMS ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cell_name = models.CharField(db_column='Cell Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dn = models.CharField(db_column='DN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=10)  # Field name made lowercase.
    parent_id = models.CharField(db_column='Parent ID', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parent_dn = models.CharField(db_column='Parent DN', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tech = models.CharField(db_column='Tech', max_length=50, blank=True, null=True)  # Field name made lowercase.
    band = models.CharField(db_column='Band', max_length=5)  # Field name made lowercase.
    admin_state = models.CharField(db_column='Admin State', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alias = models.CharField(db_column='Alias', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lac_tac = models.CharField(db_column='LAC TAC', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sac_ci_eutra = models.CharField(db_column='SAC CI EUTRA', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rnc_cid = models.CharField(db_column='RNC CID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phy_cid = models.CharField(db_column='PHY CID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lcr_cid = models.CharField(db_column='LCR CID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mcc = models.CharField(db_column='MCC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mnc = models.CharField(db_column='MNC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nodeid = models.CharField(db_column='NODEID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR ID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carrier = models.CharField(db_column='CARRIER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ne_type = models.CharField(db_column='NE TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subdomain = models.CharField(db_column='SUBDOMAIN', max_length=10)  # Field name made lowercase.
    function = models.CharField(db_column='FUNCTION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sdcch_cap = models.CharField(db_column='SDCCH CAP', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tch_cap = models.CharField(db_column='TCH CAP', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    azimuth = models.CharField(db_column='Azimuth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    record_status = models.IntegerField(default=1)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.cell_name

    class Meta:
        #managed = False
        db_table = 'cell'
        unique_together = (('ems_id', 'dn', 'site', 'band', 'subdomain'),)
        verbose_name_plural = 'Cells'


class Location(models.Model):
    code = models.IntegerField()
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=30)
    region = models.CharField(max_length=4)
    regionname = models.CharField(max_length=40)
    area = models.CharField(max_length=3)

    def __str__(self):
        return "{} | {}".format(self.province, self.city)

    class Meta:
        #managed = False
        db_table = 'location'


class TocAor(models.Model):
    cluster = models.CharField(unique=True, max_length=25)
    area = models.CharField(max_length=3)
    supervisor = models.CharField(max_length=60, blank=True, null=True)
    manager = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.cluster

    class Meta:
        #managed = False
        db_table = 'toc_aor'

class SmartSite(models.Model):
    siteid = models.CharField(unique=True, max_length=10)
    sitename = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    toc_aor = models.ForeignKey('TocAor', on_delete=models.SET_NULL, blank=True, null=True)
    lat = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    lng = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.siteid

    @property
    def smartne(self):
        return self.smartne_set.all()

    class Meta:
        #managed = False
        db_table = 'smart_site'


class SmartNe(models.Model):
    #siteid = models.ForeignKey('SmartSite', models.DO_NOTHING, db_column='siteid')
    siteid = models.CharField(max_length=10)
    band = models.CharField(max_length=5)
    tech = models.CharField(max_length=10)
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)
    smartsite = models.ForeignKey('SmartSite', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}_{}".format(self.siteid, self.band, self.tech)

    class Meta:
        #managed = False
        db_table = 'smart_ne'
        unique_together = (('siteid', 'band', 'tech'),)


class SiteNeAsset(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    smartsite = models.ForeignKey('SmartSite', on_delete=models.CASCADE)
    smartne = models.ForeignKey('SmartNe', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'site_ne_asset'
        unique_together = (('cell', 'smartsite', 'smartne', 'device'),)

class SmartParkedNe(models.Model):
    sitene = models.ForeignKey('SmartNE', on_delete=models.CASCADE)
    date_parked = models.DateTimeField()
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'smart_parked_ne'

class DeviceSyncStatus(models.Model):
    device_name = models.CharField(max_length=250, unique=True)
    ne_type = models.CharField(max_length=50)
    sync_status = models.CharField(max_length=25)
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'device_sync_status'
'''
class ApiUserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'api_user_token'
'''

