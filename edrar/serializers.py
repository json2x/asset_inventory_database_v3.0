from rest_framework import serializers
from api.serializers import DevicesSerializer, TrxSerializer
from api.models import Cell

class CellsDeviceTrxSerializer(serializers.ModelSerializer):

    device = DevicesSerializer(many=False)
    trx = TrxSerializer(many=True)
    
    class Meta:
        model = Cell
        fields = (
            'id', 'domain', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'azimuth', 'record_status', 'trx', 'device'
        )