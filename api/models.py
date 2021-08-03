from django.db import models
from django.contrib.auth import get_user_model


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

class AccessConstraint(models.Model):
    area = models.CharField(db_column='DN', max_length=5, blank=True, null=True)
    site_id = models.CharField(db_column='Site ID', max_length=5, blank=True, null=True)
    exact_date = models.CharField(db_column='Exact Date', max_length=5, blank=True, null=True)
    day_of_month = models.CharField(db_column='Day of Month', max_length=10, blank=True, null=True)
    day_of_week = models.CharField(db_column='Day of Week', max_length=10, blank=True, null=True)
    start_time = models.CharField(db_column='Start Time', max_length=5, blank=True, null=True)
    end_time = models.CharField(db_column='End Time', max_length=5, blank=True, null=True)
    restricted_time = models.CharField(db_column='Restricted Time', max_length=10, blank=True, null=True)
    site_name = models.CharField(db_column='Site Name', max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'accessconstraint'

class LR_3G_IMA_GRP(models.Model):
    ems_id = models.CharField(db_column='EMS_ID', max_length=10, blank=True, null=True)
    idnum = models.CharField(db_column='IDNUM', max_length=130, blank=True, null=True)
    dn = models.CharField(db_column='DN', max_length=130, blank=True, null=True)
    parent_id = models.CharField(db_column='Parent ID', max_length=20, blank=True, null=True)
    parent_dn = models.CharField(db_column='Parent DN', max_length=130, blank=True, null=True)

    class Meta:
        db_table = 'lr_3g_ima_grp'

class LR_3G_IMA_LNK(models.Model):
    ems_id = models.CharField(db_column='EMS_ID', max_length=10, blank=True, null=True)
    idnum = models.CharField(db_column='IDNUM', max_length=140, blank=True, null=True)
    dn = models.CharField(db_column='DN', max_length=140, blank=True, null=True)
    parent_id = models.CharField(db_column='Parent ID', max_length=130, blank=True, null=True)
    parent_dn = models.CharField(db_column='Parent DN', max_length=130, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'lr_3g_ima_lnk'

class LRBandwidth(models.Model):
    device_id = models.CharField(db_column='Device ID', max_length=60, blank=True, null=True)
    bandwidth = models.CharField(db_column= 'Bandwidth', max_length=15, blank=True, null=True)
    tech = models.CharField(db_column='Tech', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lr_bandwidth'

class LRBSC(models.Model):
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=True)
    bsc_no = models.CharField(db_column='BSC No', max_length=20, blank=True, null=True)
    bsc_loc = models.CharField(db_column='BSC LOCATION', max_length=30, blank=True, null=True)
    ao_ipbh_cap = models.CharField(db_column='AO IP BH Capacity', max_length=5, blank=True, null=True)
    sig_bh_cap = models.CharField(db_column='SIGTRAN BH Capacity', max_length=250, blank=True, null=True)
    gbo_ipbh_cap = models.CharField(db_column='GBO IP BH Capacity', max_length=5, blank=True, null=True)
    combined_ipbh = models.CharField(db_column='COMBINED IP BH Capacity', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lrbsc'

class LRBSC_RNC(models.Model):
    ne_name = models.CharField(db_column='NE NAME', max_length=10, blank=True, null=True)
    msc_poolname = models.CharField(db_column='MSC POOL NAME', max_length=250, blank=True, null=True)
    msc_name = models.CharField(db_column='MSC NAME', max_length=5, blank=True, null=True)
    spc_name = models.CharField(db_column='SPC NAME', max_length=10, blank=True, null=True)
    int_net_code = models.CharField(db_column='INT NET CODE', max_length=250, blank=True, null=True)
    int_spnet_code = models.CharField(db_column='INT SP NET CODE', max_length=250, blank=True, null=True)
    nat_code = models.CharField(db_column='NAT CODE', max_length=250, blank=True, null=True)
    nat_sp_code = models.CharField(db_column='NAT SP CODE', max_length=10, blank=True, null=True)
    sgsn_name = models.CharField(db_column='SGSN NAME', max_length=250, blank=True, null=True)
    sgsn_pool_name = models.CharField(db_column='SGSN POOL NAME', max_length=250, blank=True, null=True)
    ne_index = models.CharField(db_column='NE INDEX', max_length=5, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=5, blank=True, null=True)
    netid = models.CharField(db_column='NET ID', max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'lrbsc_rnc'

class LRCEMDEV(models.Model):
    dn = models.CharField(db_column='DN', max_length=20, blank=True, null=True)
    ne_type = models.CharField(db_column='NE TYPE', max_length=5, blank=True, null=True)
    home_msc_pool = models.CharField(db_column='Home MSC Pool', max_length=10, blank=True, null=True)
    gt_address = models.CharField(db_column='Gt Address', max_length=20, blank=True, null=True)
    msc_server_type = models.CharField(db_column='MSC Server Type', max_length=5, blank=True, null=True)
    carrier = models.CharField(db_column='Carrier', max_length=5, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=20, blank=True, null=True)
    spc_name = models.CharField(db_column='SPC Name', max_length=10, blank=True, null=True)
    int_net_code = models.CharField(db_column='International Network Code', max_length=5, blank=True, null=True)
    int_spnet = models.CharField(db_column='International Spare Network', max_length=5, blank=True, null=True)
    nat_net_code = models.CharField(db_column='National Network Code', max_length=5, blank=True, null=True)
    nat_spnet_code = models.CharField(db_column='National Spare Network Code', max_length=5, blank=True, null=True)
    bcu = models.CharField(db_column='BCU', max_length=5, blank=True, null=True)
    homing_msc = models.CharField(db_column='Homing Msc', max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'lrcemdev'

class LRCEMIP(models.Model):
    dn = models.CharField(db_column='DN', max_length=20, blank=True, null=True)
    ne_type = models.CharField(db_column='NE Type', max_length=5, blank=True, null=True)
    ip_add = models.CharField(db_column='IP Address', max_length=15, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lrcemip'

class LRCEMNRI(models.Model):
    dn = models.CharField(db_column='DN', max_length=20, blank=True, null=True)
    nri = models.CharField(db_column='NRI', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lrcemnri'

class LR_CSPGCTRL(models.Model):
    pg_pol = models.CharField(db_column='PG POL', max_length=5, blank=True, null=True)
    msc_spc = models.CharField(db_column='MSC SPC', max_length=10, blank=True, null=True)
    lai = models.CharField(db_column='LAI', max_length=10, blank=True, null=True)
    pg_type = models.CharField(db_column='PG TYPE', max_length=20, blank=True, null=True)
    pg_times = models.CharField(db_column='PG TIMES', max_length=5, blank=True, null=True)
    pg1_durh = models.CharField(db_column='PG1 DURH', max_length=5, blank=True, null=True)
    pg1_idt = models.CharField(db_column='PG1 IDT', max_length=5, blank=True, null=True)
    pg2_durh = models.CharField(db_column='PG2 DURH', max_length=5, blank=True, null=True)
    pg2_idt = models.CharField(db_column='PG2 IDT', max_length=5, blank=True, null=True)
    pg3_durh = models.CharField(db_column='PG3 DURH', max_length=5, blank=True, null=True)
    lpg3_idtai = models.CharField(db_column='LPG3 IDTAI', max_length=5, blank=True, null=True)
    pg4_durh = models.CharField(db_column='PG4 DURH', max_length=5, blank=True, null=True)
    pg4_idt = models.CharField(db_column='PG4 IDT', max_length=5, blank=True, null=True)
    pg5_durh = models.CharField(db_column='PG5 DURH', max_length=5, blank=True, null=True)
    pg5_idt = models.CharField(db_column='PG5 IDT', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lr_cspgctrl'

class LR_ENODEB(models.Model):
    ne_id = models.CharField(db_column=' NE ID', max_length=10, blank=True, null=True)
    ne_name = models.CharField(db_column='NE NAME', max_length=30, blank=True, null=True)
    cpia = models.CharField(db_column='CPIA', max_length=20, blank=True, null=True)
    upia = models.CharField(db_column='UPIA', max_length=20, blank=True, null=True)
    mme_name = models.CharField(db_column='MME NAME', max_length=250, blank=True, null=True)
    mcc = models.CharField(db_column='MCC', max_length=5, blank=True, null=True)
    mnc = models.CharField(db_column='MNC', max_length=5, blank=True, null=True)
    mme_pname = models.CharField(db_column='MME POOL NAME', max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'lr_enodeb'

class LR_ERDIP(models.Model):
    bsc_id = models.CharField(db_column='BSC.ID', max_length=10, blank=True, null=True)
    rbl_id = models.CharField(db_column='RBL.ID', max_length=5, blank=True, null=True)
    tg_id = models.CharField(db_column='TG.ID', max_length=10, blank=True, null=True)
    device_id = models.CharField(db_column='DEVICE.ID', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lr_erdip'

class LR_IP_POOLINV(models.Model):
    device_id = models.CharField(db_column='DEVICE ID', max_length=20, blank=True, null=True)
    apn = models.CharField(db_column='APN', max_length=50, blank=True, null=True)
    ip_pname = models.CharField(db_column='IP POOL NAME', max_length=30, blank=True, null=True)
    cidr = models.CharField(db_column='CIDR', max_length=20, blank=True, null=True)
    iprange = models.CharField(db_column='IPRANGE', max_length=60, blank=True, null=True)
    totalips = models.CharField(db_column='TOTALIPS', max_length=5, blank=True, null=True)
    usableips = models.CharField(db_column='USABLEIPS', max_length=5, blank=True, null=True)
    remarks = models.CharField(db_column='REMARKS', max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'lr_ip_polinv'

class LR_LINK(models.Model):
    idnum = models.CharField(db_column='IDNUM', max_length=5, blank=True, null=True)
    create_date = models.CharField(db_column='Create Date', max_length=250, blank=True, null=True)
    dn = models.CharField(db_column='DN', max_length=250, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)
    update_date = models.CharField(db_column='Update Date', max_length=250, blank=True, null=True)
    link_type = models.CharField(db_column='Link Type', max_length=10, blank=True, null=True)
    aend_node = models.CharField(db_column='AEND Node', max_length=70, blank=True, null=True)
    aend_tp = models.CharField(db_column='AEND TP', max_length=60, blank=True, null=True)
    add_info = models.CharField(db_column='Additional Info', max_length=250, blank=True, null=True)
    aend_ip = models.CharField(db_column='AEND IP', max_length=20, blank=True, null=True)
    service = models.CharField(db_column='Service', max_length=20, blank=True, null=True)
    direction = models.CharField(db_column='Direction-', max_length=5, blank=True, null=True)
    ems_name = models.CharField(db_column='EMS Name', max_length=30, blank=True, null=True)
    native_ems_name = models.CharField(db_column='Native EMS Name', max_length=15, blank=True, null=True)
    owner = models.CharField(db_column='Owner', max_length=5, blank=True, null=True)
    parent_dn = models.CharField(db_column='Parent DN', max_length=250, blank=True, null=True)
    rate = models.CharField(db_column='Rate', max_length=20, blank=True, null=True)
    usr_label = models.CharField(db_column='User Label', max_length=150, blank=True, null=True)
    zend_node = models.CharField(db_column='ZEND Node', max_length=70, blank=True, null=True)
    zend_tp = models.CharField(db_column='ZEND TP', max_length=80, blank=True, null=True)
    zend_ip = models.CharField(db_column='ZEND IP', max_length=20, blank=True, null=True)
    date_res_id = models.CharField(db_column='Date Resource ID', max_length=250, blank=True, null=True)
    domain = models.CharField(db_column='Domain', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lr_link'

class LR_LTunnel(models.Model):
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)
    linktype = models.CharField(db_column='LINK TYPE', max_length=10, blank=True, null=True)
    capacity = models.CharField(db_column='CAPACITY', max_length=250, blank=True, null=True)
    tunnel_id = models.CharField(db_column='TUNNEL ID', max_length=15, blank=True, null=True)
    tunnel_bandwidth = models.CharField(db_column='TUNNEL BANDWIDTH', max_length=250, blank=True, null=True)
    aendnode_sitecodes = models.CharField(db_column='AENDNODE SITECODES', max_length=5, blank=True, null=True)
    aend_node = models.CharField(db_column='AENDNODE', max_length=20, blank=True, null=True)
    aend_tp = models.CharField(db_column='AEND TP', max_length=35, blank=True, null=True)
    aend_tp_child = models.CharField(db_column='AEND TP (CHILD)', max_length=250, blank=True, null=True)
    aend_ip = models.CharField(db_column='AEND IP', max_length=250, blank=True, null=True)
    aend_eq = models.CharField(db_column='AEND EQUIPMENT', max_length=10, blank=True, null=True)
    zend_nodes_sitecodes = models.CharField(db_column='ZENDNODE SITECODES', max_length=5, blank=True, null=True)
    zend_node = models.CharField(db_column='ZENDNODE', max_length=20, blank=True, null=True)
    zend_tp = models.CharField(db_column='ZEND TP', max_length=35, blank=True, null=True)
    zend_tp_child = models.CharField(db_column='ZEND TP (CHILD)', max_length=250, blank=True, null=True)
    zend_ip = models.CharField(db_column='ZEND IP', max_length=250, blank=True, null=True)
    zend_eq = models.CharField(db_column='ZEND EQUIPMENT', max_length=10, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=30, blank=True, null=True)
    domain = models.CharField(db_column='DOMAIN', max_length=250, blank=True, null=True)
    cluster = models.CharField(db_column='CLUSTER', max_length=250, blank=True, null=True)
    cao_wo = models.CharField(db_column='CAO/WO', max_length=250, blank=True, null=True)
    band_service = models.CharField(db_column='BAND/SERVICE', max_length=250, blank=True, null=True)
    direction = models.CharField(db_column='DIRECTION', max_length=250, blank=True, null=True)
    remarks = models.CharField(db_column='REMARKS', max_length=60, blank=True, null=True)
    rnc_bsc = models.CharField(db_column='RNC/BSC', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'lr_ltunnel'

class LR_NBINT(models.Model):
    domain = models.CharField(db_column='Domain', max_length=20, blank=True, null=True)
    ems_id = models.CharField(db_column='EMS ID', max_length=20, blank=True, null=True)
    parent_id = models.CharField(db_column='Parent ID', max_length=40, blank=True, null=True)
    lip_1 = models.CharField(db_column='LIP 1', max_length=20, blank=True, null=True)
    lip_2 = models.CharField(db_column='LIP 2', max_length=40, blank=True, null=True)
    own_spc = models.CharField(db_column='Own SPC', max_length=20, blank=True, null=True)
    assoc_set_id = models.CharField(db_column='Assoc Set ID', max_length=20, blank=True, null=True)
    assoc_set_name = models.CharField(db_column='Assoc Set Name', max_length=40, blank=True, null=True)
    assoc_index = models.CharField(db_column='Assoc Index', max_length=40, blank=True, null=True)
    rip_1 = models.CharField(db_column='RIP 1', max_length=30, blank=True, null=True)
    rip_2 = models.CharField(db_column='RIP 2', max_length=50, blank=True, null=True)
    use = models.CharField(db_column='USE', max_length=30, blank=True, null=True)
    class_nbint = models.CharField(db_column='Class', max_length=20, blank=True, null=True)
    assoc_name = models.CharField(db_column='ASSOC NAME', max_length=50, blank=True, null=True)
    local_port = models.CharField(db_column='LOCAL PORT', max_length=10, blank=True, null=True)
    peer_port = models.CharField(db_column='PEER PORT', max_length=10, blank=True, null=True)
    deno = models.CharField(db_column='DENO', max_length=10, blank=True, null=True)
    deno_name = models.CharField(db_column='DENO NAME', max_length=40, blank=True, null=True)
    leno = models.CharField(db_column='LENO', max_length=5, blank=True, null=True)
    leno_name = models.CharField(db_column='LENO NAME', max_length=40, blank=True, null=True)
    peer_device_id = models.CharField(db_column='PEER DEVICE ID', max_length=20, blank=True, null=True)
    peer_spc = models.CharField(db_column='PEER SPC', max_length=10, blank=True, null=True)
    peer_nsei = models.CharField(db_column='PEER A SET ID NSEI', max_length=250, blank=True, null=True)
    peer_assoc_set = models.CharField(db_column='PEER ASSOC SET NAME', max_length=250, blank=True, null=True)
    name = models.CharField(db_column='', max_length=250, blank=True, null=True)
    peer_assoc_index = models.CharField(db_column='PEER ASSOC INDEX', max_length=250, blank=True, null=True)
    peer_assoc_name = models.CharField(db_column='PEER ASSOC NAME', max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'lr_nbint'

class LR_PCCapacity(models.Model):
    idnum = models.CharField(db_column='IDNUM', max_length=20, blank=True, null=True)
    device_id = models.CharField(db_column='Device ID', max_length=30, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)
    area_served = models.CharField(db_column='Area Served', max_length=10, blank=True, null=True)
    sw_release = models.CharField(db_column='SW Reease', max_length=20, blank=True, null=True)
    hw_capacity_sau = models.CharField(db_column='HW Capacity (SAU)', max_length=10, blank=True, null=True)
    hw_capacity_pdp = models.CharField(db_column='HW Capacity (PDP)', max_length=250, blank=True, null=True)
    sw_capacity_sau = models.CharField(db_column='SW Capacity (SAU)', max_length=250, blank=True, null=True)
    sw_capacity_pdp = models.CharField(db_column='SW Capacity (PDP)', max_length=250, blank=True, null=True)
    hw_capacity_tput = models.CharField(db_column='HW Capacity (TPUT)', max_length=10, blank=True, null=True)
    hw_capacity_pdp1 = models.CharField(db_column='HW Capacity (PDP)1', max_length=250, blank=True, null=True)
    purchasedsw_capacity_tput = models.CharField(db_column='PurchasedSW (TPUT)', max_length=250, blank=True, null=True)
    purchasedsw_pdp = models.CharField(db_column='PurchasedSW (PDP)', max_length=10, blank=True, null=True)
    ecu_sau = models.CharField(db_column='ECU (SAU)', max_length=10, blank=True, null=True)
    epu_pdp = models.CharField(db_column='EPU (PDP)', max_length=10, blank=True, null=True)
    ecu = models.CharField(db_column='ECU', max_length=5, blank=True, null=True)
    epu = models.CharField(db_column='EPU', max_length=5, blank=True, null=True)
    redunduncy_model = models.CharField(db_column='Redunduncy Model', max_length=5, blank=True, null=True)
    no_of_subrack = models.CharField(db_column='No Of SubRack', max_length=5, blank=True, null=True)
    gsc = models.CharField(db_column='GSC', max_length=5, blank=True, null=True)
    active_cpb = models.CharField(db_column='Active CPB', max_length=5, blank=True, null=True)
    standyby_cpb = models.CharField(db_column='Standby CPB', max_length=5, blank=True, null=True)
    active_ppb = models.CharField(db_column='Active PPB', max_length=5, blank=True, null=True)
    standby_ppb = models.CharField(db_column='Standby PPB', max_length=5, blank=True, null=True)
    lc = models.CharField(db_column='LC', max_length=5, blank=True, null=True)
    tput = models.CharField(db_column='TPUT', max_length=5, blank=True, null=True)
    board_type = models.CharField(db_column='Board Type', max_length=5, blank=True, null=True)
    no_of_boards = models.CharField(db_column='No Of Boards', max_length=5, blank=True, null=True)
    sw_capacity = models.CharField(db_column='SW Capacity', max_length=10, blank=True, null=True)
    chasis_type = models.CharField(db_column='Chasis Type', max_length=20, blank=True, null=True)
    blade_type = models.CharField(db_column='Blade Type', max_length=5, blank=True, null=True)
    blade_capacity = models.CharField(db_column='Blade Capacity', max_length=10, blank=True, null=True)
    total_no_of_blades = models.CharField(db_column='Total Number of Blades', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lr_pccapacity'

class LR_Parked(models.Model):
    site_no = models.CharField(db_column='SITENO', max_length=10, blank=True, null=True)
    band = models.CharField(db_column='BAND', max_length=10, blank=True, null=True)
    tech = models.CharField(db_column='TECH', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'lr_parked'

class LR_PSCoreDevice(models.Model):
    dn = models.CharField(db_column='DN', max_length=15, blank=True, null=True)
    device_id = models.CharField(db_column='Device ID', max_length=15, blank=True, null=True)
    ems_id = models.CharField(db_column='EMS ID', max_length=20, blank=True, null=True)
    vendor_id = models.CharField(db_column='VendorID', max_length=5, blank=True, null=True)
    ne_type = models.CharField(db_column='NE Type', max_length=5, blank=True, null=True)
    site_id = models.CharField(db_column='Site ID', max_length=10, blank=True, null=True)
    sau_license_sw = models.CharField(db_column='SAU License SW', max_length=10, blank=True, null=True)
    sau_hw = models.CharField(db_column='SAU HW', max_length=10, blank=True, null=True)
    pdp_license_sw = models.CharField(db_column='PDP License SW', max_length=10, blank=True, null=True)
    th_license_sw = models.CharField(db_column='Throughput License SW', max_length=10, blank=True, null=True)
    th_hw_gbps = models.CharField(db_column='Throughput HW(Gbps)', max_length=5, blank=True, null=True)
    maxnum_2g_subs_sw = models.CharField(db_column='Max num of 2G subs SW', max_length=5, blank=True, null=True)
    maxnum_3g_subs_sw = models.CharField(db_column='Max num of 3G subs SW', max_length=5, blank=True, null=True)
    maxnum_4g_subs_sw = models.CharField(db_column='Max num of 4G subs SW', max_length=5, blank=True, null=True)
    maxnum_2g_actpdp_sw = models.CharField(db_column='Max num of 2G act PDP SW', max_length=5, blank=True, null=True)
    maxnum_3g_actpdp_sw = models.CharField(db_column='Max num of 3G act PDPs SW', max_length=5, blank=True, null=True)
    maxnum_4g_bnum_sw = models.CharField(db_column='Max num of 4G Bearer Num SW', max_length=5, blank=True, null=True)
    maxtrans_cap_usr_sw = models.CharField(db_column='Max trans cap of usr plane SW', max_length=10, blank=True, null=True)
    maxnum_234g_subs_hw = models.CharField(db_column='Max num of 2G 3G 4G subs HW', max_length=10, blank=True, null=True)
    maxnum_234g_act_bear_hw = models.CharField(db_column='Max num 2G 3G act 4G Bear HW', max_length=10, blank=True, null=True)
    maxtrans_cap_usr_hw = models.CharField(db_column='Max trans cap of usr plane HW', max_length=10, blank=True, null=True)
    pdp_supt_basic_sw_ggsn = models.CharField(db_column='PDP of Supt Basic SW for GGSN', max_length=10, blank=True, null=True)
    pdp_supt_basic_sw_pgw = models.CharField(db_column='PDP Supt Basic SW for S PGW', max_length=10, blank=True, null=True)
    throughput_ugw_sw = models.CharField(db_column='Throughput of whole UGW SW', max_length=10, blank=True, null=True)
    pdp_supt_basic_hw_ggsn = models.CharField(db_column='PDP Supt Basic HW GGSN S PGW', max_length=5, blank=True, null=True)
    throuhput_ugw_hw = models.CharField(db_column='Throughput of whole UGW HW', max_length=20, blank=True, null=True)
    hw_capacity_sau = models.CharField(db_column='HardwareCapacity(SAU)', max_length=250, blank=True, null=True)
    hw_capacity = models.CharField(db_column='HardwareCapacity', max_length=250, blank=True, null=True)
    hw_capcity_gbps = models.CharField(db_column='HardwareCapacity(Gbps)', max_length=250, blank=True, null=True)
    bearer_sgw = models.CharField(db_column='Bearer Nos of SBSw for S-GW', max_length=5, blank=True, null=True)
    bearer_pgw = models.CharField(db_column='Bearer Nos of SBSw for P-GW ', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'lr_pscoredevice'

class LR_Rnc(models.Model):
    area = models.CharField(db_column='Area', max_length=15, blank=True, null=True)
    rnc_no = models.CharField(db_column='RNC No', max_length=20, blank=True, null=True)
    rnc_location = models.CharField(db_column='RNC LOCATION', max_length=30, blank=True, null=True)
    bandwidtch_cap_lups = models.CharField(db_column='Bandwidth Capacity luPS Provisioned', max_length=10, blank=True, null=True)
    bandwidtch_cap_lucs = models.CharField(db_column='Bandwidth Capacity luCS Provisioned', max_length=5, blank=True, null=True)
    combined_ipbh_cap = models.CharField(db_column='Combined IP BH Capacity', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'lr_rnc'

class LR_RSAGAlarm(models.Model):
    host = models.CharField(db_column='HOST', max_length=10, blank=True, null=True)
    alarm_name = models.CharField(db_column='ALARM NAME', max_length=70, blank=True, null=True)
    network_element = models.CharField(db_column='NETWORK ELEMENT (NE)', max_length=10, blank=True, null=True)
    alarm_category = models.CharField(db_column='ALARM CATEGORY', max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'lr_rsagalarm'

class LR_TDTopology(models.Model):
    aend = models.CharField(db_column='AEND', max_length=30, blank=True, null=True)
    zend = models.CharField(db_column='ZEND', max_length=30, blank=True, null=True)
    domain = models.CharField(db_column='DOMAIN', max_length=20, blank=True, null=True)
    function = models.CharField(db_column='FUNCTION', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lr_tdtopology'

class LR_TRX(models.Model):
    ems_trx_id = models.CharField(db_column='EMS TRX ID', max_length=140, blank=True, null=True)
    ems_id = models.CharField(db_column='EMS ID', max_length=15, blank=True, null=True)
    trx_name = models.CharField(db_column='TRX Name', max_length=140, blank=True, null=True)
    dn = models.CharField(db_column='DN', max_length=140, blank=True, null=True)
    site_id = models.CharField(db_column='Site ID', max_length=10, blank=True, null=True)
    parent_id = models.CharField(db_column='Parent ID', max_length=20, blank=True, null=True)
    parent_dn = models.CharField(db_column='Parent DN', max_length=140, blank=True, null=True)
    admin_state = models.CharField(db_column='Admin State', max_length=15, blank=True, null=True)
    e1_assignment = models.CharField(db_column='E1 Assignment', max_length=10, blank=True, null=True)
    homing_bts = models.CharField(db_column='HOMING BTS', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lr_trx'

class SiteListReport(models.Model):
    site_id = models.CharField(db_column='Site ID', max_length=10, blank=True, null=True)
    parent_site_id = models.CharField(db_column='Parent Site ID', max_length=20, blank=True, null=True)
    site_name = models.CharField(db_column='Site Name', max_length=110, blank=True, null=True)
    latitude = models.CharField(db_column='Latitude', max_length=10, blank=True, null=True)
    longitude = models.CharField(db_column='Logitude', max_length=10, blank=True, null=True)
    site_stage_name = models.CharField(db_column='Site Stage Name', max_length=20, blank=True, null=True)
    site_type_name = models.CharField(db_column='Site Type Name', max_length=20, blank=True, null=True)
    access_restriction = models.CharField(db_column='Access Restriction', max_length=250, blank=True, null=True)
    area_name = models.CharField(db_column='Area Name', max_length=20, blank=True, null=True)
    major_node = models.CharField(db_column='Major Node', max_length=5, blank=True, null=True)
    has_room = models.CharField(db_column='Has Room', max_length=25, blank=True, null=True)
    site_owner = models.CharField(db_column='Site Owner', max_length=250, blank=True, null=True)
    region_name = models.CharField(db_column='Region Name', max_length=10, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)
    ppgis_city_code = models.CharField(db_column='PPGIS City Code', max_length=5, blank=True, null=True)
    province = models.CharField(db_column='Province', max_length=40, blank=True, null=True)
    lessor_name = models.CharField(db_column='Lessor Name', max_length=170, blank=True, null=True)
    lessor_phone = models.CharField(db_column='Lessor Phone', max_length=170, blank=True, null=True)
    altitude_m = models.CharField(db_column='Altitude(m)', max_length=10, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)
    travel_duration = models.CharField(db_column='Travel Duration(m)', max_length=250, blank=True, null=True)
    tower_height = models.CharField(db_column='Tower Height', max_length=30, blank=True, null=True)
    tower_type = models.CharField(db_column='Tower Type', max_length=90, blank=True, null=True)
    mtf = models.CharField(db_column='MTF', max_length=5, blank=True, null=True)
    vip = models.CharField(db_column='VIP', max_length=5, blank=True, null=True)
    malls = models.CharField(db_column='Malls', max_length=5, blank=True, null=True)
    schools = models.CharField(db_column='Schools', max_length=5, blank=True, null=True)
    residentials = models.CharField(db_column='Residentials', max_length=5, blank=True, null=True)
    churches = models.CharField(db_column='Churches', max_length=5, blank=True, null=True)
    hospitals = models.CharField(db_column='Hospitals', max_length=5, blank=True, null=True)
    cemetery = models.CharField(db_column='Cemetery', max_length=5, blank=True, null=True)
    port = models.CharField(db_column='Port', max_length=5, blank=True, null=True)
    intl_airport = models.CharField(db_column='Intl Airport', max_length=5, blank=True, null=True)
    dom_airport = models.CharField(db_column='Dom Airport', max_length=5, blank=True, null=True)
    bus_terminal = models.CharField(db_column='Bus Terminal', max_length=5, blank=True, null=True)
    cbd = models.CharField(db_column='CBD', max_length=5, blank=True, null=True)
    gov = models.CharField(db_column='Government', max_length=5, blank=True, null=True)
    offices = models.CharField(db_column='Offices', max_length=5, blank=True, null=True)
    tourists_spots = models.CharField(db_column='Tourists Spots', max_length=5, blank=True, null=True)
    events_serving_site = models.CharField(db_column='Events Serving Site', max_length=5, blank=True, null=True)
    hotels = models.CharField(db_column='Hotels', max_length=5, blank=True, null=True)
    corp = models.CharField(db_column='Corp', max_length=5, blank=True, null=True)
    pd_rd = models.CharField(db_column='PD/RD', max_length=5, blank=True, null=True)
    mpic_office = models.CharField(db_column='MPIC Offices', max_length=5, blank=True, null=True)
    smart_stores = models.CharField(db_column='Smart Stores', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'sitelistreport'

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
