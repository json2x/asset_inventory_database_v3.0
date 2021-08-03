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
    dn = models.CharField(max_length=250, blank=True, null=True)  # db_column='DN'
    device_id = models.CharField(max_length=250)  # db_column='Device ID'
    ems_device_id = models.CharField(max_length=250, blank=True, null=True)  # db_column='EMS Device ID'
    device_alias = models.CharField(max_length=250, blank=True, null=True)  # db_column='Device Alias'
    device_ip = models.CharField(max_length=50, blank=True, null=True)  # db_column='Device IP'
    ems_id = models.CharField(max_length=50, blank=True, null=True)  # db_column='EMS ID'
    vendor_id = models.CharField(max_length=10, blank=True, null=True)  # db_column='Vendor ID'
    ne_type = models.CharField(max_length=10, blank=True, null=True)  # db_column='NE Type'
    model = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    hardware_description = models.CharField(max_length=50, blank=True, null=True)  # db_column='Hardware Description'
    functional_description = models.CharField(max_length=50, blank=True, null=True)  # db_column='Functional Description'
    parent_device_id = models.CharField(max_length=250, blank=True, null=True)  # db_column='Parent Device ID'
    parentdn = models.CharField(max_length=250, blank=True, null=True)  # db_column='ParentDN'
    site_id = models.CharField(max_length=10, blank=True, null=True)  # db_column='Site ID'
    device_state = models.CharField(max_length=50, blank=True, null=True)  # db_column='Device State'
    software_version = models.CharField(max_length=100, blank=True, null=True)  # db_column='Software Version'
    integration_date = models.CharField( max_length=100, blank=True, null=True)  # db_column='Integration Date
    end_of_support = models.CharField(max_length=100, blank=True, null=True)  # db_column='End of Support'
    tsa_scope = models.CharField(max_length=100, blank=True, null=True)  # db_column='TSA Scope'
    product_id = models.CharField(max_length=100, blank=True, null=True)  # db_column='Product ID'
    serial_number = models.CharField(max_length=100, blank=True, null=True)  # db_column='Serial Number'
    freq_tx_rx_field = models.CharField(max_length=50, blank=True, null=True)  # db_column='FREQ (TX_RX)'
    hardware_capacity = models.CharField(max_length=50, blank=True, null=True)  # db_column='Hardware Capacity'
    domain = models.CharField(max_length=30, blank=True, null=True)  # db_column='Domain'
    ne_owner = models.CharField(max_length=50, blank=True, null=True)  # db_column='NE Owner'
    tx_clusterimg = models.CharField(max_length=100, blank=True, null=True)  # db_column='TX Clusterimg'
    tx_type = models.CharField(max_length=10, blank=True, null=True)  # db_column='TX Type'
    natspcode = models.CharField(max_length=50, blank=True, null=True)  # db_column='NATSPCODE'
    admin_state = models.CharField( max_length=50, blank=True, null=True)  # db_column='Admin State
    subdomain = models.CharField(max_length=50, blank=True, null=True)  # db_column='SUBDOMAIN'
    function = models.CharField(max_length=50, blank=True, null=True)  # db_column='FUNCTION'
    iubce_dl_lic = models.CharField(max_length=10, blank=True, null=True)  # db_column='IUBCE DL LIC'
    iubce_ul_lic = models.CharField(max_length=10, blank=True, null=True)  # db_column='IUBCE UL LIC'
    s1cu_lic = models.CharField(max_length=10, blank=True, null=True)  # db_column='S1CU LIC'
    cluster_region = models.CharField(max_length=50, blank=True, null=True)  # db_column='Cluster Region'
    cluster_sub_region = models.CharField(max_length=50, blank=True, null=True)  # db_column='Cluster Sub Region'
    cluster_province = models.CharField(max_length=50, blank=True, null=True)  # db_column='Cluster Province'
    cluster_city = models.CharField(max_length=50, blank=True, null=True)  # db_column='Cluster City'
    mw_hub = models.CharField(max_length=10, blank=True, null=True)  # db_column='MW HUB'
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
    domain = models.CharField(max_length=10, blank=True, null=True)  # db_column='Domain'
    ems_cell_id = models.CharField(max_length=250, blank=True, null=True)  # db_column='EMS Cell ID'
    ems_id = models.CharField(max_length=50, blank=True, null=True)  # db_column='EMS ID'
    cell_name = models.CharField(max_length=50)  # db_column='Cell Name'
    dn = models.CharField(max_length=250, blank=True, null=True)  # db_column='DN'
    site = models.CharField(max_length=10)  # db_column='Site'
    parent_id = models.CharField( max_length=250)  # db_column='Parent ID
    parent_dn = models.CharField(max_length=250, blank=True, null=True)  # db_column='Parent DN'
    tech = models.CharField(max_length=50, blank=True, null=True)  # db_column='Tech'
    band = models.CharField(max_length=5)  # db_column='Band'
    admin_state = models.CharField(max_length=50, blank=True, null=True)  # db_column='Admin State'
    alias = models.CharField(max_length=50, blank=True, null=True)  # db_column='Alias'
    lac_tac = models.CharField(max_length=10, blank=True, null=True)  # db_column='LAC TAC'
    sac_ci_eutra = models.CharField(max_length=50, blank=True, null=True)  # db_column='SAC CI EUTRA'
    rnc_cid = models.CharField(max_length=10, blank=True, null=True)  # db_column='RNC CID'
    phy_cid = models.CharField(max_length=10, blank=True, null=True)  # db_column='PHY CID'
    lcr_cid = models.CharField(max_length=10, blank=True, null=True)  # db_column='LCR CID
    mcc = models.CharField(max_length=5, blank=True, null=True)  # db_column='MCC'
    mnc = models.CharField(max_length=5, blank=True, null=True)  # db_column='MNC'
    nodeid = models.CharField(max_length=10, blank=True, null=True)  # db_column='NODEID'
    sector_id = models.CharField(max_length=10, blank=True, null=True)  # db_column='SECTOR ID
    carrier = models.CharField(max_length=10, blank=True, null=True)  # db_column='CARRIER
    ne_type = models.CharField(max_length=5, blank=True, null=True)  # db_column='NE TYPE'
    subdomain = models.CharField(max_length=10)  # db_column='SUBDOMAIN
    function = models.CharField(max_length=10, blank=True, null=True)  # db_column='FUNCTION'
    sdcch_cap = models.CharField(max_length=10, blank=True, null=True)  # db_column='SDCCH CAP'
    tch_cap = models.CharField(max_length=10, blank=True, null=True)  # db_column='TCH CAP'
    azimuth = models.CharField(max_length=50, blank=True, null=True)  # db_column='Azimut
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
    area = models.CharField(max_length=5, blank=True, null=True) # db_column='DN',
    site_id = models.CharField(max_length=5, blank=True, null=True) # db_column='Site ID',
    exact_date = models.CharField(max_length=5, blank=True, null=True) # db_column='Exact Date',
    day_of_month = models.CharField(max_length=10, blank=True, null=True) # db_column='Day of Month',
    day_of_week = models.CharField(max_length=10, blank=True, null=True) # db_column='Day of Week',
    start_time = models.CharField(max_length=5, blank=True, null=True) # db_column='Start Time',
    end_time = models.CharField(max_length=5, blank=True, null=True) # db_column='End Time',
    restricted_time = models.CharField(max_length=10, blank=True, null=True) # db_column='Restricted Time',
    site_name = models.CharField(max_length=80, blank=True, null=True) # db_column='Site Name',

    class Meta:
        db_table = 'accessconstraint'

