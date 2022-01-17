from django.db import models
from django_pandas.managers import DataFrameManager

class Site(models.Model):                                                           # Source: SID - Site List Report
    site_id = models.CharField(max_length=250)                                      # src file col='Site ID'
    parent_site_id = models.CharField(max_length=250)                               # src file col='Parent Site ID'
    site_name = models.CharField(max_length=250)                                    # src file col='Site Name'
    latitude = models.CharField(max_length=10, blank=True, null=True)               # src file col='Latitude'
    longitude = models.CharField(max_length=10, blank=True, null=True)              # src file col='Logitude'
    site_stage_name = models.CharField(max_length=20, blank=True, null=True)        # src file col='Site Stage Name'
    site_type_name = models.CharField(max_length=20, blank=True, null=True)         # src file col='Site Type Name'
    access_restriction = models.CharField(max_length=250, blank=True, null=True)    # src file col='Access Restriction'
    area_name = models.CharField(max_length=20, blank=True, null=True)              # src file col='Area Name'
    major_node = models.CharField(max_length=5, blank=True, null=True)              # src file col='Major Node'
    has_room = models.CharField(max_length=25, blank=True, null=True)               # src file col='Has Room'
    site_owner = models.CharField(max_length=250, blank=True, null=True)            # src file col='Site Owner'
    region_name = models.CharField(max_length=10, blank=True, null=True)            # src file col='Region Name'
    city = models.CharField(max_length=50, blank=True, null=True)                   # src file col='City'
    ppgis_city_code = models.CharField(max_length=5, blank=True, null=True)         # src file col='PPGIS City Code'
    province = models.CharField(max_length=40, blank=True, null=True)               # src file col='Province'
    lessor_name = models.CharField(max_length=170, blank=True, null=True)           # src file col='Lessor Name'
    lessor_phone = models.CharField(max_length=170, blank=True, null=True)          # src file col='Lessor Phone'
    altitude_m = models.CharField(max_length=10, blank=True, null=True)             # src file col='Altitude(m)'
    address = models.CharField(max_length=250, blank=True, null=True)               # src file col='Address'
    travel_duration = models.CharField(max_length=250, blank=True, null=True)       # src file col='Travel Duration(m)'
    tower_height = models.CharField(max_length=30, blank=True, null=True)           # src file col='Tower Height'
    tower_type = models.CharField(max_length=90, blank=True, null=True)             # src file col='Tower Type'
    mtf = models.CharField(max_length=5, blank=True, null=True)                     # src file col='MTF'
    vip = models.CharField(max_length=5, blank=True, null=True)                     # src file col='VIP'
    malls = models.CharField(max_length=5, blank=True, null=True)                   # src file col='Malls'
    schools = models.CharField(max_length=5, blank=True, null=True)                 # src file col='Schools'
    residentials = models.CharField(max_length=5, blank=True, null=True)            # src file col='Residentials'
    churches = models.CharField(max_length=5, blank=True, null=True)                # src file col='Churches'
    hospitals = models.CharField(max_length=5, blank=True, null=True)               # src file col='Hospitals'
    cemetery = models.CharField(max_length=5, blank=True, null=True)                # src file col='Cemetery'
    port = models.CharField(max_length=5, blank=True, null=True)                    # src file col='Port'
    intl_airport = models.CharField(max_length=5, blank=True, null=True)            # src file col='Intl Airport'
    dom_airport = models.CharField(max_length=5, blank=True, null=True)             # src file col='Dom Airport'
    bus_terminal = models.CharField(max_length=5, blank=True, null=True)            # src file col='Bus Terminal'
    cbd = models.CharField(max_length=5, blank=True, null=True)                     # src file col='CBD'
    gov = models.CharField(max_length=5, blank=True, null=True)                     # src file col='Government'
    offices = models.CharField(max_length=5, blank=True, null=True)                 # src file col='Offices'
    tourists_spots = models.CharField(max_length=5, blank=True, null=True)          # src file col='Tourists Spots'
    events_serving_site = models.CharField(max_length=5, blank=True, null=True)     # src file col='Events Serving Site'
    hotels = models.CharField(max_length=5, blank=True, null=True)                  # src file col='Hotels'
    corp = models.CharField(max_length=5, blank=True, null=True)                    # src file col='Corp'
    pd_rd = models.CharField(max_length=5, blank=True, null=True)                   # src file col='PD/RD'
    mpic_office = models.CharField(max_length=5, blank=True, null=True)             # src file col='MPIC Offices'
    smart_stores = models.CharField(max_length=5, blank=True, null=True)            # src file col='Smart Stores'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_record_sync_date = models.DateField()                                    # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.site_id, self.site_name)

    @property
    def smart_site(self):
        try:
            return SmartSite.objects.get(site_id = self.site_id)
        except:
            return None


###################################################################################################################

class PHLocation(models.Model):
    code = models.IntegerField()
    citymun = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    regionname = models.CharField(max_length=250)
    area = models.CharField(max_length=250)

    objects = DataFrameManager()

    def __str__(self):
        return self.cluster

###################################################################################################################

class Aor(models.Model):
    cluster = models.CharField(unique=True, max_length=250)
    area = models.CharField(max_length=250)
    supervisor = models.CharField(max_length=250, blank=True, null=True)
    manager = models.CharField(max_length=250, blank=True, null=True)

    record_status = models.IntegerField(default=1)

    objects = DataFrameManager()

    def __str__(self):
        return self.cluster

###################################################################################################################

class SmartSite(models.Model):
    site_id = models.CharField(unique=True, max_length=250)
    site_name = models.CharField(max_length=250)
    address = models.TextField(blank=True, null=True)
    geolocation = models.ForeignKey(PHLocation, on_delete=models.SET_NULL, blank=True, null=True)
    aor = models.ForeignKey(Aor, on_delete=models.SET_NULL, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)

    record_status = models.IntegerField(default=1)

    objects = DataFrameManager()

    def __str__(self):
        return '{} {}'.format(self.site_id, self.site_name)

###################################################################################################################

