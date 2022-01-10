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

#User = get_user_model()

#[ DONE ]
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

'''
vlr_capacity = models.CharField(max_length=250, blank=True, null=True)v
simultaneous_pdp = models.CharField(max_length=250, blank=True, null=True)
radius_km = models.CharField(max_length=250, blank=True, null=True)
device_ipv6_address = models.CharField(max_length=250, blank=True, null=True)
org = models.CharField(max_length=250, blank=True, null=True)
cluster_region = models.CharField(max_length=250, blank=True, null=True)
cluster_sub region = models.CharField(max_length=250, blank=True, null=True)
cluster_province = models.CharField(max_length=250, blank=True, null=True)
cluster_city = models.CharField(max_length=250, blank=True, null=True)
mw_hub = models.CharField(max_length=250, blank=True, null=True)
longitude = models.CharField(max_length=250, blank=True, null=True)
latitude = models.CharField(max_length=250, blank=True, null=True)

sau_license = radius_km = models.CharField(max_length=250, blank=True, null=True)
unpacking = models.CharField(max_length=250, blank=True, null=True)
device_state = models.CharField(max_length=250, blank=True, null=True)
version = models.CharField(max_length=250, blank=True, null=True)
device_level_label = models.CharField(max_length=250, blank=True, null=True)
maintenance_personnel = models.CharField(max_length=250, blank=True, null=True)
source = models.CharField(max_length=250, blank=True, null=True)
is_hub = models.CharField(max_length=250, blank=True, null=True)
is_vip = models.CharField(max_length=250, blank=True, null=True)
site_state = models.CharField(max_length=250, blank=True, null=True)
cabinet_type = models.CharField(max_length=250, blank=True, null=True)
int_date2 = models.CharField(max_length=250, blank=True, null=True)
license_expired_from = models.CharField(max_length=250, blank=True, null=True)
acceptance_date = models.CharField(max_length=250, blank=True, null=True)
rack_type = models.CharField(max_length=250, blank=True, null=True)
business_case = models.CharField(max_length=250, blank=True, null=True)
asset_number = models.CharField(max_length=250, blank=True, null=True)
brand = models.CharField(max_length=250, blank=True, null=True)
device_position = models.CharField(max_length=250, blank=True, null=True)
capacity = models.CharField(max_length=250, blank=True, null=True)
old_id = models.CharField(max_length=250, blank=True, null=True)
igwb_software = models.CharField(max_length=250, blank=True, null=True)
hardware_lifecycle = models.CharField(max_length=250, blank=True, null=True)
ethernet_switch = models.CharField(max_length=250, blank=True, null=True)
functional_location = models.CharField(max_length=250, blank=True, null=True)
gn_throughput_license = models.CharField(max_length=250, blank=True, null=True)
payload_license = models.CharField(max_length=250, blank=True, null=True)
pool = models.CharField(max_length=250, blank=True, null=True)
project_definition = models.CharField(max_length=250, blank=True, null=True)
s1_lub_capacity
ce_cu capacity
cap_key_s1_traffic
cap_key_cu
ericsson_microwave_sl_cap
'''
    def __str__(self):
        return self.device_id

    @property
    def cells(self):
        return self.cell_set.all()

    @property
    def has_invalid_chars_in_device_name(self):
        device_name = self.device_id
        return not device_name.isalnum()