class LR_3G_IMA_GRP(models.Model):
    ems_id = models.CharField(max_length=10, blank=True, null=True) # db_column='EMS_ID'
    idnum = models.CharField(max_length=130, blank=True, null=True) # db_column='IDNUM
    dn = models.CharField(max_length=130, blank=True, null=True) # db_column='DN'
    parent_id = models.CharField(max_length=20, blank=True, null=True) # db_column='Parent ID'
    parent_dn = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent DN'

    class Meta:
        db_table = 'lr_3g_ima_grp'

class LR_3G_IMA_LNK(models.Model):
    ems_id = models.CharField(max_length=10, blank=True, null=True) # db_column='EMS_ID'
    idnum = models.CharField(max_length=140, blank=True, null=True) # db_column='IDNUM'
    dn = models.CharField(max_length=140, blank=True, null=True) # db_column='DN'
    parent_id = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent ID'
    parent_dn = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent DN'

    class Meta:
        #managed = False
        db_table = 'lr_3g_ima_lnk'

class LRBandwidth(models.Model):
    device_id = models.CharField(max_length=60, blank=True, null=True) # db_column='Device ID'
    bandwidth = models.CharField(max_length=15, blank=True, null=True) # db_column= 'Bandwidth'
    tech = models.CharField(max_length=20, blank=True, null=True) # db_column='Tech'

    class Meta:
        db_table = 'lr_bandwidth'

class LRBSC(models.Model):
    area = models.CharField(max_length=20, blank=True, null=True) # db_column='Area'
    bsc_no = models.CharField(max_length=20, blank=True, null=True) # db_column='BSC No'
    bsc_loc = models.CharField(max_length=30, blank=True, null=True) # db_column='BSC LOCATION'
    ao_ipbh_cap = models.CharField(max_length=5, blank=True, null=True) # db_column='AO IP BH Capacity'
    sig_bh_cap = models.CharField(max_length=250, blank=True, null=True) # db_column='SIGTRAN BH Capacity'
    gbo_ipbh_cap = models.CharField(max_length=5, blank=True, null=True) # db_column='GBO IP BH Capacity'
    combined_ipbh = models.CharField(max_length=5, blank=True, null=True) # db_column='COMBINED IP BH Capacity'

    class Meta:
        db_table = 'lrbsc'