class Device(models.Model):
    domain = models.CharField(max_length=250)                                       # db_column='Domain'
    ems_id = models.CharField(max_length=250)                                       # db_column='EMS ID'
    device_id = models.CharField(max_length=250)                                    # db_column='Device ID'
    dn = models.CharField(max_length=250, blank=True, null=True)                    # db_column='DN'
    ems_device_id = models.CharField(max_length=250, blank=True, null=True)         # db_column='EMS Device ID'
    device_alias = models.CharField(max_length=250, blank=True, null=True)          # db_column='Device Alias'
    device_ip = models.CharField(max_length=250, blank=True, null=True)             # db_column='Device IP'
    vendor_id = models.CharField(max_length=250, blank=True, null=True)             # db_column='Vendor ID'
    ne_type = models.CharField(max_length=250, blank=True, null=True)               # db_column='NE Type'
    model = models.CharField(max_length=250, blank=True, null=True)                 # Field name made lowercase.
    hw_desc = models.CharField(max_length=250, blank=True, null=True)               # db_column='Hardware Description'      #hw_desc sa dynamic inventory
    fnc_desc = models.CharField(max_length=250, blank=True, null=True)              # db_column='Functional Description'    #fnc_desc sa dynamic inventory
    parent_device_id = models.CharField(max_length=250, blank=True, null=True)      # db_column='Parent Device ID'
    parentdn = models.CharField(max_length=250, blank=True, null=True)              # db_column='ParentDN'
    site_id = models.CharField(max_length=250, blank=True, null=True)               # db_column='Site ID'
    device_state = models.CharField(max_length=250, blank=True, null=True)          # db_column='Device State'
    software_version = models.CharField(max_length=250, blank=True, null=True)      # db_column='Software Version'
    int_date = models.CharField( max_length=250, blank=True, null=True)             # db_column='Integration Date           #int_date sa dynamic inventory
    end_of_support = models.CharField(max_length=250, blank=True, null=True)        # db_column='End of Support'
    tsa_scope = models.CharField(max_length=250, blank=True, null=True)             # db_column='TSA Scope'
    prod_id = models.CharField(max_length=250, blank=True, null=True)               # db_column='Product ID'                #prod_id
    serial_no = models.CharField(max_length=250, blank=True, null=True)             # db_column='Serial Number'             #serial_no
    freq_txrx = models.CharField(max_length=250, blank=True, null=True)             # db_column='FREQ (TX_RX)'				#freq_txrx
    hw_cap = models.CharField(max_length=250, blank=True, null=True)                # db_column='Hardware Capacity'			#hw_cap
    ne_owner = models.CharField(max_length=250, blank=True, null=True)              # db_column='NE Owner'
    tx_cluster = models.CharField(max_length=250, blank=True, null=True)            # db_column='TX Clusterimg'             #tx_cluster
    tx_type = models.CharField(max_length=250, blank=True, null=True)               # db_column='TX Type'                   #tx_type
    nat_sp_code = models.CharField(max_length=250, blank=True, null=True)           # db_column='NATSPCODE' 				#nat_sp_code
    admin_state = models.CharField( max_length=250, blank=True, null=True)          # db_column='Admin State
    subdomain = models.CharField(max_length=250, blank=True, null=True)             # db_column='SUBDOMAIN'
    function = models.CharField(max_length=250, blank=True, null=True)              # db_column='FUNCTION'
    iubce_dl_lic = models.CharField(max_length=250, blank=True, null=True)          # db_column='IUBCE DL LIC'
    iubce_ul_lic = models.CharField(max_length=250, blank=True, null=True)          # db_column='IUBCE UL LIC'
    s1cu_lic = models.CharField(max_length=250, blank=True, null=True)              # db_column='S1CU LIC'
    cluster_region = models.CharField(max_length=250, blank=True, null=True)        # db_column='Cluster Region'
    cluster_sub_region = models.CharField(max_length=250, blank=True, null=True)    # db_column='Cluster Sub Region'
    cluster_province = models.CharField(max_length=250, blank=True, null=True)      # db_column='Cluster Province'
    cluster_city = models.CharField(max_length=250, blank=True, null=True)          # db_column='Cluster City'
    mw_hub = models.CharField(max_length=250, blank=True, null=True)                # db_column='MW HUB'

    vlr_capacity = models.CharField(max_length=250, blank=True, null=True)          # Added for ESA
    simultaneous_pdp = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA
    radius_km = models.CharField(max_length=250, blank=True, null=True)             # Added for ESA
    device_ipv6_address = models.CharField(max_length=250, blank=True, null=True)   # Added for ESA
    org = models.CharField(max_length=250, blank=True, null=True)                   # Added for ESA
    sau_license = models.CharField(max_length=250, blank=True, null=True)           # Added for ESA
    unpacking = models.CharField(max_length=250, blank=True, null=True)             # Added for ESA
    version = models.CharField(max_length=250, blank=True, null=True)               # Added for ESA
    device_level_label = models.CharField(max_length=250, blank=True, null=True)    # Added for ESA
    maintenance_personnel = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    source = models.CharField(max_length=250, blank=True, null=True)                # Added for ESA
    is_hub = models.CharField(max_length=250, blank=True, null=True)                # Added for ESA
    is_vip = models.CharField(max_length=250, blank=True, null=True)                # Added for ESA
    site_state = models.CharField(max_length=250, blank=True, null=True)            # Added for ESA
    cabinet_type = models.CharField(max_length=250, blank=True, null=True)          # Added for ESA
    int_date2 = models.CharField(max_length=250, blank=True, null=True)             # Added for ESA
    license_expired_from = models.CharField(max_length=250, blank=True, null=True)  # Added for ESA
    acceptance_date = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    rack_type = models.CharField(max_length=250, blank=True, null=True)             # Added for ESA
    business_case = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    asset_number = models.CharField(max_length=250, blank=True, null=True)          # Added for ESA
    brand = models.CharField(max_length=250, blank=True, null=True)                 # Added for ESA
    device_position = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    capacity = models.CharField(max_length=250, blank=True, null=True)              # Added for ESA
    old_id = models.CharField(max_length=250, blank=True, null=True)                # Added for ESA
    igwb_software = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    hardware_lifecycle = models.CharField(max_length=250, blank=True, null=True)    # Added for ESA
    ethernet_switch = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    functional_location = models.CharField(max_length=250, blank=True, null=True)   # Added for ESA
    gn_throughput_license = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    payload_license = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    pool = models.CharField(max_length=250, blank=True, null=True)                  # Added for ESA
    project_definition = models.CharField(max_length=250, blank=True, null=True)    # Added for ESA
    s1_lub_capacity = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    ce_cu_capacity = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    #cap_key_s1_traffic = models.CharField(max_length=250, blank=True, null=True)   # Added for ESA				#this is the same with s1cu_lic
    #cap_key_cu = models.CharField(max_length=250, blank=True, null=True)           # Added for ESA              #this is the same with s1cu_lic
    ericsson_microwave_sl_cap = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    longitude = models.CharField(max_length=250, blank=True, null=True)             # Added for ESA
    latitude = models.CharField(max_length=250, blank=True, null=True)              # Added for ESA

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.device_id, self.subdomain)

    @property
    def cells(self):
        return self.cell_set.all()

    @property
    def has_invalid_chars_in_device_name(self):
        device_name = self.device_id
        return not device_name.isalnum()

    @property
    def smart_site(self):
        try:
            return SmartSite.objects.get(site_id = self.site_id)
        except:
            return None
            

    class Meta:
        unique_together = ['domain', 'ems_id', 'device_id', 'dn']