#[ DONE ]
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

    '''
    additional fields
    bcc = models.CharField(max_length=250, blank=True, null=True)
    bspwr = models.CharField(max_length=250, blank=True, null=True)
    bspwrb = models.CharField(max_length=250, blank=True, null=True)
    bspwrt = models.CharField(max_length=250, blank=True, null=True)
    bstxpwr = models.CharField(max_length=250, blank=True, null=True)
    cell_active_state = models.CharField(max_length=250, blank=True, null=True)
    cell_admin_state = models.CharField(max_length=250, blank=True, null=True)
    cell_id = models.CharField(max_length=250, blank=True, null=True)
    cell_index = models.CharField(max_length=250, blank=True, null=True)
    configured_maxtxpower = models.CharField(max_length=250, blank=True, null=True)
    crs_gain = models.CharField(max_length=250, blank=True, null=True)
    downlink_bandwidth = models.CharField(max_length=250, blank=True, null=True)
    downlink_earfcn = models.CharField(max_length=250, blank=True, null=True)
    local_cell_id = models.CharField(max_length=250, blank=True, null=True)
    max_transmission_power = models.CharField(max_length=250, blank=True, null=True)
    mbcch = models.CharField(max_length=250, blank=True, null=True)
    mimo = models.CharField(max_length=250, blank=True, null=True)
    ncc = models.CharField(max_length=250, blank=True, null=True)
    pa_for_even_power_distribution = models.CharField(max_length=250, blank=True, null=True)
    pb = models.CharField(max_length=250, blank=True, null=True)
    pcpichpower = models.CharField(max_length=250, blank=True, null=True)
    pdschtypebgain = models.CharField(max_length=250, blank=True, null=True)
    powl_mbcch_trx = models.CharField(max_length=250, blank=True, null=True)
    powl_tch_trxs = models.CharField(max_length=250, blank=True, null=True)
    powt_mbcch_trx = models.CharField(max_length=250, blank=True, null=True)
    powt_tch_trxs = models.CharField(max_length=250, blank=True, null=True)
    pscrambcode = models.CharField(max_length=250, blank=True, null=True)
    ra = models.CharField(max_length=250, blank=True, null=True)
    rac = models.CharField(max_length=250, blank=True, null=True)
    ref_signal_power = models.CharField(max_length=250, blank=True, null=True)
    rnc_id = models.CharField(max_length=250, blank=True, null=True)
    rnc_name = models.CharField(max_length=250, blank=True, null=True)
    root_sequence_index = models.CharField(max_length=250, blank=True, null=True)
    server = models.CharField(max_length=250, blank=True, null=True)
    tch = models.CharField(max_length=250, blank=True, null=True)
    uarfcndownlink = models.CharField(max_length=250, blank=True, null=True)
    uarfcnuplink = models.CharField(max_length=250, blank=True, null=True)
    uplink_bandwidth = models.CharField(max_length=250, blank=True, null=True)
    uplink_earfcn = models.CharField(max_length=250, blank=True, null=True)
    uraids = models.CharField(max_length=250, blank=True, null=True)
    ant_gain = models.CharField(max_length=250, blank=True, null=True)
    ant_hbw = models.CharField(max_length=250, blank=True, null=True)
    ant_model = models.CharField(max_length=250, blank=True, null=True)
    ant_type = models.CharField(max_length=250, blank=True, null=True)
    ant_vbw = models.CharField(max_length=250, blank=True, null=True)
    antenna_output_power = models.CharField(max_length=250, blank=True, null=True)
    cell_application = models.CharField(max_length=250, blank=True, null=True)
    cell_last_update = models.CharField(max_length=250, blank=True, null=True)
    cell_remarks = models.CharField(max_length=250, blank=True, null=True)
    cell_status = models.CharField(max_length=250, blank=True, null=True)
    cell_type = models.CharField(max_length=250, blank=True, null=True)
    cell_updated_by = models.CharField(max_length=250, blank=True, null=True)
    height = models.CharField(max_length=250, blank=True, null=True)
    latitude = models.CharField(max_length=250, blank=True, null=True)
    longitude = models.CharField(max_length=250, blank=True, null=True)
    m_tilt = models.CharField(max_length=250, blank=True, null=True)
    map_beamwidth = models.CharField(max_length=250, blank=True, null=True)
    map_radius = models.CharField(max_length=250, blank=True, null=True)
    mobile_fixed = models.CharField(max_length=250, blank=True, null=True)
    ret = models.CharField(max_length=250, blank=True, null=True)
    rru_location = models.CharField(max_length=250, blank=True, null=True)
    sector_no = models.CharField(max_length=250, blank=True, null=True)
    site_last_update = models.CharField(max_length=250, blank=True, null=True)
    site_name = models.CharField(max_length=250, blank=True, null=True)
    trx_count = models.CharField(max_length=250, blank=True, null=True)
    integration_datetime = models.CharField(max_length=250, blank=True, null=True) 
    onair_datetime = models.CharField(max_length=250, blank=True, null=True)        
    user_label = models.CharField(max_length=250, blank=True, null=True)

    '''
    def __str__(self):
        return self.cell_name

    @property
    def trx(self):
        return self.trx_set.all()

#[ DONE ]
class Trx(models.Model):
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
    record_status = models.IntegerField(default=1)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

'''
homing_id =
trxfreq =
'''
    def __str__(self):
        return self.trx_name


class Location(models.Model):
    code = models.IntegerField()
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=30)
    region = models.CharField(max_length=4)
    regionname = models.CharField(max_length=40)
    area = models.CharField(max_length=3)

    '''
    additional fields
    location_id_text = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    latitude = models.CharField(max_length=250, blank=True, null=True)
    location_name = models.CharField(max_length=250, blank=True, null=True)
    longitude = models.CharField(max_length=250, blank=True, null=True)
    '''

    def __str__(self):
        return "{} | {}".format(self.province, self.city)


class TocAor(models.Model):
    cluster = models.CharField(unique=True, max_length=25)
    area = models.CharField(max_length=3)
    supervisor = models.CharField(max_length=60, blank=True, null=True)
    manager = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.cluster


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


class SiteNeAsset(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    trx = models.ForeignKey(Trx, blank=True, null=True, on_delete=models.CASCADE)
    smartsite = models.ForeignKey('SmartSite', on_delete=models.CASCADE)
    smartne = models.ForeignKey('SmartNe', on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)


class SmartParkedNe(models.Model):
    sitene = models.ForeignKey('SmartNE', on_delete=models.CASCADE)
    date_parked = models.DateTimeField()
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)


class DeviceSyncStatus(models.Model):
    device_name = models.CharField(max_length=250, unique=True)
    ne_type = models.CharField(max_length=50)
    sync_status = models.CharField(max_length=25)
    record_status = models.IntegerField(default=1)
    update_at = models.DateTimeField(auto_now=True)

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


class IMA_GRP_3G(models.Model):
    ems_id = models.CharField(max_length=10, blank=True, null=True) # db_column='EMS_ID'
    idnum = models.CharField(max_length=130, blank=True, null=True) # db_column='IDNUM
    dn = models.CharField(max_length=130, blank=True, null=True) # db_column='DN'
    parent_id = models.CharField(max_length=20, blank=True, null=True) # db_column='Parent ID'
    parent_dn = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent DN'


class IMA_LNK_3G(models.Model):
    ems_id = models.CharField(max_length=10, blank=True, null=True) # db_column='EMS_ID'
    idnum = models.CharField(max_length=140, blank=True, null=True) # db_column='IDNUM'
    dn = models.CharField(max_length=140, blank=True, null=True) # db_column='DN'
    parent_id = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent ID'
    parent_dn = models.CharField(max_length=130, blank=True, null=True) # db_column='Parent DN'


