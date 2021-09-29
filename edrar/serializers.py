from django.db.models import fields
from rest_framework import serializers
from django.db.models import Q
import datetime

from api.serializers import DevicesSerializer, TrxSerializer
from api import models as Api


from edrar import models as Edrar

from nmsdata.serializers import NmsDevicesSerializer, NmsTrxSerializer
from nmsdata import models as Nms

class UpdateLogDailyActivitySerializer(serializers.ModelSerializer):

    tech = serializers.SerializerMethodField()
    band = serializers.SerializerMethodField()

    class Meta:
        model = Edrar.DailyActivity
        fields = (
            'date_logged', 'tech', 'user', 'counterpart', 'activity', 'site_status', 'rfs_count', 'siteid', 'band', 
            'vendor', 'homing', 'bts_id', 'device_name', 'equipment_type', 'trx_config', 'iub_type', 'bandwidth', 
            'sac', 'cell_id', 'cell_name', 'lac', 'pci', 'abis', 'iubip', 's1_c', 's1_u', 'omip', 'remarks'
        )

    def get_tech(self, activity):
        tech = Edrar.MobileTechnology.objects.get(name=activity.tech)
        return tech.id

    def get_band(self, activity):
        band = Edrar.MobileFrequencyBand.objects.get(band=activity.band)
        return band.id

    def get_date_logged(self, activity):
        return activity.date_logged.strftime("%Y-%m-%d %H:%M:%S")

class DailyActivitySerializer(serializers.ModelSerializer):

    activity = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    site_status = serializers.SerializerMethodField()
    siteid = serializers.SerializerMethodField()
    date_logged = serializers.SerializerMethodField()

    class Meta:
        model = Edrar.DailyActivity
        fields = (
            'date_logged', 'tech', 'user', 'counterpart', 'activity', 'site_status', 'rfs_count', 'siteid', 'band', 
            'vendor', 'homing', 'bts_id', 'device_name', 'equipment_type', 'trx_config', 'iub_type', 'bandwidth', 
            'sac', 'cell_id', 'cell_name', 'lac', 'pci', 'abis', 'iubip', 's1_c', 's1_u', 'omip', 'remarks'
        )

    def get_activity(self, activity):
        return activity.activity.name

    def get_user(self, activity):
        return activity.user.username

    def get_site_status(self, activity):
        return activity.site_status.name

    def get_siteid(self, activity):
        return activity.siteid.siteid

    def get_date_logged(self, activity):
        return activity.date_logged.strftime("%Y-%m-%d %H:%M:%S")

class CellsDeviceTrxSerializer(serializers.ModelSerializer):

    # device = DevicesSerializer(many=False)
    # trx = TrxSerializer(many=True)
    device = serializers.SerializerMethodField()
    trx = serializers.SerializerMethodField()
    
    class Meta:
        model = Api.Cell
        fields = (
            'id', 'domain', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'azimuth', 'record_status', 'trx', 'device'
        )

    def get_device(self, cell):
        result = Api.Device.objects.filter(~Q(record_status=3)).get(id=cell.device.id)

        return NmsDevicesSerializer(result, many=False).data

    def get_trx(self, cell):
        result = Api.Trx.objects.filter(~Q(record_status=3)).filter(cell__id=cell.id)

        return TrxSerializer(result, many=True).data



class CellsDeviceTrxNMSDataSerializer(serializers.ModelSerializer):

    domain = serializers.SerializerMethodField()
    device = serializers.SerializerMethodField()
    trx = serializers.SerializerMethodField()
    
    class Meta:
        model = Nms.Cell
        fields = (
            'id', 'domain', 'ems_cell_id', 'ems_id', 'cell_name', 'dn', 'site', 'parent_id', 'parent_dn', 
            'tech', 'band', 'admin_state', 'alias', 'lac_tac', 'sac_ci_eutra', 'rnc_cid', 'phy_cid', 
            'lcr_cid', 'mcc', 'mnc', 'nodeid', 'sector_id', 'carrier', 'ne_type', 'subdomain', 'function', 
            'sdcch_cap', 'tch_cap', 'homing_id', 'dlear_fcn', 'ulear_dcn', 'dlc_hbw', 'ulc_hbw',
            'rac', 'ncc', 'bcc', 'nnode_id', 'nbscid', 'psc', 'bcchno', 'record_status', 'device', 'trx'
        )

    def get_domain(self, cell):
        result = Edrar.MobileTechnology.objects.filter(name=cell.subdomain)
        if result:
            return 'RAN'
        else:
            return None

    def get_device(self, cell):
        result = Nms.Device.objects.filter(ems_id=cell.ems_id).filter(device_id=cell.parent_id)\
        .filter(subdomain=cell.subdomain).filter(parent_device_id=cell.homing_id)

        return NmsDevicesSerializer(result, many=True).data

    def get_trx(self, cell):
        result = Nms.Trx.objects.filter(ems_id=cell.ems_id)\
            .filter(parent_id=cell.cell_name).filter(homing_bts=cell.parent_id)\
            .filter(homing_id=cell.homing_id)

        return NmsTrxSerializer(result, many=True).data
    
class SiteTechBandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api.Cell
        fields = ('site', 'tech', 'band')