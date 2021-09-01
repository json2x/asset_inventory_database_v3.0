from rest_framework import serializers
from .models import Device, Cell, Trx

class NmsDevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            'id', 'dn', 'device_id', 'ems_device_id', 'device_alias', 'device_ip', 'ems_id', 'vendor_id', 
            'ne_type', 'model', 'hardware_description', 'functional_description', 'parent_device_id', 
            'parentdn', 'site_id', 'device_state', 'software_version', 'integration_date', 'end_of_support', 
            'tsa_scope', 'product_id', 'serial_number', 'freq_tx_rx_field', 'hardware_capacity', 'domain', 
            'ne_owner', 'tx_clusterimg', 'tx_type', 'natspcode', 'admin_state', 'subdomain', 'function', 
            'iubce_dl_lic', 'iubce_ul_lic', 's1cu_lic'
        )

class NmsCellsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = (
            'id', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'homing_id', 'dlear_fcn', 'ulear_dcn', 'dlc_hbw', 'ulc_hbw',
            'rac', 'ncc', 'bcc', 'nnode_id', 'nbscid', 'azimuth', 'psc', 'bcchno'
        )
    
class NmsTrxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trx
        fields = (
            'id', 'ems_trx_id', 'ems_id', 'trx_name', 'dn', 'site_id', 'parent_id', 
            'parent_dn', 'admin_state', 'e1_assignment', 'homing_bts', 'homing_id',
            'trxfreq'
        )