class LRBSC_RNC(models.Model):
    ne_name = models.CharField(max_length=10, blank=True, null=True) # db_column='NE NAME'
    msc_poolname = models.CharField(max_length=250, blank=True, null=True) # db_column='MSC POOL NAME'
    msc_name = models.CharField(max_length=5, blank=True, null=True) # db_column='MSC NAME'
    spc_name = models.CharField(max_length=10, blank=True, null=True) # db_column='SPC NAME'
    int_net_code = models.CharField(max_length=250, blank=True, null=True) # db_column='INT NET CODE'
    int_spnet_code = models.CharField(max_length=250, blank=True, null=True) # db_column='INT SP NET CODE'
    nat_code = models.CharField(max_length=250, blank=True, null=True) # db_column='NAT CODE'
    nat_sp_code = models.CharField(max_length=10, blank=True, null=True) # db_column='NAT SP CODE'
    sgsn_name = models.CharField(max_length=250, blank=True, null=True) # db_column='SGSN NAME'
    sgsn_pool_name = models.CharField(max_length=250, blank=True, null=True) # db_column='SGSN POOL NAME'
    ne_index = models.CharField(max_length=5, blank=True, null=True) # db_column='NE INDEX'
    type = models.CharField(max_length=5, blank=True, null=True) # db_column='TYPE'
    netid = models.CharField(max_length=250, blank=True, null=True) # db_column='NET ID'

    class Meta:
        db_table = 'lrbsc_rnc'

class LRCEMDEV(models.Model):
    dn = models.CharField(max_length=20, blank=True, null=True) # db_column='DN'
    ne_type = models.CharField(max_length=5, blank=True, null=True) # db_column='NE TYPE'
    home_msc_pool = models.CharField(max_length=10, blank=True, null=True) # db_column='Home MSC Pool'
    gt_address = models.CharField(max_length=20, blank=True, null=True) # db_column='Gt Address'
    msc_server_type = models.CharField(max_length=5, blank=True, null=True) # db_column='MSC Server Type'
    carrier = models.CharField(max_length=5, blank=True, null=True) # db_column ='Carrier'
    country = models.CharField(max_length=20, blank=True, null=True) # db_column='Country'
    spc_name = models.CharField(max_length=10, blank=True, null=True) # db_column='SPC Name'
    int_net_code = models.CharField(max_length=5, blank=True, null=True) # db_column='International Network Code'
    int_spnet = models.CharField(max_length=5, blank=True, null=True) # db_column='International Spare Network'
    nat_net_code = models.CharField(max_length=5, blank=True, null=True) # db_column='National Network Code'
    nat_spnet_code = models.CharField(max_length=5, blank=True, null=True) # db_column='National Spare Network Code'
    bcu = models.CharField(max_length=5, blank=True, null=True) # db_column='BCU'
    homing_msc = models.CharField(max_length=15, blank=True, null=True) # db_column='Homing Msc'

    class Meta:
        db_table = 'lrcemdev'

class LRCEMIP(models.Model):
    dn = models.CharField(max_length=20, blank=True, null=True) # db_column='DN'
    ne_type = models.CharField(max_length=5, blank=True, null=True) # db_column='NE Type'
    ip_add = models.CharField(max_length=15, blank=True, null=True) # db_column='IP Address'
    type = models.CharField(max_length=5, blank=True, null=True) # db_column='Type'

    class Meta:
        db_table = 'lrcemip'

class LRCEMNRI(models.Model):
    dn = models.CharField(max_length=20, blank=True, null=True) # db_column='DN'
    nri = models.CharField(max_length=5, blank=True, null=True) # db_column='NRI'

    class Meta:
        db_table = 'lrcemnri'

class LR_CSPGCTRL(models.Model):
    pg_pol = models.CharField(max_length=5, blank=True, null=True) # db_column='PG POL'
    msc_spc = models.CharField(max_length=10, blank=True, null=True) # db_column='MSC SPC'
    lai = models.CharField(max_length=10, blank=True, null=True) # db_column='LAI'
    pg_type = models.CharField(max_length=20, blank=True, null=True) # db_column='PG TYPE'
    pg_times = models.CharField(max_length=5, blank=True, null=True) # db_column='PG TIMES'
    pg1_durh = models.CharField(max_length=5, blank=True, null=True) # db_column='PG1 DURH'
    pg1_idt = models.CharField(max_length=5, blank=True, null=True) # db_column='PG1 IDT'
    pg2_durh = models.CharField(max_length=5, blank=True, null=True) # db_column='PG2 DURH'
    pg2_idt = models.CharField(max_length=5, blank=True, null=True) # db_column='PG2 IDT'
    pg3_durh = models.CharField(max_length=5, blank=True, null=True) # db_column='PG3 DURH'
    lpg3_idtai = models.CharField(max_length=5, blank=True, null=True) # db_column='LPG3 IDTAI'
    pg4_durh = models.CharField(max_length=5, blank=True, null=True) # db_column='PG4 DURH'
    pg4_idt = models.CharField(max_length=5, blank=True, null=True) # db_column='PG4 IDT'
    pg5_durh = models.CharField(max_length=5, blank=True, null=True) # db_column='PG5 DURH'
    pg5_idt = models.CharField(max_length=5, blank=True, null=True) # db_column='PG5 IDT'

    class Meta:
        db_table = 'lr_cspgctrl'

