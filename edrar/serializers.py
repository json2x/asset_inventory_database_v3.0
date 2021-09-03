from rest_framework import serializers
from api.serializers import DevicesSerializer, TrxSerializer
from api.models import Cell

from nmsdata.serializers import NmsDevicesSerializer, NmsTrxSerializer
from nmsdata import models as Nms

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

class CellsDeviceTrxNMSDataSerializer(serializers.ModelSerializer):

    device = serializers.SerializerMethodField()
    trx = serializers.SerializerMethodField()
    
    class Meta:
        model = Nms.Cell
        fields = (
            'id', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'homing_id', 'dlear_fcn', 'ulear_dcn', 'dlc_hbw', 'ulc_hbw',
            'rac', 'ncc', 'bcc', 'nnode_id', 'nbscid', 'psc', 'bcchno', 'device', 'trx'
        )

    def get_device(self, obj):
        result = Nms.Device.objects.filter(ems_id=obj.ems_id)\
            .filter(device_id=obj.parent_id)\
            .filter(subdomain=obj.subdomain)\
            .filter(parent_device_id=obj.homing_id)

        return NmsDevicesSerializer(result, many=True).data

    def get_trx(self, obj):
        result = Nms.Trx.objects.filter(ems_id=obj.ems_id)\
            .filter(parent_id=obj.cell_name)\
            .filter(homing_bts=obj.parent_id)\
            .filter(homing_id=obj.homing_id)

        return NmsTrxSerializer(result, many=True).data