###################################################################################################################

class Cell(models.Model):
    domain = models.CharField(max_length=250)  		                                # db_column='Domain'
    ems_id = models.CharField(max_length=250)  		                                # db_column='EMS ID'
    ems_cell_id = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='EMS Cell ID'
    cell_name = models.CharField(max_length=250)  							        # db_column='Cell Name'
    dn = models.CharField(max_length=250, blank=True, null=True)  			        # db_column='DN'
    site_id = models.CharField(max_length=250)  							        # db_column='Site'
    parent_id = models.CharField( max_length=250)  							        # db_column='Parent ID
    parent_dn = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='Parent DN'
    tech = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='Tech'
    band = models.CharField(max_length=250)  								        # db_column='Band'
    admin_state = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='Admin State'
    alias = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='Alias'             #no output
    lac_tac = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='LAC TAC'
    sac_ci_eutra = models.CharField(max_length=250, blank=True, null=True)          # db_column='SAC CI EUTRA'
    rnc_cid = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='RNC CID'
    phy_cid = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='PHY CID'
    lcr_cid = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='LCR CID
    mcc = models.CharField(max_length=250, blank=True, null=True)  			        # db_column='MCC'
    mnc = models.CharField(max_length=250, blank=True, null=True)  			        # db_column='MNC'
    nodeid = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='NODEID'
    sector_id = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='SECTOR ID
    carrier = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='CARRIER
    ne_type = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='NE TYPE'
    subdomain = models.CharField(max_length=250)  							        # db_column='SUBDOMAIN
    function = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='FUNCTION'
    sdcch_cap = models.CharField(max_length=250, blank=True, null=True)  	        # db_column='SDCCH CAP'
    tch_cap = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='TCH CAP'
    azimuth = models.CharField(max_length=250, blank=True, null=True)  		        # db_column='Azimut             #no output
	
    bcc = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    bspwr = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    bspwrb = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    bspwrt = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    bstxpwr = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    cell_active_state = models.CharField(max_length=250, blank=True, null=True)     # Added for ESA
    cell_admin_state = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA
    cell_id = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    cell_index = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA
    configured_maxtxpower = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    crs_gain = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    downlink_bandwidth = models.CharField(max_length=250, blank=True, null=True)    # Added for ESA
    downlink_earfcn = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA
    local_cell_id = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    max_transmission_power = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    mbcch = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    mimo = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA           		#none for now; will clarify pa
    ncc = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    pa_for_even_power_distribution = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    pb = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    pcpichpower = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA
    pdschtypebgain = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    powl_mbcch_trx = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    powl_tch_trxs = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    powt_mbcch_trx = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    powt_tch_trxs = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    pscrambcode = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA
    ra = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    rac = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    ref_signal_power = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA
    rnc_id = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    rnc_name = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    root_sequence_index = models.CharField(max_length=250, blank=True, null=True)   # Added for ESA
    server = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA                 	#Derived value based on where the dump was taken. but ERI gave the attr so may value ito but for 4G lang
    tch = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA
    uarfcndownlink = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    uarfcnuplink = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA
    uplink_bandwidth = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA
    uplink_earfcn = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA
    uraids = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA
    ant_gain = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA              	#Derived value based on Antenna Model Reference file.
    ant_hbw = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA                	#Derived value based on Antenna Model Reference file. but ERI gave the attr so may value ito but for 4G lang
    ant_model = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA             		#Input value from engineers.
    ant_type = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA              	#Derived value based on Antenna Model Reference file.
    ant_vbw = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA               	#Derived value based on Antenna Model Reference file.
    antenna_output_power = models.CharField(max_length=250, blank=True, null=True)  # Added for ESA   
    cell_application = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA      			#Input value from engineers.
    cell_last_update = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA       		    #Input value from engineers. but ERI gave the attr so may value ito but for 4G lang 
    cell_remarks = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA          		#Input value from engineers.
    cell_status = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA            		#Input value from engineers. but ERI gave the attr so may value ito but for 4G lang
    cell_type = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA              	#Input value from engineers. but ERI gave the attr so may value ito but for 4G lang
    cell_updated_by = models.CharField(max_length=250, blank=True, null=True)       # Added for ESA       			#Input value from engineers.
    height = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA                	#Input value from engineers.
    latitude = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA               	#Input value from engineers. but ERI gave the attr so may value ito but for 3G, 4G lang
    longitude = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA              	#Input value from engineers. but ERI gave the attr so may value ito but for 3G, 4G lang
    m_tilt = models.CharField(max_length=250, blank=True, null=True) 		        # Added for ESA                	#Input value from engineers.
    map_beamwidth = models.CharField(max_length=250, blank=True, null=True)         # Added for ESA          		#Derived value based on Frequency Reference file. but ERI gave the attr so may value ito but for 4G lang
    map_radius = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA            		#Derived value based on Frequency Reference file.
    mobile_fixed = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA          		#Derived value from DL EARFCN and Carrier Reference Table.
    ret = models.CharField(max_length=250, blank=True, null=True) 			        # Added for ESA                 #no output as of now, will clarify pa
    rru_location = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA          		#Input value from engineers.
    sector_no = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA              	#Derived value from Cellname and planning convention file but ERI gave the attr so may value ito but for 4G lang
    site_last_update = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA       		    #Input value from engineers. but ERI gave the attr so may value ito but for 4G lang
    site_name = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA              	#Input value from engineers. but ERI gave the attr so may value ito but for 4G lang
    trx_count = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA              	#Derived value from cellname count in GTRXDEV. no output as of now, will clarify pa
    integration_datetime = models.CharField(max_length=250, blank=True, null=True)  # Added for ESA  			    #no output
    onair_datetime = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA        			#no output
    user_label = models.CharField(max_length=250, blank=True, null=True) 	        # Added for ESA            		#no output
	
    record_status = models.IntegerField(default=1)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} {} {}'.format(self.cell_name, self.subdomain, self.band)

    @property
    def trx(self):
        return self.trx_set.all()

    class Meta:
        unique_together = ['domain', 'ems_id', 'cell_name', 'dn', 'subdomain', 'band']

###################################################################################################################