class LR_ENODEB(models.Model):
    ne_id = models.CharField(max_length=10, blank=True, null=True) # db_column=' NE ID'
    ne_name = models.CharField(max_length=30, blank=True, null=True) # db_column='NE NAME'
    cpia = models.CharField(max_length=20, blank=True, null=True) # db_column='CPIA'
    upia = models.CharField(max_length=20, blank=True, null=True) # db_column='UPIA'
    mme_name = models.CharField(max_length=250, blank=True, null=True) # db_column='MME NAME'
    mcc = models.CharField(max_length=5, blank=True, null=True) # db_column='MCC'
    mnc = models.CharField(max_length=5, blank=True, null=True) # db_column='MNC'
    mme_pname = models.CharField(max_length=250, blank=True, null=True) # db_column='MME POOL NAME'

    class Meta:
        db_table = 'lr_enodeb'

class LR_ERDIP(models.Model):
    bsc_id = models.CharField(max_length=10, blank=True, null=True) #d b_column='BSC.ID'
    rbl_id = models.CharField(max_length=5, blank=True, null=True) # db_column='RBL.ID'
    tg_id = models.CharField(max_length=10, blank=True, null=True) # db_column='TG.ID
    device_id = models.CharField(max_length=20, blank=True, null=True) # db_column='DEVICE.ID'

    class Meta:
        db_table = 'lr_erdip'

class LR_IP_POOLINV(models.Model):
    device_id = models.CharField(max_length=20, blank=True, null=True) # db_column='DEVICE ID'
    apn = models.CharField(max_length=50, blank=True, null=True) # db_column='APN'
    ip_pname = models.CharField(max_length=30, blank=True, null=True) # db_column='IP POOL NAME'
    cidr = models.CharField(max_length=20, blank=True, null=True) # db_column='CIDR'
    iprange = models.CharField(max_length=60, blank=True, null=True) # db_column='IPRANGE'
    totalips = models.CharField(max_length=5, blank=True, null=True) # db_column='TOTALIPS'
    usableips = models.CharField(max_length=5, blank=True, null=True) # db_column='USABLEIPS'
    remarks = models.CharField(max_length=250, blank=True, null=True) # db_column='REMARKS'

    class Meta:
        db_table = 'lr_ip_polinv'

class LR_LINK(models.Model):
    idnum = models.CharField(max_length=5, blank=True, null=True) # db_column='IDNUM'
    create_date = models.CharField(max_length=250, blank=True, null=True) # db_column='Create Date'
    dn = models.CharField(max_length=250, blank=True, null=True) # db_column='DN'
    name = models.CharField(max_length=250, blank=True, null=True) # db_column='Name'
    update_date = models.CharField(max_length=250, blank=True, null=True) # db_column='Update Date'
    link_type = models.CharField(max_length=10, blank=True, null=True) # db_column='Link Type'
    aend_node = models.CharField(max_length=70, blank=True, null=True) # db_column='AEND Node'
    aend_tp = models.CharField(max_length=60, blank=True, null=True) # db_column='AEND TP'
    add_info = models.CharField(max_length=250, blank=True, null=True) # db_column='Additional Info'
    aend_ip = models.CharField(max_length=20, blank=True, null=True) # db_column='AEND IP'
    service = models.CharField(max_length=20, blank=True, null=True) # db_column='Service'
    direction = models.CharField(max_length=5, blank=True, null=True) # db_column='Direction-'
    ems_name = models.CharField(max_length=30, blank=True, null=True) # db_column='EMS Name'
    native_ems_name = models.CharField(max_length=15, blank=True, null=True) # db_column='Native EMS Name'
    owner = models.CharField(max_length=5, blank=True, null=True) # db_column='Owner'
    parent_dn = models.CharField(max_length=250, blank=True, null=True) # db_column='Parent DN'
    rate = models.CharField(max_length=20, blank=True, null=True) # db_column='Rate'
    usr_label = models.CharField(max_length=150, blank=True, null=True) #d b_column='User Label'
    zend_node = models.CharField(max_length=70, blank=True, null=True) # db_column='ZEND Node'
    zend_tp = models.CharField(max_length=80, blank=True, null=True) # db_column='ZEND TP'
    zend_ip = models.CharField(max_length=20, blank=True, null=True) # db_column='ZEND IP'
    date_res_id = models.CharField(max_length=250, blank=True, null=True) # db_column='Date Resource ID'
    domain = models.CharField(max_length=20, blank=True, null=True) # db_column='Domain'

    class Meta:
        db_table = 'lr_link'

