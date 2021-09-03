from django.db import models

class Device(models.Model):
    dn = models.CharField(max_length=250, blank=True, null=True)
    device_id = models.CharField(max_length=250, blank=True, null=True)
    ems_device_id = models.CharField(max_length=250, blank=True, null=True)
    device_alias = models.CharField(max_length=250, blank=True, null=True)
    device_ip = models.CharField(max_length=250, blank=True, null=True)
    ems_id = models.CharField(max_length=250, blank=True, null=True)
    vendor_id = models.CharField(max_length=250, blank=True, null=True)
    ne_type = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=250, blank=True, null=True)
    hardware_description = models.CharField(max_length=250, blank=True, null=True)
    functional_description = models.CharField(max_length=250, blank=True, null=True)
    parent_device_id = models.CharField(max_length=250, blank=True, null=True)
    parentdn = models.CharField(max_length=250, blank=True, null=True)
    site_id = models.CharField(max_length=250, blank=True, null=True)
    device_state = models.CharField(max_length=250, blank=True, null=True)
    software_version = models.CharField(max_length=250, blank=True, null=True)
    integration_date = models.CharField(max_length=250, blank=True, null=True)
    end_of_support = models.CharField(max_length=250, blank=True, null=True)
    tsa_scope = models.CharField(max_length=250, blank=True, null=True)
    product_id = models.CharField(max_length=250, blank=True, null=True)
    serial_number = models.CharField(max_length=250, blank=True, null=True)
    freq_tx_rx_field = models.CharField(max_length=250, blank=True, null=True)
    hardware_capacity = models.CharField(max_length=250, blank=True, null=True)
    domain = models.CharField(max_length=250, blank=True, null=True)
    ne_owner = models.CharField(max_length=250, blank=True, null=True)
    tx_clusterimg = models.CharField(max_length=250, blank=True, null=True)
    tx_type = models.CharField(max_length=250, blank=True, null=True)
    natspcode = models.CharField(max_length=250, blank=True, null=True)
    admin_state = models.CharField(max_length=250, blank=True, null=True)
    subdomain = models.CharField(max_length=250, blank=True, null=True)
    function = models.CharField(max_length=250, blank=True, null=True)
    iubce_dl_lic = models.CharField(max_length=250, blank=True, null=True)
    iubce_ul_lic = models.CharField(max_length=250, blank=True, null=True)
    s1cu_lic = models.CharField(max_length=250, blank=True, null=True)
    record_status = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Devices'

class Cell(models.Model):
    ems_cell_id = models.CharField(max_length=250, blank=True, null=True)
    ems_id = models.CharField(max_length=250, blank=True, null=True)
    cell_name = models.CharField(max_length=250)
    dn = models.CharField(max_length=250, blank=True, null=True)
    site = models.CharField(max_length=10)
    parent_id = models.CharField( max_length=250)
    parent_dn = models.CharField(max_length=250, blank=True, null=True)
    tech = models.CharField(max_length=250, blank=True, null=True)
    band = models.CharField(max_length=250, blank=True, null=True)
    admin_state = models.CharField(max_length=250, blank=True, null=True)
    alias = models.CharField(max_length=250, blank=True, null=True)
    lac_tac = models.CharField(max_length=250, blank=True, null=True)
    sac_ci_eutra = models.CharField(max_length=250, blank=True, null=True)
    rnc_cid = models.CharField(max_length=250, blank=True, null=True)
    phy_cid = models.CharField(max_length=250, blank=True, null=True)
    lcr_cid = models.CharField(max_length=250, blank=True, null=True)
    mcc = models.CharField(max_length=250, blank=True, null=True)
    mnc = models.CharField(max_length=250, blank=True, null=True)
    nodeid = models.CharField(max_length=250, blank=True, null=True)
    sector_id = models.CharField(max_length=250, blank=True, null=True)
    carrier = models.CharField(max_length=250, blank=True, null=True)
    ne_type = models.CharField(max_length=250, blank=True, null=True)
    subdomain = models.CharField(max_length=250, blank=True, null=True)
    function = models.CharField(max_length=250, blank=True, null=True)
    sdcch_cap = models.CharField(max_length=250, blank=True, null=True)
    tch_cap = models.CharField(max_length=250, blank=True, null=True)
    homing_id = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    dlear_fcn = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    ulear_dcn = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    dlc_hbw = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    ulc_hbw = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    rac = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    ncc = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    bcc = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    nnode_id = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    nbscid = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    psc = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    bcchno = models.CharField(max_length=250, blank=True, null=True) #Not in AID
    record_status = models.CharField(max_length=250, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Cells'
    

class Trx(models.Model):
    ems_trx_id = models.CharField(max_length=250, blank=True, null=True)
    ems_id = models.CharField(max_length=250, blank=True, null=True)
    trx_name = models.CharField(max_length=250, blank=True, null=True)
    dn = models.CharField(max_length=250, blank=True, null=True)
    site_id = models.CharField(max_length=250, blank=True, null=True)
    parent_id = models.CharField(max_length=250, blank=True, null=True)
    parent_dn = models.CharField(max_length=250, blank=True, null=True)
    admin_state = models.CharField(max_length=250, blank=True, null=True)
    e1_assignment = models.CharField(max_length=250, blank=True, null=True)
    homing_bts = models.CharField(max_length=250, blank=True, null=True)
    homing_id = models.CharField(max_length=250, blank=True, null=True) #Not is AID
    trxfreq = models.CharField(max_length=250, blank=True, null=True) #Not is AID
    record_status = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'TRX'