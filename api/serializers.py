from rest_framework import serializers
from .models import Trx, Cell, Device, Location, SiteNeAsset, SmartNe, SmartSite, TocAor


class TrxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trx
        fields = (
            'id', 'ems_trx_id', 'ems_id', 'trx_name', 'dn', 'site_id', 'parent_id', 
            'parent_dn', 'admin_state', 'e1_assignment', 'homing_bts', 'record_status'
        )
    

class CellsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = (
            'id', 'domain', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'azimuth', 'record_status', 'device'
        )


class DevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            'id', 'dn', 'device_id', 'ems_device_id', 'device_alias', 'device_ip', 'ems_id', 'vendor_id', 
            'ne_type', 'model', 'hardware_description', 'functional_description', 'parent_device_id', 
            'parentdn', 'site_id', 'device_state', 'software_version', 'integration_date', 'end_of_support', 
            'tsa_scope', 'product_id', 'serial_number', 'freq_tx_rx_field', 'hardware_capacity', 'domain', 
            'ne_owner', 'tx_clusterimg', 'tx_type', 'natspcode', 'admin_state', 'subdomain', 'function', 
            'iubce_dl_lic', 'iubce_ul_lic', 's1cu_lic', 'cluster_region', 'cluster_sub_region', 
            'cluster_province', 'cluster_city', 'mw_hub', 'record_status', 'has_invalid_chars_in_device_name'
        )
        

class DeviceAndCellsSerializer(serializers.ModelSerializer):
    cells = CellsSerializer(many=True)

    class Meta:
        model = Device
        fields = (
            'id', 'dn', 'device_id', 'ems_device_id', 'device_alias', 'device_ip', 'ems_id', 'vendor_id', 
            'ne_type', 'model', 'hardware_description', 'functional_description', 'parent_device_id', 
            'parentdn', 'site_id', 'device_state', 'software_version', 'integration_date', 'end_of_support', 
            'tsa_scope', 'product_id', 'serial_number', 'freq_tx_rx_field', 'hardware_capacity', 'domain', 
            'ne_owner', 'tx_clusterimg', 'tx_type', 'natspcode', 'admin_state', 'subdomain', 'function', 
            'iubce_dl_lic', 'iubce_ul_lic', 's1cu_lic', 'cluster_region', 'cluster_sub_region', 
            'cluster_province', 'cluster_city', 'mw_hub', 'record_status', 
            'has_invalid_chars_in_device_name', 'cells'
        )


class SmartNeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmartNe
        fields = ('id', 'siteid', 'band', 'tech', 'record_status', 'update_at', 'smartsite')


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'city', 'province', 'region', 'area')


class TocAorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TocAor
        fields = ('id', 'cluster', 'area')


class SmartSiteSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)
    toc_aor = TocAorSerializer(many=False)
    class Meta:
        model = SmartSite
        fields = (
            'id', 'siteid', 'sitename', 'address', 'location', 'toc_aor',
            'lat', 'lng', 'record_status', 'update_at'
        )


class SmartSiteAndNEsSerializer(serializers.ModelSerializer):
    smartne = SmartNeSerializer(many=True)
    location = LocationSerializer(many=False)
    toc_aor = TocAorSerializer(many=False)
    class Meta:
        model = SmartSite
        fields = (
            'id', 'siteid', 'sitename', 'address', 'location', 'toc_aor', 
            'lat', 'lng', 'record_status', 'update_at', 'smartne'
        )

class SmartSiteCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SmartSite
        fields = (
            'id', 'siteid', 'sitename', 'address', 'location', 'toc_aor', 
            'lat', 'lng', 'record_status', 'update_at'
        )


class SiteNeAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmartNe
        fields = ('id', 'cell', 'site', 'ne', 'device', 'update_at')

'''
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token
'''