class LR_LTunnel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True) # db_column='NAME'
    linktype = models.CharField(max_length=10, blank=True, null=True) # db_column='LINK TYPE'
    capacity = models.CharField(max_length=250, blank=True, null=True) # db_column='CAPACITY'
    tunnel_id = models.CharField(max_length=15, blank=True, null=True) # db_column='TUNNEL ID'
    tunnel_bandwidth = models.CharField(max_length=250, blank=True, null=True) # db_column='TUNNEL BANDWIDTH'
    aendnode_sitecodes = models.CharField(max_length=5, blank=True, null=True) # db_column='AENDNODE SITECODES'
    aend_node = models.CharField(max_length=20, blank=True, null=True) # db_column='AENDNODE'
    aend_tp = models.CharField(max_length=35, blank=True, null=True) # db_column='AEND TP'
    aend_tp_child = models.CharField(max_length=250, blank=True, null=True) # db_column='AEND TP (CHILD)'
    aend_ip = models.CharField(max_length=250, blank=True, null=True) # db_column='AEND IP'
    aend_eq = models.CharField(max_length=10, blank=True, null=True) # db_column='AEND EQUIPMENT'
    zend_nodes_sitecodes = models.CharField(max_length=5, blank=True, null=True) # db_column='ZENDNODE SITECODES'
    zend_node = models.CharField(max_length=20, blank=True, null=True) # db_column='ZENDNODE'
    zend_tp = models.CharField(max_length=35, blank=True, null=True) # db_column='ZEND TP'
    zend_tp_child = models.CharField(max_length=250, blank=True, null=True) # db_column='ZEND TP (CHILD)'
    zend_ip = models.CharField(max_length=250, blank=True, null=True) # db_column='ZEND IP'
    zend_eq = models.CharField(max_length=10, blank=True, null=True) # db_column='ZEND EQUIPMENT'
    description = models.CharField(max_length=30, blank=True, null=True) # db_column='DESCRIPTION'
    domain = models.CharField(max_length=250, blank=True, null=True) # db_column='DOMAIN'
    cluster = models.CharField(max_length=250, blank=True, null=True) # db_column='CLUSTER'
    cao_wo = models.CharField(max_length=250, blank=True, null=True) # db_column='CAO/WO'
    band_service = models.CharField(max_length=250, blank=True, null=True) # db_column='BAND/SERVICE'
    direction = models.CharField(max_length=250, blank=True, null=True) # db_column='DIRECTION'
    remarks = models.CharField(max_length=60, blank=True, null=True) # db_column='REMARKS'
    rnc_bsc = models.CharField(max_length=10, blank=True, null=True) # db_column='RNC/BSC

    class Meta:
        db_table = 'lr_ltunnel'

class LR_NBINT(models.Model):
    domain = models.CharField(max_length=20, blank=True, null=True) # db_column='Domain'
    ems_id = models.CharField(max_length=20, blank=True, null=True) # db_column='EMS ID'
    parent_id = models.CharField(max_length=40, blank=True, null=True) # db_column='Parent ID'
    lip_1 = models.CharField(max_length=20, blank=True, null=True) # db_column='LIP 1'
    lip_2 = models.CharField(max_length=40, blank=True, null=True) # db_column='LIP 2'
    own_spc = models.CharField(max_length=20, blank=True, null=True) # db_column='Own SPC'
    assoc_set_id = models.CharField(max_length=20, blank=True, null=True) # db_column='Assoc Set ID'
    assoc_set_name = models.CharField(max_length=40, blank=True, null=True) # db_column='Assoc Set Name'
    assoc_index = models.CharField(max_length=40, blank=True, null=True) # db_column='Assoc Index'
    rip_1 = models.CharField(max_length=30, blank=True, null=True) # db_column='RIP 1'
    rip_2 = models.CharField(max_length=50, blank=True, null=True) # db_column='RIP 2'
    use = models.CharField(max_length=30, blank=True, null=True) # db_column='USE'
    class_nbint = models.CharField(max_length=20, blank=True, null=True) # db_column='Class'
    assoc_name = models.CharField(max_length=50, blank=True, null=True) # db_column='ASSOC NAME'
    local_port = models.CharField(max_length=10, blank=True, null=True) # db_column='LOCAL PORT'
    peer_port = models.CharField(max_length=10, blank=True, null=True) # db_column='PEER PORT'
    deno = models.CharField(max_length=10, blank=True, null=True) # db_column='DENO'
    deno_name = models.CharField(max_length=40, blank=True, null=True) # db_column='DENO NAME'
    leno = models.CharField(max_length=5, blank=True, null=True) # db_column='LENO'
    leno_name = models.CharField(max_length=40, blank=True, null=True) # db_column='LENO NAME'
    peer_device_id = models.CharField(max_length=20, blank=True, null=True) # db_column='PEER DEVICE ID'
    peer_spc = models.CharField(max_length=10, blank=True, null=True) # db_column='PEER SPC'
    peer_nsei = models.CharField(max_length=250, blank=True, null=True) # db_column='PEER A SET ID NSEI'
    peer_assoc_set = models.CharField(max_length=250, blank=True, null=True) # db_column='PEER ASSOC SET NAME'
    name = models.CharField(max_length=250, blank=True, null=True) # db_column='Name'
    peer_assoc_index = models.CharField(max_length=250, blank=True, null=True) # db_column='PEER ASSOC INDEX'
    peer_assoc_name = models.CharField(max_length=250, blank=True, null=True) # db_column='PEER ASSOC NAME'

    class Meta:
        db_table = 'lr_nbint'