class Bandwidth(models.Model):
    device_id = models.CharField(max_length=60, blank=True, null=True) # db_column='Device ID'
    bandwidth = models.CharField(max_length=15, blank=True, null=True) # db_column= 'Bandwidth'
    tech = models.CharField(max_length=20, blank=True, null=True) # db_column='Tech'


class BSC(models.Model):
    area = models.CharField(max_length=20, blank=True, null=True) # db_column='Area'
    bsc_no = models.CharField(max_length=20, blank=True, null=True) # db_column='BSC No'
    bsc_loc = models.CharField(max_length=30, blank=True, null=True) # db_column='BSC LOCATION'
    ao_ip_bh_cap = models.CharField(max_length=5, blank=True, null=True) # db_column='AO IP BH Capacity'
    sig_bh_cap = models.CharField(max_length=250, blank=True, null=True) # db_column='SIGTRAN BH Capacity'
    gbo_ip_bh_cap = models.CharField(max_length=5, blank=True, null=True) # db_column='GBO IP BH Capacity'
    combined_ip_bh = models.CharField(max_length=5, blank=True, null=True) # db_column='COMBINED IP BH Capacity'


class BSC_RNC(models.Model):
    ne_name = models.CharField(max_length=10) # db_column='NE NAME'
    msc_poolname = models.CharField(max_length=250, blank=True, null=True) # db_column='MSC POOL NAME'
    msc_name = models.CharField(max_length=5) # db_column='MSC NAME'
    spc_name = models.CharField(max_length=10, blank=True, null=True) # db_column='SPC NAME'
    int_net_code = models.CharField(max_length=250, blank=True, null=True) # db_column='INT NET CODE'
    int_spnet_code = models.CharField(max_length=250, blank=True, null=True) # db_column='INT SP NET CODE'
    nat_code = models.CharField(max_length=250, blank=True, null=True) # db_column='NAT CODE'
    nat_sp_code = models.CharField(max_length=10, blank=True, null=True) # db_column='NAT SP CODE'
    sgsn_name = models.CharField(max_length=250, blank=True, null=True) # db_column='SGSN NAME'
    sgsn_pool_name = models.CharField(max_length=250, blank=True, null=True) # db_column='SGSN POOL NAME'
    ne_index = models.CharField(max_length=5) # db_column='NE INDEX'
    type = models.CharField(max_length=5) # db_column='TYPE'
    netid = models.CharField(max_length=250, blank=True, null=True) # db_column='NET ID'


class CEMDEV(models.Model):
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


class CEMIP(models.Model):
    dn = models.CharField(max_length=20, blank=True, null=True) # db_column='DN'
    ne_type = models.CharField(max_length=5, blank=True, null=True) # db_column='NE Type'
    ip_add = models.CharField(max_length=15, blank=True, null=True) # db_column='IP Address'
    type = models.CharField(max_length=5, blank=True, null=True) # db_column='Type'


class CEMNRI(models.Model):
    dn = models.CharField(max_length=20, blank=True, null=True) # db_column='DN'
    nri = models.CharField(max_length=5, blank=True, null=True) # db_column='NRI'


class CSPGCTRL(models.Model):
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


class ENODEB(models.Model):
    ne_id = models.CharField(max_length=10, blank=True, null=True) # db_column=' NE ID'
    ne_name = models.CharField(max_length=30, blank=True, null=True) # db_column='NE NAME'
    cpia = models.CharField(max_length=20, blank=True, null=True) # db_column='CPIA'
    upia = models.CharField(max_length=20, blank=True, null=True) # db_column='UPIA'
    mme_name = models.CharField(max_length=250, blank=True, null=True) # db_column='MME NAME'
    mcc = models.CharField(max_length=5, blank=True, null=True) # db_column='MCC'
    mnc = models.CharField(max_length=5, blank=True, null=True) # db_column='MNC'
    mme_pname = models.CharField(max_length=250, blank=True, null=True) # db_column='MME POOL NAME'


class ERDIP(models.Model):
    bsc_id = models.CharField(max_length=10, blank=True, null=True) #d b_column='BSC.ID'
    rbl_id = models.CharField(max_length=5, blank=True, null=True) # db_column='RBL.ID'
    tg_id = models.CharField(max_length=10, blank=True, null=True) # db_column='TG.ID
    device_id = models.CharField(max_length=20, blank=True, null=True) # db_column='DEVICE.ID'


class IP_POOLINV(models.Model):
    device_id = models.CharField(max_length=20, blank=True, null=True) # db_column='DEVICE ID'
    apn = models.CharField(max_length=50, blank=True, null=True) # db_column='APN'
    ip_pname = models.CharField(max_length=30, blank=True, null=True) # db_column='IP POOL NAME'
    cidr = models.CharField(max_length=20, blank=True, null=True) # db_column='CIDR'
    iprange = models.CharField(max_length=60, blank=True, null=True) # db_column='IPRANGE'
    totalips = models.CharField(max_length=5, blank=True, null=True) # db_column='TOTALIPS'
    usableips = models.CharField(max_length=5, blank=True, null=True) # db_column='USABLEIPS'
    remarks = models.CharField(max_length=250, blank=True, null=True) # db_column='REMARKS'


class Link(models.Model):
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