class Trx(models.Model):
    ems_id = models.CharField(max_length=250, blank=True, null=True)                # db_column='EMS ID'
    ems_trx_id = models.CharField(max_length=250, blank=True, null=True)            # db_column='EMS TRX ID'
    trx_name = models.CharField(max_length=250, blank=True, null=True)              # db_column='TRX Name'
    dn = models.CharField(max_length=250, blank=True, null=True)                    # db_column='DN'
    site_id = models.CharField(max_length=250, blank=True, null=True)               # db_column='Site ID'
    parent_id = models.CharField(max_length=250, blank=True, null=True)             # db_column='Parent ID'
    parent_dn = models.CharField(max_length=250, blank=True, null=True)             # db_column='Parent DN'
    admin_state = models.CharField(max_length=250, blank=True, null=True)           # db_column='Admin State'
    e1_assignment = models.CharField(max_length=250, blank=True, null=True)         # db_column='E1 Assignment'        #no output
    homing_bts = models.CharField(max_length=250, blank=True, null=True)            # db_column='HOMING BTS'
    homing_id = models.CharField(max_length=250, blank=True, null=True)
    trxfreq = models.CharField(max_length=250, blank=True, null=True)

    record_status = models.IntegerField(default=1)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.trx_name

    class Meta:
        unique_together = ['ems_id', 'trx_name', 'parent_id', 'homing_bts', 'homing_id']

###################################################################################################################

class SmartParked(models.Model):
    site_id = models.CharField(max_length=250)                                      # 
    band = models.CharField(max_length=250)                                         # 
    tech = models.CharField(max_length=250)                                         # 

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {} | {}'.format(self.site_id, self.band, self.tech)

###################################################################################################################

class Bandwidth(models.Model):
    device_id = models.CharField(max_length=250)                                    # 
    bandwidth = models.CharField(max_length=250)                                    # 
    tech = models.CharField(max_length=250)                                         # 

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.device_id

###################################################################################################################

class BSC(models.Model):
    area = models.CharField(max_length=250)                                         # src file col = 'Area'
    bsc_no = models.CharField(max_length=250)                                       # src file col = 'BSC No'
    bsc_loc = models.CharField(max_length=250)                                      # src file col = 'BSC\RNC LOCATION'
    ao_ip_bh_cap = models.CharField(max_length=250, blank=True, null=True)          # src file col = 'Ao IP BH Capacity'
    sig_bh_cap = models.CharField(max_length=250, blank=True, null=True)            # src file col = 'SIGTRAN BH Capacity'
    gbo_ip_bh_cap = models.CharField(max_length=250, blank=True, null=True)         # src file col = 'Gbo IP BH Capacity'
    combined_ip_bh = models.CharField(max_length=250, blank=True, null=True)        # src file col = 'COMBINED IP BH Capacity'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.bsc_no

###################################################################################################################

class RNC(models.Model):
    area = models.CharField(max_length=250)                                         # src file col = 'Area'
    rnc_no = models.CharField(max_length=250)                                       # src file col = 'RNC No'
    rnc_location = models.CharField(max_length=250)                                 # src file col = 'RNC LOCATION'
    bandwidth_cap_lups = models.CharField(max_length=250, blank=True, null=True)    # src file col = 'Bandwidth Capacity luPS Provisioned'
    bandwidth_cap_lucs = models.CharField(max_length=250, blank=True, null=True)    # src file col = 'Bandwidth Capacity luCS Provisioned'
    combined_ipbh_cap = models.CharField(max_length=250, blank=True, null=True)     # src file col = 'Combined IP BH Capacity'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.rnc_no

###################################################################################################################

class BSC_RNC(models.Model):
    ne_name = models.CharField(max_length=250)                                      # src file col = 'NE NAME'
    msc_poolname = models.CharField(max_length=250, blank=True, null=True)          # src file col = 'MSC POOL NAME'
    msc_name = models.CharField(max_length=250)                                     # src file col = 'MSC NAME'
    spc_name = models.CharField(max_length=250, blank=True, null=True)              # src file col = 'SPC NAME'
    int_net_code = models.CharField(max_length=250, blank=True, null=True)          # src file col = 'INT NET CODE'
    int_spnet_code = models.CharField(max_length=250, blank=True, null=True)        # src file col = 'INT SP NET CODE'
    nat_code = models.CharField(max_length=250, blank=True, null=True)              # src file col = 'NAT CODE'
    nat_sp_code = models.CharField(max_length=250, blank=True, null=True)           # src file col = 'NAT SP CODE'
    sgsn_name = models.CharField(max_length=250, blank=True, null=True)             # src file col = 'SGSN NAME'
    sgsn_pool_name = models.CharField(max_length=250, blank=True, null=True)        # src file col = 'SGSN POOL NAME'
    ne_index = models.CharField(max_length=250)                                     # src file col = 'NE INDEX'
    type = models.CharField(max_length=250)                                         # src file col = 'TYPE'
    netid = models.CharField(max_length=250, blank=True, null=True)                 # src file col = 'NET ID'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.ne_name

###################################################################################################################

class ENodeB(models.Model):
    ne_id = models.CharField(max_length=250, blank=True, null=True)                 # src file col = ' NE ID'
    ne_name = models.CharField(max_length=250)                                      # src file col = 'NE NAME'
    cpia = models.CharField(max_length=250, blank=True, null=True)                  # src file col = 'CPIA'
    upia = models.CharField(max_length=250, blank=True, null=True)                  # src file col = 'UPIA'
    mme_name = models.CharField(max_length=250, blank=True, null=True)              # src file col = 'MME NAME'
    mcc = models.CharField(max_length=250, blank=True, null=True)                   # src file col = 'MCC'
    mnc = models.CharField(max_length=250, blank=True, null=True)                   # src file col = 'MNC'
    mme_pname = models.CharField(max_length=250, blank=True, null=True)             # src file col = 'MME POOL NAME'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.ne_name

###################################################################################################################