class LR_PCCapacity(models.Model):
    idnum = models.CharField(max_length=20, blank=True, null=True) # db_column='IDNUM'
    device_id = models.CharField(max_length=30, blank=True, null=True) # db_column='Device ID'
    name = models.CharField(max_length=20, blank=True, null=True) # db_column='Name'
    vendor = models.CharField(max_length=10, blank=True, null=True) # db_column='Vendor'
    area_served = models.CharField(max_length=10, blank=True, null=True) # db_column='Area Served'
    sw_release = models.CharField(max_length=20, blank=True, null=True) # db_column='SW Reease'
    hw_capacity_sau = models.CharField(max_length=10, blank=True, null=True) # db_column='HW Capacity (SAU)'
    hw_capacity_pdp = models.CharField(max_length=250, blank=True, null=True) # db_column='HW Capacity (PDP)'
    sw_capacity_sau = models.CharField(max_length=250, blank=True, null=True) # db_column='SW Capacity (SAU)
    sw_capacity_pdp = models.CharField(max_length=250, blank=True, null=True) # db_column='SW Capacity (PDP)'
    hw_capacity_tput = models.CharField(max_length=10, blank=True, null=True) # db_column='HW Capacity (TPUT)'
    hw_capacity_pdp1 = models.CharField(max_length=250, blank=True, null=True) # db_column='HW Capacity (PDP)1'
    purchasedsw_capacity_tput = models.CharField(max_length=250, blank=True, null=True) # db_column='PurchasedSW (TPUT)'
    purchasedsw_pdp = models.CharField(max_length=10, blank=True, null=True) # db_column='PurchasedSW (PDP)'
    ecu_sau = models.CharField(max_length=10, blank=True, null=True) # db_column='ECU (SAU)'
    epu_pdp = models.CharField(max_length=10, blank=True, null=True) # db_column='EPU (PDP)'
    ecu = models.CharField(max_length=5, blank=True, null=True) # db_column='ECU'
    epu = models.CharField(max_length=5, blank=True, null=True) # db_column='EPU'
    redunduncy_model = models.CharField(max_length=5, blank=True, null=True) # db_column='Redunduncy Model'
    no_of_subrack = models.CharField(max_length=5, blank=True, null=True) # db_column='No Of SubRack'
    gsc = models.CharField(max_length=5, blank=True, null=True) # db_column='GSC'
    active_cpb = models.CharField(max_length=5, blank=True, null=True) # db_column='Active CPB'
    standyby_cpb = models.CharField(max_length=5, blank=True, null=True) # db_column='Standby CPB'
    active_ppb = models.CharField(max_length=5, blank=True, null=True) # db_column='Active PPB'
    standby_ppb = models.CharField(max_length=5, blank=True, null=True) # db_column='Standby PPB'
    lc = models.CharField(max_length=5, blank=True, null=True) # db_column='LC'
    tput = models.CharField(max_length=5, blank=True, null=True) # db_column='TPUT'
    board_type = models.CharField(max_length=5, blank=True, null=True) # db_column='Board Type'
    no_of_boards = models.CharField(max_length=5, blank=True, null=True) # db_column='No Of Boards'
    sw_capacity = models.CharField(max_length=10, blank=True, null=True) # db_column='SW Capacity'
    chasis_type = models.CharField(max_length=20, blank=True, null=True) # db_column='Chasis Type'
    blade_type = models.CharField(max_length=5, blank=True, null=True) # db_column='Blade Type'
    blade_capacity = models.CharField(max_length=10, blank=True, null=True) # db_column='Blade Capacity'
    total_no_of_blades = models.CharField(max_length=5, blank=True, null=True) # db_column='Total Number of Blades'

    class Meta:
        db_table = 'lr_pccapacity'

class LR_Parked(models.Model):
    site_no = models.CharField(max_length=10, blank=True, null=True) # db_column='SITENO'
    band = models.CharField(max_length=10, blank=True, null=True) # db_column='BAND'
    tech = models.CharField(max_length=10, blank=True, null=True) # db_column='TECH'

    class Meta:
        db_table = 'lr_parked'