'''
additional fields
service = models.CharField(max_length=250, blank=True, null=True)
direction = models.CharField(max_length=250, blank=True, null=True)
zend_ip = models.CharField(max_length=250, blank=True, null=True)
domain = models.CharField(max_length=250, blank=True, null=True)
link_id = models.CharField(max_length=250, blank=True, null=True)
loop = models.CharField(max_length=250, blank=True, null=True)
'''

class LTunnel(models.Model):
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


class NBINT(models.Model):
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


class PCCapacity(models.Model):
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


class Parked(models.Model):
    site_no = models.CharField(max_length=10, blank=True, null=True) # db_column='SITENO'
    band = models.CharField(max_length=10, blank=True, null=True) # db_column='BAND'
    tech = models.CharField(max_length=10, blank=True, null=True) # db_column='TECH'


class PSCoreDevice(models.Model):
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

	'''
	additional fields
	max_num_5g_nsa_opt3_subs = models.CharField(max_length=250, blank=True, null=True)
	max_num_5g_nsa_opt3_bear_num = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bas_sw_sgw = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bas_sw_pgw = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bas_sw_sgw_c = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bas_sw_pgw_c = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bac_sw_sgw_u = models.CharField(max_length=250, blank=True, null=True)
	bea_num_sup_5g_nsa_bas_sw_pgw_u = models.CharField(max_length=250, blank=True, null=True)
	diameter_basic_sw_package = models.CharField(max_length=250, blank=True, null=True)
	pol_cont_ovr_gx_int_using_dia = models.CharField(max_length=250, blank=True, null=True)
	hw_capacity = models.CharField(max_length=250, blank=True, null=True)
	num_of_act_subs = models.CharField(max_length=250, blank=True, null=True)
	num_subs_served_by_spr = models.CharField(max_length=250, blank=True, null=True)
	num_sy_online_sessions = models.CharField(max_length=250, blank=True, null=True)
	num_call_online_ses_ovr_rx_int = models.CharField(max_length=250, blank=True, null=True)
	'''

class RNC(models.Model):
    area = models.CharField(max_length=15, blank=True, null=True) # db_column='Area'
    rnc_no = models.CharField(max_length=20, blank=True, null=True) # db_column='RNC No'
    rnc_location = models.CharField(max_length=30, blank=True, null=True) # db_column='RNC LOCATION'
    bandwidth_cap_lups = models.CharField(max_length=10, blank=True, null=True) # db_column='Bandwidth Capacity luPS Provisioned'
    bandwidth_cap_lucs = models.CharField(max_length=5, blank=True, null=True) # db_column='Bandwidth Capacity luCS Provisioned'
    combined_ipbh_cap = models.CharField(max_length=10, blank=True, null=True) # db_column='Combined IP BH Capacity'


class RSAGAlarm(models.Model):
    host = models.CharField(max_length=10, blank=True, null=True) # db_column='HOST'
    alarm_name = models.CharField(max_length=70, blank=True, null=True) # db_column='ALARM NAME'
    network_element = models.CharField(max_length=10, blank=True, null=True) # db_column='NETWORK ELEMENT (NE)'
    alarm_category = models.CharField(max_length=15, blank=True, null=True) # db_column='ALARM CATEGORY'


class TDTopology(models.Model):
    aend = models.CharField(max_length=30, blank=True, null=True) # db_column='AEND'
    zend = models.CharField(max_length=30, blank=True, null=True) # db_column='ZEND'
    domain = models.CharField(max_length=20, blank=True, null=True) # db_column='DOMAIN'
    function = models.CharField(max_length=20, blank=True, null=True) # db_column='FUNCTION'

#[ DONE ]
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