class PSCoreDevice(models.Model):
    dn = models.CharField(max_length=250, blank=True, null=True)                            # src file col='DN'
    device_id = models.CharField(max_length=250)                                            # src file col='Device ID'
    ems_id = models.CharField(max_length=250)                                               # src file col='EMS ID'
    vendor_id = models.CharField(max_length=250)                                            # src file col='VendorID'
    ne_type = models.CharField(max_length=250)                                              # src file col='NE Type'
    site_id = models.CharField(max_length=250, blank=True, null=True)                       # src file col='Site ID'
    sau_license_sw = models.CharField(max_length=250, blank=True, null=True)                # src file col='SAU License SW'
    sau_hw = models.CharField(max_length=250, blank=True, null=True)                        # src file col='SAU HW'
    pdp_license_sw = models.CharField(max_length=250, blank=True, null=True)                # src file col='PDP License SW'
    throughput_license_sw = models.CharField(max_length=250, blank=True, null=True)         # src file col='Throughput License SW'
    throughput_hw_gbps = models.CharField(max_length=250, blank=True, null=True)            # src file col='Throughput HW(Gbps)'
    max_num_2g_subs_sw = models.CharField(max_length=250, blank=True, null=True)            # src file col='Max num of 2G subs SW'
    max_num_3g_subs_sw = models.CharField(max_length=250, blank=True, null=True)            # src file col='Max num of 3G subs SW'
    max_num_4g_subs_sw = models.CharField(max_length=250, blank=True, null=True)            # src file col='Max num of 4G subs SW'
    max_num_2g_act_pdp_sw = models.CharField(max_length=250, blank=True, null=True)         # src file col='Max num of 2G act PDP SW'
    max_num_3g_act_pdp_sw = models.CharField(max_length=250, blank=True, null=True)         # src file col='Max num of 3G act PDPs SW'
    max_num_4g_bearer_num_sw = models.CharField(max_length=250, blank=True, null=True)      # src file col='Max num of 4G Bearer Num SW'
    max_trans_cap_usr_sw = models.CharField(max_length=250, blank=True, null=True)          # src file col='Max trans cap of usr plane SW'
    max_num_234g_subs_hw = models.CharField(max_length=250, blank=True, null=True)          # src file col='Max num of 2G 3G 4G subs HW'
    max_num_234g_act_bear_hw = models.CharField(max_length=250, blank=True, null=True)      # src file col='Max num 2G 3G act 4G Bear HW'
    max_trans_cap_usr_hw = models.CharField(max_length=250, blank=True, null=True)          # src file col='Max trans cap of usr plane HW
    pdp_supt_basic_sw_ggsn = models.CharField(max_length=250, blank=True, null=True)        # src file col='PDP of Supt Basic SW for GGSN'
    pdp_supt_basic_sw_pgw = models.CharField(max_length=250, blank=True, null=True)         # src file col='PDP Supt Basic SW for S PGW'
    throughput_whole_ugw_sw = models.CharField(max_length=250, blank=True, null=True)       # src file col='Throughput of whole UGW SW'
    pdp_supt_basic_hw_ggsn_s_pgw = models.CharField(max_length=250, blank=True, null=True)  # src file col='PDP Supt Basic HW GGSN S PGW'
    throuhput_whole_ugw_hw = models.CharField(max_length=250, blank=True, null=True)        # src file col='Throughput of whole UGW HW'
    hw_capacity_sau = models.CharField(max_length=250, blank=True, null=True)               # src file col='HardwareCapacity(SAU)'
    hw_capacity = models.CharField(max_length=250, blank=True, null=True)                   # src file col='HardwareCapacity'
    hw_capcity_gbps = models.CharField(max_length=250, blank=True, null=True)               # src file col='HardwareCapacity(Gbps)'
    bearer_num_sbs_sgw = models.CharField(max_length=250, blank=True, null=True)            # src file col='Bearer Nos of SBSw for S-GW'
    bearer_num_sbs_pgw = models.CharField(max_length=250, blank=True, null=True)            # src file col='Bearer Nos of SBSw for P-GW '
    
    max_num_5g_nsa_opt3_subs = models.CharField(max_length=250, blank=True, null=True)      # Added for ESA
    max_num_5g_nsa_opt3_bear_num = models.CharField(max_length=250, blank=True, null=True)  # Added for ESA
    bea_num_sup_5g_nsa_bas_sw_sgw = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    bea_num_sup_5g_nsa_bas_sw_pgw = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    bea_num_sup_5g_nsa_bas_sw_sgw_c = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    bea_num_sup_5g_nsa_bas_sw_pgw_c = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    bea_num_sup_5g_nsa_bac_sw_sgw_u = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    bea_num_sup_5g_nsa_bas_sw_pgw_u = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    diameter_basic_sw_package = models.CharField(max_length=250, blank=True, null=True)     # Added for ESA
    pol_cont_ovr_gx_int_using_dia = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    hw_capacity = models.CharField(max_length=250, blank=True, null=True)                   # Added for ESA
    num_of_act_subs = models.CharField(max_length=250, blank=True, null=True)               # Added for ESA
    num_subs_served_by_spr = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    num_sy_online_sessions = models.CharField(max_length=250, blank=True, null=True)        # Added for ESA
    num_call_online_ses_ovr_rx_int = models.CharField(max_length=250, blank=True, null=True) # Added for ESA
    vdra_capacities = models.CharField(max_length=250, blank=True, null=True)               # Added for ESA
    vupcc_capacities = models.CharField(max_length=250, blank=True, null=True)              # Added for ESA

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.device_id, self.ne_type)

    class Meta:
        unique_together = ['device_id', 'ems_id', 'vendor_id', 'ne_type']

    

###################################################################################################################

class PSCoreCapacity(models.Model):
    id_str = models.CharField(max_length=20)                                        # src file col='ID'
    device_id = models.CharField(max_length=30)                                     # src file col='Device ID'
    name = models.CharField(max_length=20)                                          # src file col='Name'
    vendor = models.CharField(max_length=10, blank=True, null=True)                 # src file col='Vendor'
    area_served = models.CharField(max_length=10, blank=True, null=True)            # src file col='Area Served'
    sw_release = models.CharField(max_length=20, blank=True, null=True)             # src file col='SW Reease'
    hw_capacity_sau = models.CharField(max_length=10, blank=True, null=True)        # src file col='HW Capacity (SAU)'
    hw_capacity_pdp = models.CharField(max_length=250, blank=True, null=True)       # src file col='HW Capacity (PDP)'
    sw_capacity_sau = models.CharField(max_length=250, blank=True, null=True)       # src file col='SW Capacity (SAU)
    sw_capacity_pdp = models.CharField(max_length=250, blank=True, null=True)       # src file col='SW Capacity (PDP)'
    hw_capacity_tput = models.CharField(max_length=10, blank=True, null=True)       # src file col='HW Capacity (TPUT)'
    hw_capacity_pdp1 = models.CharField(max_length=250, blank=True, null=True)      # src file col='HW Capacity (PDP)1'
    purchasedsw_capacity_tput = models.CharField(max_length=250, blank=True, null=True) # src file col='PurchasedSW (TPUT)'
    purchasedsw_pdp = models.CharField(max_length=10, blank=True, null=True)        # src file col='Purchased SW (PDP)'
    ecu_sau = models.CharField(max_length=10, blank=True, null=True)                # src file col='ECU (SAU)'
    epu_pdp = models.CharField(max_length=10, blank=True, null=True)                # src file col='EPU (PDP)'
    ecu = models.CharField(max_length=5, blank=True, null=True)                     # src file col='ECU'
    epu = models.CharField(max_length=5, blank=True, null=True)                     # src file col='EPU'
    redunduncy_model = models.CharField(max_length=5, blank=True, null=True)        # src file col='Redunduncy Model'
    no_of_subrack = models.CharField(max_length=5, blank=True, null=True)           # src file col='No Of SubRack'
    gsc = models.CharField(max_length=5, blank=True, null=True)                     # src file col='GSC'
    active_cpb = models.CharField(max_length=5, blank=True, null=True)              # src file col='Active CPB'
    standyby_cpb = models.CharField(max_length=5, blank=True, null=True)            # src file col='Standby CPB'
    active_ppb = models.CharField(max_length=5, blank=True, null=True)              # src file col='Active PPB'
    standby_ppb = models.CharField(max_length=5, blank=True, null=True)             # src file col='Standby PPB'
    lc = models.CharField(max_length=5, blank=True, null=True)                      # src file col='LC'
    tput = models.CharField(max_length=5, blank=True, null=True)                    # src file col='TPUT'
    board_type = models.CharField(max_length=5, blank=True, null=True)              # src file col='Board Type'
    no_of_boards = models.CharField(max_length=5, blank=True, null=True)            # src file col='NoOfBoards'
    sw_capacity = models.CharField(max_length=10, blank=True, null=True)            # src file col='SW Capacity'
    chasis_type = models.CharField(max_length=20, blank=True, null=True)            # src file col='Chasis Type'
    blade_type = models.CharField(max_length=5, blank=True, null=True)              # src file col='Blade Type'
    blade_capacity = models.CharField(max_length=10, blank=True, null=True)         # src file col='Blade Capacity'
    total_no_of_blades = models.CharField(max_length=5, blank=True, null=True)      # src file col='Total Number of Blades'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.device_id, self.name)

    class Meta:
        unique_together = ['id_str', 'device_id', 'name']