class LR_PSCoreDevice(models.Model):
    dn = models.CharField(max_length=15, blank=True, null=True) # db_column='DN'
    device_id = models.CharField(max_length=15, blank=True, null=True) # db_column='Device ID'
    ems_id = models.CharField(max_length=20, blank=True, null=True)  #db_column='EMS ID'
    vendor_id = models.CharField(max_length=5, blank=True, null=True) # db_column='VendorID'
    ne_type = models.CharField(max_length=5, blank=True, null=True) # db_column='NE Type'
    site_id = models.CharField(max_length=10, blank=True, null=True) # db_column='Site ID'
    sau_license_sw = models.CharField(max_length=10, blank=True, null=True) # db_column='SAU License SW'
    sau_hw = models.CharField(max_length=10, blank=True, null=True) # db_column='SAU HW'
    pdp_license_sw = models.CharField(max_length=10, blank=True, null=True) # db_column='PDP License SW'
    th_license_sw = models.CharField(max_length=10, blank=True, null=True) # db_column='Throughput License SW'
    th_hw_gbps = models.CharField(max_length=5, blank=True, null=True) # db_column='Throughput HW(Gbps)'
    maxnum_2g_subs_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 2G subs SW'
    maxnum_3g_subs_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 3G subs SW'
    maxnum_4g_subs_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 4G subs SW'
    maxnum_2g_actpdp_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 2G act PDP SW'
    maxnum_3g_actpdp_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 3G act PDPs SW'
    maxnum_4g_bnum_sw = models.CharField(max_length=5, blank=True, null=True) # db_column='Max num of 4G Bearer Num SW'
    maxtrans_cap_usr_sw = models.CharField(max_length=10, blank=True, null=True) # db_column='Max trans cap of usr plane SW'
    maxnum_234g_subs_hw = models.CharField(max_length=10, blank=True, null=True)  #db_column='Max num of 2G 3G 4G subs HW'
    maxnum_234g_act_bear_hw = models.CharField(max_length=10, blank=True, null=True) # db_column='Max num 2G 3G act 4G Bear HW'
    maxtrans_cap_usr_hw = models.CharField(max_length=10, blank=True, null=True) # db_column='Max trans cap of usr plane HW
    pdp_supt_basic_sw_ggsn = models.CharField(max_length=10, blank=True, null=True) # db_column='PDP of Supt Basic SW for GGSN'
    pdp_supt_basic_sw_pgw = models.CharField(max_length=10, blank=True, null=True) # db_column='PDP Supt Basic SW for S PGW'
    throughput_ugw_sw = models.CharField(max_length=10, blank=True, null=True) # db_column='Throughput of whole UGW SW'
    pdp_supt_basic_hw_ggsn = models.CharField(max_length=5, blank=True, null=True) # db_column='PDP Supt Basic HW GGSN S PGW'
    throuhput_ugw_hw = models.CharField(max_length=20, blank=True, null=True) # db_column='Throughput of whole UGW HW'
    hw_capacity_sau = models.CharField(max_length=250, blank=True, null=True) # db_column='HardwareCapacity(SAU)'
    hw_capacity = models.CharField(max_length=250, blank=True, null=True) # db_column='HardwareCapacity'
    hw_capcity_gbps = models.CharField(max_length=250, blank=True, null=True) # db_column='HardwareCapacity(Gbps)'
    bearer_sgw = models.CharField(max_length=5, blank=True, null=True) # db_column='Bearer Nos of SBSw for S-GW'
    bearer_pgw = models.CharField(max_length=5, blank=True, null=True) # db_column='Bearer Nos of SBSw for P-GW '

    class Meta:
        db_table = 'lr_pscoredevice'

class LR_Rnc(models.Model):
    area = models.CharField(max_length=15, blank=True, null=True) # db_column='Area'
    rnc_no = models.CharField(max_length=20, blank=True, null=True) # db_column='RNC No'
    rnc_location = models.CharField(max_length=30, blank=True, null=True) # db_column='RNC LOCATION'
    bandwidtch_cap_lups = models.CharField(max_length=10, blank=True, null=True) # db_column='Bandwidth Capacity luPS Provisioned'
    bandwidtch_cap_lucs = models.CharField(max_length=5, blank=True, null=True) # db_column='Bandwidth Capacity luCS Provisioned'
    combined_ipbh_cap = models.CharField(max_length=10, blank=True, null=True) # db_column='Combined IP BH Capacity'

    class Meta:
        db_table = 'lr_rnc'

class LR_RSAGAlarm(models.Model):
    host = models.CharField(max_length=10, blank=True, null=True) # db_column='HOST'
    alarm_name = models.CharField(max_length=70, blank=True, null=True) # db_column='ALARM NAME'
    network_element = models.CharField(max_length=10, blank=True, null=True) # db_column='NETWORK ELEMENT (NE)'
    alarm_category = models.CharField(max_length=15, blank=True, null=True) # db_column='ALARM CATEGORY'

    class Meta:
        db_table = 'lr_rsagalarm'

class LR_TDTopology(models.Model):
    aend = models.CharField(max_length=30, blank=True, null=True) # db_column='AEND'
    zend = models.CharField(max_length=30, blank=True, null=True) # db_column='ZEND'
    domain = models.CharField(max_length=20, blank=True, null=True) # db_column='DOMAIN'
    function = models.CharField(max_length=20, blank=True, null=True) # db_column='FUNCTION'

    class Meta:
        db_table = 'lr_tdtopology'