'''

    class CSOutageRCA(models.Model):
        bcrc_core = models.CharField(max_length=250, blank=True, null=True)
        bcrn_ran = models.CharField(max_length=250, blank=True, null=True)
        ne_type = models.CharField(max_length=250, blank=True, null=True)


    class PSOutageRCA(models.Model):
        nsei = models.CharField(max_length=250, blank=True, null=True)
        peer_ip_address = models.CharField(max_length=250, blank=True, null=True)
        ne_id = models.CharField(max_length=250, blank=True, null=True)
        link_number = models.CharField(max_length=250, blank=True, null=True)
        dest_entity_code = models.CharField(max_length=250, blank=True, null=True)
        route_index = models.CharField(max_length=250, blank=True, null=True)
        bsc_id = models.CharField(max_length=250, blank=True, null=True)
        bsc_name = models.CharField(max_length=250, blank=True, null=True)
        sgsn_pool = models.CharField(max_length=250, blank=True, null=True)
        rnc_id = models.CharField(max_length=250, blank=True, null=True)
        rnc_name = models.CharField(max_length=250, blank=True, null=True)
        usn_pool_name = models.CharField(max_length=250, blank=True, null=True)


    class Site(models.Model):
        site_id = models.CharField(max_length=250, blank=True, null=True)
        site_name = models.CharField(max_length=250, blank=True, null=True)
        region_site = models.CharField(max_length=250, blank=True, null=True)
        fm_office = models.CharField(max_length=250, blank=True, null=True)
        longitude = models.CharField(max_length=250, blank=True, null=True)
        latitude = models.CharField(max_length=250, blank=True, null=True)
        site_stage_label = models.CharField(max_length=250, blank=True, null=True)
        site_type_label = models.CharField(max_length=250, blank=True, null=True)
        parent_site  = models.CharField(max_length=250, blank=True, null=True)
        site_priority_label = models.CharField(max_length=250, blank=True, null=True)
        access_type_label = models.CharField(max_length=250, blank=True, null=True)
        area = models.CharField(max_length=250, blank=True, null=True)
        transport_type_label = models.CharField(max_length=250, blank=True, null=True)
        morphology = models.CharField(max_length=250, blank=True, null=True)
        contractor = models.CharField(max_length=250, blank=True, null=True)
        power_type = models.CharField(max_length=250, blank=True, null=True)
        project_name = models.CharField(max_length=250, blank=True, null=True)
        location_id = models.CharField(max_length=250, blank=True, null=True)
        lessor_name = models.CharField(max_length=250, blank=True, null=True)
        lessor's_mobile_phone = models.CharField(max_length=250, blank=True, null=True)
        lessor_address = models.CharField(max_length=250, blank=True, null=True)
        altitude = models.CharField(max_length=250, blank=True, null=True)
        is_hub = models.CharField(max_length=250, blank=True, null=True)
        is_vip = models.CharField(max_length=250, blank=True, null=True)
        site_state = models.CharField(max_length=250, blank=True, null=True)
        is_boundary = models.CharField(max_length=250, blank=True, null=True)
        room_type = models.CharField(max_length=250, blank=True, null=True)
        has_generator = models.CharField(max_length=250, blank=True, null=True)
        generator_type_label = models.CharField(max_length=250, blank=True, null=True)
        generator_number = models.CharField(max_length=250, blank=True, null=True)
        functional_location = models.CharField(max_length=250, blank=True, null=True)
        integration_date = models.CharField(max_length=250, blank=True, null=True)
        acceptance_date = models.CharField(max_length=250, blank=True, null=True)
        pln_id = models.CharField(max_length=250, blank=True, null=True)
        fuel_tank_no = models.CharField(max_length=250, blank=True, null=True)
        genset_number = models.CharField(max_length=250, blank=True, null=True)
        air_conditioner_no = models.CharField(max_length=250, blank=True, null=True)
        life_cycle = models.CharField(max_length=250, blank=True, null=True)
        cluster_id = models.CharField(max_length=250, blank=True, null=True)
        collocation_id = models.CharField(max_length=250, blank=True, null=True)
        collocation_name = models.CharField(max_length=250, blank=True, null=True)
        radius_km = models.CharField(max_length=250, blank=True, null=True)
        site_maintainer = models.CharField(max_length=250, blank=True, null=True)
        owner = models.CharField(max_length=250, blank=True, null=True)
        site_address = models.CharField(max_length=250, blank=True, null=True)
        covered_scope = models.CharField(max_length=250, blank=True, null=True)
        phase = models.CharField(max_length=250, blank=True, null=True)
        device_location = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        hang_site_number = models.CharField(max_length=250, blank=True, null=True)
        access_issue = models.CharField(max_length=250, blank=True, null=True)
        dangerous_site = models.CharField(max_length=250, blank=True, null=True)
        org = models.CharField(max_length=250, blank=True, null=True)
        date_on_aired = models.CharField(max_length=250, blank=True, null=True)
        municipality_psgcode = models.CharField(max_length=250, blank=True, null=True)
        province_psgcode = models.CharField(max_length=250, blank=True, null=True)
        access_restriction = models.CharField(max_length=250, blank=True, null=True)
        major_node = models.CharField(max_length=250, blank=True, null=True)
        has_room = models.CharField(max_length=250, blank=True, null=True)
        city = models.CharField(max_length=250, blank=True, null=True)
        ppgis_city_code = models.CharField(max_length=250, blank=True, null=True)
        province = models.CharField(max_length=250, blank=True, null=True)
        travel_duration = models.CharField(max_length=250, blank=True, null=True)
        tower_height = models.CharField(max_length=250, blank=True, null=True)
        tower_type = models.CharField(max_length=250, blank=True, null=True)
        mtf = models.CharField(max_length=250, blank=True, null=True)
        vip = models.CharField(max_length=250, blank=True, null=True)
        malls = models.CharField(max_length=250, blank=True, null=True)
        schools = models.CharField(max_length=250, blank=True, null=True)
        residential = models.CharField(max_length=250, blank=True, null=True)
        churches = models.CharField(max_length=250, blank=True, null=True)
        hospitals = models.CharField(max_length=250, blank=True, null=True)
        cemetery = models.CharField(max_length=250, blank=True, null=True)
        port = models.CharField(max_length=250, blank=True, null=True)
        intl_airport = models.CharField(max_length=250, blank=True, null=True)
        dom_airport = models.CharField(max_length=250, blank=True, null=True)
        busterminal = models.CharField(max_length=250, blank=True, null=True)
        cbd = models.CharField(max_length=250, blank=True, null=True)
        government_offices = models.CharField(max_length=250, blank=True, null=True)
        touristspots = models.CharField(max_length=250, blank=True, null=True)
        eventsservingsite = models.CharField(max_length=250, blank=True, null=True)
        hotels = models.CharField(max_length=250, blank=True, null=True)
        corp = models.CharField(max_length=250, blank=True, null=True)
        pd_rd = models.CharField(max_length=250, blank=True, null=True)
        mpic_offices = models.CharField(max_length=250, blank=True, null=True)
        smart_stores = models.CharField(max_length=250, blank=True, null=True)
        decom_remarks = models.CharField(max_length=250, blank=True, null=True)
        for_decom = models.CharField(max_length=250, blank=True, null=True)
        municipality_class = models.CharField(max_length=250, blank=True, null=True)
        site_ref = models.CharField(max_length=250, blank=True, null=True)
        site_remarks = models.CharField(max_length=250, blank=True, null=True)
        site_updated_by = models.CharField(max_length=250, blank=True, null=True)
        sub_area = models.CharField(max_length=250, blank=True, null=True)
        tower_type = models.CharField(max_length=250, blank=True, null=True)
        under_project = models.CharField(max_length=250, blank=True, null=True)
        barangay = models.CharField(max_length=250, blank=True, null=True)


    class USNUGWPool(models.Model):
        ne = models.CharField(max_length=250, blank=True, null=True)
        pool_name = models.CharField(max_length=250, blank=True, null=True)


    class APNUGWMapping(models.Model):
        apn = models.CharField(max_length=250, blank=True, null=True)
        ugw = models.CharField(max_length=250, blank=True, null=True)


    class MSSPool(models.Model):
        mss_name = models.CharField(max_length=250, blank=True, null=True)
        pool_name = models.CharField(max_length=250, blank=True, null=True)


    class RANHoming(models.Model):
        area = models.CharField(max_length=250, blank=True, null=True)
        ran_vendor = models.CharField(max_length=250, blank=True, null=True)
        technology = models.CharField(max_length=250, blank=True, null=True)
        location_site = models.CharField(max_length=250, blank=True, null=True)
        site_tac_details = models.CharField(max_length=250, blank=True, null=True)
        vugw_homing = models.CharField(max_length=250, blank=True, null=True)


    class DCSite(models.Model):
        ne_name = models.CharField(max_length=250, blank=True, null=True)
        dc_site = models.CharField(max_length=250, blank=True, null=True)


    class GGSNClustering(models.Model):
        cluster = models.CharField(max_length=250, blank=True, null=True)
        ggsn = models.CharField(max_length=250, blank=True, null=True)


    class SourceSinkLookup(models.Model):
        port = models.CharField(max_length=250, blank=True, null=True)
        source = models.CharField(max_length=250, blank=True, null=True)
        sink = models.CharField(max_length=250, blank=True, null=True)
        rtnif_pla = models.CharField(max_length=250, blank=True, null=True)


    class MIAndBBGrouping(models.Model):
        apn_designation = models.CharField(max_length=250, blank=True, null=True)
        apn = models.CharField(max_length=250, blank=True, null=True)


    class GTMTop99RankGroup(models.Model):
        top99 = models.CharField(max_length=250, blank=True, null=True)
        gtm_rank2020 = models.CharField(max_length=250, blank=True, null=True)
        gtm_group2020 = models.CharField(max_length=250, blank=True, null=True)
        area = models.CharField(max_length=250, blank=True, null=True)


    class BCAPolygonMapping(models.Model):
        polygon_id = models.CharField(max_length=250, blank=True, null=True)
        geozone_province = models.CharField(max_length=250, blank=True, null=True)
        polygon_name_new = models.CharField(max_length=250, blank=True, null=True)
        polygon_name_old = models.CharField(max_length=250, blank=True, null=True)
        siteno = models.CharField(max_length=250, blank=True, null=True)
        date = models.CharField(max_length=250, blank=True, null=True)


    class POINetworkTagging(models.Model):
        trunk_group = models.CharField(max_length=250, blank=True, null=True)
        network = models.CharField(max_length=250, blank=True, null=True)
        vendor = models.CharField(max_length=250, blank=True, null=True)


    class Path(models.Model):
        pathid = models.CharField(max_length=250, blank=True, null=True)
        path_type = models.CharField(max_length=250, blank=True, null=True)
        path_hop = models.CharField(max_length=250, blank=True, null=True)
        ne_name = models.CharField(max_length=250, blank=True, null=True)
        ne_type = models.CharField(max_length=250, blank=True, null=True)
        ingress_interface_name = models.CharField(max_length=250, blank=True, null=True)
        egress_interface_name = models.CharField(max_length=250, blank=True, null=True)



    class TimeZone(models.Model):
        zone_id = models.CharField(max_length=250, blank=True, null=True)
        dst_id = models.CharField(max_length=250, blank=True, null=True)
        key_context = models.CharField(max_length=250, blank=True, null=True)
        zone_name = models.CharField(max_length=250, blank=True, null=True)
        zone_offset = models.CharField(max_length=250, blank=True, null=True)


    class Org(models.Model):
        org_code = models.CharField(max_length=250, blank=True, null=True)
        org_name = models.CharField(max_length=250, blank=True, null=True)
        group = models.CharField(max_length=250, blank=True, null=True)


    class Region(models.Model):
        region_name = models.CharField(max_length=250, blank=True, null=True)
        region_level = models.CharField(max_length=250, blank=True, null=True)
        region_manager = models.CharField(max_length=250, blank=True, null=True)
        mobile_regional_manager = models.CharField(max_length=250, blank=True, null=True)
        logical_id = models.CharField(max_length=250, blank=True, null=True)
        come_from = models.CharField(max_length=250, blank=True, null=True)
        latitude_number = models.CharField(max_length=250, blank=True, null=True)
        longitude_number = models.CharField(max_length=250, blank=True, null=True)


    class RegionLevel(models.Model):
        region_level_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        level = models.CharField(max_length=250, blank=True, null=True)


    class DeviceState(models.Model):
        device_state_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)

    class DeviceLevel(models.Model):
        device_level_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class SiteAccessType(models.Model):
        access_type_name = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)


    class SiteType(models.Model):
        site_type_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class SiteTransportType(models.Model):
        transport_type_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class Area(models.Model):
        area_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)


    class Vendor(models.Model):
        vendor = models.CharField(max_length=250, blank=True, null=True)
        contact = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        is_actual = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        mail = models.CharField(max_length=250, blank=True, null=True)
        phone = models.CharField(max_length=250, blank=True, null=True)
        value = models.CharField(max_length=250, blank=True, null=True)
        vendor_code = models.CharField(max_length=250, blank=True, null=True)


    class Province(models.Model):
        province_id = models.CharField(max_length=250, blank=True, null=True)
        province_name = models.CharField(max_length=250, blank=True, null=True)
        region = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        city = models.CharField(max_length=250, blank=True, null=True)


    class EMS(models.Model):
        ems_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        ems_address = models.CharField(max_length=250, blank=True, null=True)
        ems_ip = models.CharField(max_length=250, blank=True, null=True)
        ems_port = models.CharField(max_length=250, blank=True, null=True)
        ems_type = models.CharField(max_length=250, blank=True, null=True)
        ems_version = models.CharField(max_length=250, blank=True, null=True)
        equip_type = models.CharField(max_length=250, blank=True, null=True)
        installation_date = models.CharField(max_length=250, blank=True, null=True)
        license_expired_dae = models.CharField(max_length=250, blank=True, null=True)
        ne_version = models.CharField(max_length=250, blank=True, null=True)
        server_mode = models.CharField(max_length=250, blank=True, null=True)
        site = models.CharField(max_length=250, blank=True, null=True)
        vendor = models.CharField(max_length=250, blank=True, null=True)
        ems_ipv6 = models.CharField(max_length=250, blank=True, null=True)


    class EMSType(models.Model):
        ems_type_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        value_id = models.CharField(max_length=250, blank=True, null=True)


    class PARKED(models.Model):
        siteno = models.CharField(max_length=250, blank=True, null=True)
        band = models.CharField(max_length=250, blank=True, null=True)
        tech = models.CharField(max_length=250, blank=True, null=True)


    class NetworkType(models.Model):
        network_type_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class DeviceType(models.Model):
        device_type_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        network_type_id = models.CharField(max_length=250, blank=True, null=True)


    class Domain(models.Model):
        name = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        vendor = models.CharField(max_length=250, blank=True, null=True)
        value_id = models.CharField(max_length=250, blank=True, null=True)


    class Subdomain(models.Model):
        subdomain_id = models.CharField(max_length=250, blank=True, null=True)
        subdomain_name = models.CharField(max_length=250, blank=True, null=True)
        im_subdomain_name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        domain = models.CharField(max_length=250, blank=True, null=True)
        im_subdomain_id = models.CharField(max_length=250, blank=True, null=True)


    class RCADomain(models.Model):
        name = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)

    class NEType(models.Model):
        ne_type_id_in_ems = models.CharField(max_length=250, blank=True, null=True)
        ne_type_name = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        device_type = models.CharField(max_length=250, blank=True, null=True)
        ems_type = models.CharField(max_length=250, blank=True, null=True)
        product_type = models.CharField(max_length=250, blank=True, null=True)
        rca_domain = models.CharField(max_length=250, blank=True, null=True)
        physically_exist = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        domain = models.CharField(max_length=250, blank=True, null=True)


    class Product(models.Model):
        vm_name = models.CharField(max_length=250, blank=True, null=True)
        instance_id = models.CharField(max_length=250, blank=True, null=True)
        short_description = models.CharField(max_length=250, blank=True, null=True)
        owner_name = models.CharField(max_length=250, blank=True, null=True)
        owner_contact = models.CharField(max_length=250, blank=True, null=True)
        category = models.CharField(max_length=250, blank=True, null=True)
        vm_type = models.CharField(max_length=250, blank=True, null=True)
        item = models.CharField(max_length=250, blank=True, null=True)
        manufacturer_name = models.CharField(max_length=250, blank=True, null=True)
        software_type = models.CharField(max_length=250, blank=True, null=True)
        build_number = models.CharField(max_length=250, blank=True, null=True)
        patch_number = models.CharField(max_length=250, blank=True, null=True)
        vm_description = models.CharField(max_length=250, blank=True, null=True)


    class ProductType(models.Model):
        product_type = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        networktype = models.CharField(max_length=250, blank=True, null=True)


    class DeviceMaintenance(models.Model):
        maintenance_name = models.CharField(max_length=250, blank=True, null=True)
        device = models.CharField(max_length=250, blank=True, null=True)
        maintenance_start_time = models.CharField(max_length=250, blank=True, null=True)
        maintenance_end_time = models.CharField(max_length=250, blank=True, null=True)


    class ModuleType(models.Model):
        module_type_name = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)
        ne type = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)


    class SiteMaintenance(models.Model):
        maintenance_name = models.CharField(max_length=250, blank=True, null=True)
        site = models.CharField(max_length=250, blank=True, null=True)
        maintenance_start_time = models.CharField(max_length=250, blank=True, null=True)
        maintenance_end_time = models.CharField(max_length=250, blank=True, null=True)


    class Contractor(models.Model):
        contractor_name = models.CharField(max_length=250, blank=True, null=True)
        contract = models.CharField(max_length=250, blank=True, null=True)
        phone = models.CharField(max_length=250, blank=True, null=True)
        email = models.CharField(max_length=250, blank=True, null=True)
        address = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)

    class FMOffice(models.Model):
        fm_office_name = models.CharField(max_length=250, blank=True, null=True)
        fm_office_name = models.CharField(max_length=250, blank=True, null=True)
        management_region = models.CharField(max_length=250, blank=True, null=True)
        timezone = models.CharField(max_length=250, blank=True, null=True)
        network_type = models.CharField(max_length=250, blank=True, null=True)


    class ManagementRegion(models.Model):
        management_region_name = models.CharField(max_length=250, blank=True, null=True)
        parent_management_region = models.CharField(max_length=250, blank=True, null=True)


    class OilMachineType(models.Model):
        oil_machine_type = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class FaultLevel(models.Model):
        fault_level = models.CharField(max_length=250, blank=True, null=True)
        description = models.CharField(max_length=250, blank=True, null=True)
        label = models.CharField(max_length=250, blank=True, null=True)


    class Technology(models.Model):
        technology_code = models.CharField(max_length=250, blank=True, null=True)
        technology_name = models.CharField(max_length=250, blank=True, null=True)


    class AlarmCategory(models.Model):
        alarm_category_code = models.CharField(max_length=250, blank=True, null=True)
        alarm_category_name = models.CharField(max_length=250, blank=True, null=True)


    class Trunk(models.Model):
        trunk_name = models.CharField(max_length=250, blank=True, null=True)
        destination = models.CharField(max_length=250, blank=True, null=True)
        source = models.CharField(max_length=250, blank=True, null=True)
        trunk_type = models.CharField(max_length=250, blank=True, null=True)


    class SubnetworkConnection(models.Model):
        name = models.CharField(max_length=250, blank=True, null=True)
        additionalinfo = models.CharField(max_length=250, blank=True, null=True)
        aend = models.CharField(max_length=250, blank=True, null=True)
        aendtrans = models.CharField(max_length=250, blank=True, null=True)
        anedn = models.CharField(max_length=250, blank=True, null=True)
        anodename = models.CharField(max_length=250, blank=True, null=True)
        aptp = models.CharField(max_length=250, blank=True, null=True)
        dataresourceid = models.CharField(max_length=250, blank=True, null=True)
        direction = models.CharField(max_length=250, blank=True, null=True)
        dn = models.CharField(max_length=250, blank=True, null=True)
        emsname = models.CharField(max_length=250, blank=True, null=True)
        nativeemsname = models.CharField(max_length=250, blank=True, null=True)
        networkrouted = models.CharField(max_length=250, blank=True, null=True)
        owner = models.CharField(max_length=250, blank=True, null=True)
        parentdn = models.CharField(max_length=250, blank=True, null=True)
        rate = models.CharField(max_length=250, blank=True, null=True)
        rerouteallowed = models.CharField(max_length=250, blank=True, null=True)
        sncstate = models.CharField(max_length=250, blank=True, null=True)
        snctype = models.CharField(max_length=250, blank=True, null=True)
        staticprotectionlevel = models.CharField(max_length=250, blank=True, null=True)
        userlabel = models.CharField(max_length=250, blank=True, null=True)
        version = models.CharField(max_length=250, blank=True, null=True)
        zend = models.CharField(max_length=250, blank=True, null=True)
        zendtrans = models.CharField(max_length=250, blank=True, null=True)
        znedn = models.CharField(max_length=250, blank=True, null=True)
        znodename = models.CharField(max_length=250, blank=True, null=True)
        zptp = models.CharField(max_length=250, blank=True, null=True)

    class ONT(models.MODEL):
        dn = models.CharField(max_length=250, blank=True, null=True)
        ont_name = models.CharField(max_length=250, blank=True, null=True)
        ems_id = models.CharField(max_length=250, blank=True, null=True)
        vendor_name = models.CharField(max_length=250, blank=True, null=True)
        ont_port = models.CharField(max_length=250, blank=True, null=True)
        olt_name = models.CharField(max_length=250, blank=True, null=True)
        slot_number = models.CharField(max_length=250, blank=True, null=True)
        olt_number = models.CharField(max_length=250, blank=True, null=True)
        customer_id = models.CharField(max_length=250, blank=True, null=True)


    class Service(models.Model):
        device_id = models.CharField(max_length=250, blank=True, null=True)
        voice_service_id = models.CharField(max_length=250, blank=True, null=True)
        data_service_id = models.CharField(max_length=250, blank=True, null=True)
        iptv_1 = models.CharField(max_length=250, blank=True, null=True)
        iptv_2 = models.CharField(max_length=250, blank=True, null=True)
        iptv_3 = models.CharField(max_length=250, blank=True, null=True)
        termination_point = models.CharField(max_length=250, blank=True, null=True)
        service_status = models.CharField(max_length=250, blank=True, null=True)


    class TG(models.Model):
        devicename = models.CharField(max_length=250, blank=True, null=True)
        emsname = models.CharField(max_length=250, blank=True, null=True)
        frame = models.CharField(max_length=250, blank=True, null=True)
        slot = models.CharField(max_length=250, blank=True, null=True)
        port = models.CharField(max_length=250, blank=True, null=True)
        link_id = models.CharField(max_length=250, blank=True, null=True)
        link_name = models.CharField(max_length=250, blank=True, null=True)
        circuit_group_name = models.CharField(max_length=250, blank=True, null=True)
        interconnecting_carrier = models.CharField(max_length=250, blank=True, null=True)
'''

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