###################################################################################################################

class Link(models.Model):
    idnum = models.CharField(max_length=5, blank=True, null=True)                   # src file col='IDNUM'
    name = models.CharField(max_length=250, blank=True, null=True)                  # src file col='Name'
    create_date = models.CharField(max_length=250, blank=True, null=True)           # src file col='Create Date'
    update_date = models.CharField(max_length=250, blank=True, null=True)           # src file col='Update Date'
    a_end_node_id = models.CharField(max_length=70, blank=True, null=True)          # Added for ESA
    a_end_node = models.CharField(max_length=70, blank=True, null=True)             # src file col='AEND Node'
    a_end_tp = models.CharField(max_length=60, blank=True, null=True)               # src file col='AEND TP'
    a_end_ip = models.CharField(max_length=20, blank=True, null=True)               # src file col='AEND IP'
    service = models.CharField(max_length=20, blank=True, null=True)                # src file col='Service'
    direction = models.CharField(max_length=5, blank=True, null=True)               # src file col='Direction-'
    z_end_node_id = models.CharField(max_length=70, blank=True, null=True)          # Added for ESA
    z_end_node = models.CharField(max_length=70, blank=True, null=True)             # src file col='ZEND Node'
    z_end_tp = models.CharField(max_length=80, blank=True, null=True)               # src file col='ZEND TP'
    z_end_ip = models.CharField(max_length=20, blank=True, null=True)               # src file col='ZEND IP'
    dn = models.CharField(max_length=250, blank=True, null=True)                    # src file col='DN'
    link_type = models.CharField(max_length=10, blank=True, null=True)              # src file col='Link Type'
    ems_name = models.CharField(max_length=30, blank=True, null=True)               # src file col='EMS Name'
    native_ems_name = models.CharField(max_length=15, blank=True, null=True)        # src file col='Native EMS Name'
    date_res_id = models.CharField(max_length=250, blank=True, null=True)           # src file col='Date Resource ID'
    owner = models.CharField(max_length=5, blank=True, null=True)                   # src file col='Owner'
    parent_dn = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent DN'
    rate = models.CharField(max_length=20, blank=True, null=True)                   # src file col='Rate'
    usr_label = models.CharField(max_length=150, blank=True, null=True)             # src file col='User Label'
    addtl_info = models.CharField(max_length=250, blank=True, null=True)            # src file col='Additional Info'
    ne_model = models.CharField(max_length=250, blank=True, null=True)              # Added for ESA
    link_id = models.CharField(max_length=250, blank=True, null=True)               # Added for ESA
    loop = models.CharField(max_length=250, blank=True, null=True)                  # Added for ESA
    domain = models.CharField(max_length=20, blank=True, null=True)                 # src file col='Domain'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.link_type, self.name)

###################################################################################################################

class LinkTunnel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)                  # src file col='NAME'
    link_type = models.CharField(max_length=10, blank=True, null=True)              # src file col='LINK TYPE'
    capacity = models.CharField(max_length=250, blank=True, null=True)              # src file col='CAPACITY'
    tunnel_id = models.CharField(max_length=15, blank=True, null=True)              # src file col='TUNNEL ID'
    tunnel_bandwidth = models.CharField(max_length=250, blank=True, null=True)      # src file col='TUNNEL BANDWIDTH'
    aendnode_sitecodes = models.CharField(max_length=5, blank=True, null=True)      # src file col='AENDNODE SITECODES'
    aend_node = models.CharField(max_length=20, blank=True, null=True)              # src file col='AENDNODE'
    aend_tp = models.CharField(max_length=35, blank=True, null=True)                # src file col='AEND TP'
    aend_tp_child = models.CharField(max_length=250, blank=True, null=True)         # src file col='AEND TP (CHILD)'
    aend_ip = models.CharField(max_length=250, blank=True, null=True)               # src file col='AEND IP'
    aend_equipment = models.CharField(max_length=10, blank=True, null=True)         # src file col='AEND EQUIPMENT'
    zend_node_sitecodes = models.CharField(max_length=5, blank=True, null=True)     # src file col='ZENDNODE SITECODES'
    zend_node = models.CharField(max_length=20, blank=True, null=True)              # src file col='ZENDNODE'
    zend_tp = models.CharField(max_length=35, blank=True, null=True)                # src file col='ZEND TP'
    zend_tp_child = models.CharField(max_length=250, blank=True, null=True)         # src file col='ZEND TP (CHILD)'
    zend_ip = models.CharField(max_length=250, blank=True, null=True)               # src file col='ZEND IP'
    zend_equipment = models.CharField(max_length=10, blank=True, null=True)         # src file col='ZEND EQUIPMENT'
    description = models.CharField(max_length=30, blank=True, null=True)            # src file col='DESCRIPTION'
    domain = models.CharField(max_length=250, blank=True, null=True)                # src file col='DOMAIN'
    cluster = models.CharField(max_length=250, blank=True, null=True)               # src file col='CLUSTER'
    cao_wo = models.CharField(max_length=250, blank=True, null=True)                # src file col='CAO/WO'
    band_service = models.CharField(max_length=250, blank=True, null=True)          # src file col='BAND/SERVICE'
    direction = models.CharField(max_length=250, blank=True, null=True)             # src file col='DIRECTION'
    remarks = models.CharField(max_length=60, blank=True, null=True)                # src file col='REMARKS'
    rnc_bsc = models.CharField(max_length=10, blank=True, null=True)                # src file col='RNC/BSC

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.link_type, self.name)