class LR_TRX(models.Model):
    ems_trx_id = models.CharField(max_length=140, blank=True, null=True) # db_column='EMS TRX ID'
    ems_id = models.CharField(max_length=15, blank=True, null=True) # db_column='EMS ID'
    trx_name = models.CharField(max_length=140, blank=True, null=True) # db_column='TRX Name'
    dn = models.CharField(max_length=140, blank=True, null=True) # db_column='DN'
    site_id = models.CharField(max_length=10, blank=True, null=True) # db_column='Site ID'
    parent_id = models.CharField(max_length=20, blank=True, null=True) # db_column='Parent ID'
    parent_dn = models.CharField(max_length=140, blank=True, null=True) # db_column='Parent DN'
    admin_state = models.CharField(max_length=15, blank=True, null=True) # db_column='Admin State'
    e1_assignment = models.CharField(max_length=10, blank=True, null=True) # db_column='E1 Assignment'
    homing_bts = models.CharField(max_length=20, blank=True, null=True) # db_column='HOMING BTS'

    class Meta:
        db_table = 'lr_trx'

class SiteListReport(models.Model):
    site_id = models.CharField(max_length=10, blank=True, null=True)  #db_column='Site ID'
    parent_site_id = models.CharField(max_length=20, blank=True, null=True) # db_column='Parent Site ID'
    site_name = models.CharField(max_length=110, blank=True, null=True) # db_column='Site Name'
    latitude = models.CharField(max_length=10, blank=True, null=True) # db_column='Latitude'
    longitude = models.CharField(max_length=10, blank=True, null=True) # db_column='Logitude'
    site_stage_name = models.CharField(max_length=20, blank=True, null=True) # db_column='Site Stage Name'
    site_type_name = models.CharField(max_length=20, blank=True, null=True) # db_column='Site Type Name'
    access_restriction = models.CharField(max_length=250, blank=True, null=True) #db_column='Access Restriction'
    area_name = models.CharField(max_length=20, blank=True, null=True) # db_column='Area Name'
    major_node = models.CharField(max_length=5, blank=True, null=True) # db_column='Major Node'
    has_room = models.CharField(max_length=25, blank=True, null=True) # db_column='Has Room'
    site_owner = models.CharField(max_length=250, blank=True, null=True) # db_column='Site Owner'
    region_name = models.CharField(max_length=10, blank=True, null=True) # db_column='Region Name'
    city = models.CharField(max_length=50, blank=True, null=True) # db_column='City'
    ppgis_city_code = models.CharField(max_length=5, blank=True, null=True) # db_column='PPGIS City Code'
    province = models.CharField(max_length=40, blank=True, null=True) # db_column='Province'
    lessor_name = models.CharField(max_length=170, blank=True, null=True) # db_column='Lessor Name'
    lessor_phone = models.CharField(max_length=170, blank=True, null=True) # db_column='Lessor Phone'
    altitude_m = models.CharField(max_length=10, blank=True, null=True) # db_column='Altitude(m)'
    address = models.CharField(max_length=250, blank=True, null=True) # db_column='Address'
    travel_duration = models.CharField(max_length=250, blank=True, null=True) #d b_column='Travel Duration(m)'
    tower_height = models.CharField(max_length=30, blank=True, null=True) # db_column='Tower Height'
    tower_type = models.CharField(max_length=90, blank=True, null=True) # db_column='Tower Type'
    mtf = models.CharField(max_length=5, blank=True, null=True) # db_column='MTF'
    vip = models.CharField(max_length=5, blank=True, null=True) # db_column='VIP'
    malls = models.CharField(max_length=5, blank=True, null=True) # db_column='Malls'
    schools = models.CharField(max_length=5, blank=True, null=True) # db_column='Schools'
    residentials = models.CharField(max_length=5, blank=True, null=True) # db_column='Residentials'
    churches = models.CharField(max_length=5, blank=True, null=True) # db_column='Churches'
    hospitals = models.CharField(max_length=5, blank=True, null=True) # db_column='Hospitals'
    cemetery = models.CharField(max_length=5, blank=True, null=True) # db_column='Cemetery'
    port = models.CharField(max_length=5, blank=True, null=True) # db_column='Port'
    intl_airport = models.CharField(max_length=5, blank=True, null=True) # db_column='Intl Airport'
    dom_airport = models.CharField(max_length=5, blank=True, null=True) # db_column='Dom Airport'
    bus_terminal = models.CharField(max_length=5, blank=True, null=True) # db_column='Bus Terminal'
    cbd = models.CharField(max_length=5, blank=True, null=True) # db_column='CBD'
    gov = models.CharField(max_length=5, blank=True, null=True) # db_column='Government'
    offices = models.CharField(max_length=5, blank=True, null=True) # db_column='Offices'
    tourists_spots = models.CharField(max_length=5, blank=True, null=True) # db_column='Tourists Spots'
    events_serving_site = models.CharField(max_length=5, blank=True, null=True) # db_column='Events Serving Site'
    hotels = models.CharField(max_length=5, blank=True, null=True) # db_column='Hotels'
    corp = models.CharField(max_length=5, blank=True, null=True) # db_column='Corp'
    pd_rd = models.CharField(max_length=5, blank=True, null=True) # db_column='PD/RD'
    mpic_office = models.CharField(max_length=5, blank=True, null=True) # db_column='MPIC Offices'
    smart_stores = models.CharField(max_length=5, blank=True, null=True) # db_column='Smart Stores'

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