###################################################################################################################

class MIAndBBGrouping(models.Model):
    apn_designation = models.CharField(max_length=250)
    apn = models.CharField(max_length=250)

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.apn

###################################################################################################################

class GTMRankGroup(models.Model):
    place = models.CharField(max_length=250)
    gtm_rank = models.CharField(max_length=250)
    gtm_group = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    year = models.IntegerField(max_length=4)

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.place, self.gtm_group)

###################################################################################################################

class BCAPolygonMapping(models.Model):
    polygon_id = models.CharField(max_length=250)
    geozone_province = models.CharField(max_length=250)
    polygon_name_new = models.CharField(max_length=250, blank=True, null=True)
    polygon_name_old = models.CharField(max_length=250, blank=True, null=True)
    siteno = models.CharField(max_length=250, blank=True, null=True)
    date = models.CharField(max_length=250, blank=True, null=True)

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.polygon_id, self.geozone_province)

###################################################################################################################

class POINetworkTagging(models.Model):                                          #    New data model in ESA
    trunk_group = models.CharField(max_length=250)
    network = models.CharField(max_length=250, blank=True, null=True)
    vendor = models.CharField(max_length=250, blank=True, null=True)

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.polygon_id, self.geozone_province)

###################################################################################################################

class AccessConstraint(models.Model):
    area = models.CharField(max_length=250)                                         # src file col='DN',
    site_id = models.CharField(max_length=250)                                      # src file col='Site ID',
    exact_date = models.CharField(max_length=250)                                   # src file col='Exact Date',
    day_of_month = models.CharField(max_length=250)                                 # src file col='Day of Month',
    day_of_week = models.CharField(max_length=250)                                  # src file col='Day of Week',
    start_time = models.CharField(max_length=250)                                   # src file col='Start Time',
    end_time = models.CharField(max_length=250)                                     # src file col='End Time',
    restricted_time = models.CharField(max_length=250)                              # src file col='Restricted Time',
    site_name = models.CharField(max_length=250)                                    # src file col='Site Name',

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.site_id, self.area)

###################################################################################################################

class NBINT(models.Model):
    domain = models.CharField(max_length=250)                                       # src file col='Domain'
    ems_id = models.CharField(max_length=250, blank=True, null=True)                # src file col='EMS ID'
    parent_id = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent ID'
    lip_1 = models.CharField(max_length=250, blank=True, null=True)                 # src file col='LIP 1'
    lip_2 = models.CharField(max_length=250, blank=True, null=True)                 # src file col='LIP 2'
    own_spc = models.CharField(max_length=250, blank=True, null=True)               # src file col='Own SPC'
    assoc_set_id = models.CharField(max_length=250, blank=True, null=True)          # src file col='Assoc Set ID'
    assoc_set_name = models.CharField(max_length=250, blank=True, null=True)        # src file col='Assoc Set Name'
    assoc_index = models.CharField(max_length=250, blank=True, null=True)           # src file col='Assoc Index'
    rip_1 = models.CharField(max_length=250, blank=True, null=True)                 # src file col='RIP 1'
    rip_2 = models.CharField(max_length=250, blank=True, null=True)                 # src file col='RIP 2'
    use = models.CharField(max_length=250, blank=True, null=True)                   # src file col='USE'
    class_nbint = models.CharField(max_length=250, blank=True, null=True)           # src file col='Class'
    assoc_name = models.CharField(max_length=250, blank=True, null=True)            # src file col='ASSOC NAME'
    local_port = models.CharField(max_length=250, blank=True, null=True)            # src file col='LOCAL PORT'
    peer_port = models.CharField(max_length=250, blank=True, null=True)             # src file col='PEER PORT'
    deno = models.CharField(max_length=250, blank=True, null=True)                  # src file col='DENO'
    deno_name = models.CharField(max_length=250, blank=True, null=True)             # src file col='DENO NAME'
    leno = models.CharField(max_length=250, blank=True, null=True)                  # src file col='LENO'
    leno_name = models.CharField(max_length=250, blank=True, null=True)             # src file col='LENO NAME'
    peer_device_id = models.CharField(max_length=250, blank=True, null=True)        # src file col='PEER DEVICE ID'
    peer_spc = models.CharField(max_length=250, blank=True, null=True)              # src file col='PEER SPC'
    peer_nsei = models.CharField(max_length=250, blank=True, null=True)             # src file col='PEER A SET ID NSEI'
    peer_assoc_set = models.CharField(max_length=250, blank=True, null=True)        # src file col='PEER ASSOC SET NAME'
    name = models.CharField(max_length=250, blank=True, null=True)                  # src file col='Name'
    peer_assoc_index = models.CharField(max_length=250, blank=True, null=True)      # src file col='PEER ASSOC INDEX'
    peer_assoc_name = models.CharField(max_length=250, blank=True, null=True)       # src file col='PEER ASSOC NAME'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.domain, self.ems_id)

###################################################################################################################

class IPPoolInventory(models.Model):
    device_id = models.CharField(max_length=250)                                    # src file col='DEVICE ID'
    apn = models.CharField(max_length=250, blank=True, null=True)                   # src file col='APN'
    ip_pool_name = models.CharField(max_length=250, blank=True, null=True)          # src file col='IP POOL NAME'
    cidr = models.CharField(max_length=250, blank=True, null=True)                  # src file col='CIDR'
    iprange = models.CharField(max_length=250, blank=True, null=True)               # src file col='IPRANGE'
    totalips = models.CharField(max_length=250, blank=True, null=True)              # src file col='TOTALIPS'
    usableips = models.CharField(max_length=250, blank=True, null=True)             # src file col='USABLEIPS'
    remarks = models.CharField(max_length=250, blank=True, null=True)               # src file col='REMARKS'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.device_id, self.ip_pool_name)

###################################################################################################################

class Path(models.Model):                                                           # New data model in ESA
    pathid = models.CharField(max_length=250, blank=True, null=True)
    path_type = models.CharField(max_length=250, blank=True, null=True)
    path_hop = models.CharField(max_length=250, blank=True, null=True)
    ne_name = models.CharField(max_length=250, blank=True, null=True)
    ne_type = models.CharField(max_length=250, blank=True, null=True)
    ingress_interface_name = models.CharField(max_length=250, blank=True, null=True)
    egress_interface_name = models.CharField(max_length=250, blank=True, null=True)

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.pathid, self.path_type)

###################################################################################################################

class IMAGroup3G(models.Model):
    ems_id = models.CharField(max_length=250)                                       # src file col='EMS_ID'
    ima_grp_id = models.CharField(max_length=250, blank=True, null=True)            # src file col='ID
    dn = models.CharField(max_length=250, blank=True, null=True)                    # src file col='DN'
    parent_id = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent ID'
    parent_dn = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent DN'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.ima_grp_id

###################################################################################################################

class IMALink3G(models.Model):
    ems_id = models.CharField(max_length=250)                                       # src file col='EMS_ID'
    ima_link_id = models.CharField(max_length=250, blank=True, null=True)           # src file col='ID
    dn = models.CharField(max_length=250, blank=True, null=True)                    # src file col='DN'
    parent_id = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent ID'
    parent_dn = models.CharField(max_length=250, blank=True, null=True)             # src file col='Parent DN'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.ima_link_id

###################################################################################################################

class CEMDEVCS(models.Model):
    dn = models.CharField(max_length=250)                                           # src file col='DN'
    ne_type = models.CharField(max_length=250)                                      # src file col='NE TYPE'
    home_msc_pool = models.CharField(max_length=250, blank=True, null=True)         # src file col='Home MSC Pool'
    gt_address = models.CharField(max_length=250, blank=True, null=True)            # src file col='Gt Address'
    msc_server_type = models.CharField(max_length=250, blank=True, null=True)       # src file col='MSC Server Type'
    carrier = models.CharField(max_length=250, blank=True, null=True)               # src file col ='Carrier'
    country = models.CharField(max_length=250, blank=True, null=True)               # src file col='Country'
    spc_name = models.CharField(max_length=250, blank=True, null=True)              # src file col='SPC Name'
    int_net_code = models.CharField(max_length=250, blank=True, null=True)          # src file col='International Network Code'
    int_spnet = models.CharField(max_length=250, blank=True, null=True)             # src file col='International Spare Network'
    nat_net_code = models.CharField(max_length=250, blank=True, null=True)          # src file col='National Network Code'
    nat_spnet_code = models.CharField(max_length=250, blank=True, null=True)        # src file col='National Spare Network Code'
    bcu = models.IntegerField()                                                     # src file col='BCU'
    homing_msc = models.CharField(max_length=250, blank=True, null=True)            # src file col='Homing Msc'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.dn, self.ne_type)

###################################################################################################################

class CEMIPCS(models.Model):
    dn = models.CharField(max_length=250)                                           # src file col='DN'
    ne_type = models.CharField(max_length=250)                                      # src file col='NE Type'
    ip_add = models.CharField(max_length=15, blank=True, null=True)                 # src file col='IP Address'
    type = models.CharField(max_length=5, blank=True, null=True)                    # src file col='Type'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.dn, self.ne_type)

###################################################################################################################

class CEMNRICS(models.Model):
    dn = models.CharField(max_length=250)                                           # src file col='DN'
    nri = models.IntegerField()                                                     # src file col='NRI'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.dn

###################################################################################################################

class CSPGCTRL(models.Model):
    pg_pol = models.CharField(max_length=250)                                       # src file col='PG POL'
    msc_spc = models.CharField(max_length=250)                                      # src file col='MSC SPC'
    lai = models.CharField(max_length=250, blank=True, null=True)                   # src file col='LAI'
    pg_type = models.CharField(max_length=250, blank=True, null=True)               # src file col='PG TYPE'
    pg_times = models.IntegerField()                                                # src file col='PG TIMES'
    pg1_durh = models.IntegerField()                                                # src file col='PG1 DURH'
    pg1_idt = models.CharField(max_length=250, blank=True, null=True)               # src file col='PG1 IDT'
    pg2_durh = models.IntegerField()                                                # src file col='PG2 DURH'
    pg2_idt = models.CharField(max_length=250, blank=True, null=True)               # src file col='PG2 IDT'
    pg3_durh = models.IntegerField()                                                # src file col='PG3 DURH'
    lpg3_idtai = models.CharField(max_length=250, blank=True, null=True)            # src file col='LPG3 IDTAI'
    pg4_durh = models.IntegerField()                                                # src file col='PG4 DURH'
    pg4_idt = models.CharField(max_length=250, blank=True, null=True)               # src file col='PG4 IDT'
    pg5_durh = models.IntegerField()                                                # src file col='PG5 DURH'
    pg5_idt = models.CharField(max_length=250, blank=True, null=True)               # src file col='PG5 IDT'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.pg_pol, self.msc_spc)

###################################################################################################################

class ERDIP(models.Model):
    bsc_id = models.CharField(max_length=250)                                       # src file col='BSC.ID'
    rbl_id = models.IntegerField()                                                  # src file col='RBL.ID'
    tg_id = models.CharField(max_length=250)                                        # src file col='TG.ID
    device_id = models.CharField(max_length=250)                                    # src file col='DEVICE.ID'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return self.bsc_id

###################################################################################################################

class RSAGAlarm(models.Model):
    host = models.CharField(max_length=250)                                         # src file col='HOST'
    alarm_name = models.CharField(max_length=250)                                   # src file col='ALARM NAME'
    network_element = models.CharField(max_length=250)                              # src file col='NETWORK ELEMENT (NE)'
    alarm_category = models.CharField(max_length=250)                               # src file col='ALARM CATEGORY'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.host, self.alarm_name)

###################################################################################################################

class TDTopology(models.Model):
    aend = models.CharField(max_length=250, blank=True, null=True)                  # src file col='AEND'
    zend = models.CharField(max_length=250, blank=True, null=True)                  # src file col='ZEND'
    domain = models.CharField(max_length=250)                                       # src file col='DOMAIN'
    function = models.CharField(max_length=250)                                     # src file col='FUNCTION'

    record_status = models.IntegerField(default=1)

    no_update = models.SmallIntegerField(default=0)                                 # increment count if current record_status == 0;
    record_create_date = models.DateField(auto_now_add=True)                        # creates time stamp when record is created in table
    record_update_date = models.DateField()                                         # manually update this field every time the record is updated
    record_sync_date = models.DateField()                                           # manually update this field every time the record is synced
    objects = DataFrameManager()

    def __str__(self):
        return '{} | {}'.format(self.domain, self.function)