var G_NE_DATA = {};
var G_DEVICE_DATA = {};
var G_CELL_DATA = {};
var G_TRX_DATA = {};
var G_DEVICE_DATA_AID = {};
var G_CELL_DATA_AID = {};
var G_TRX_DATA_AID = {};
var G_DEVICE_DATA_NMS = {};
var G_CELL_DATA_NMS = {};
var G_TRX_DATA_NMS = {};

const G_DATA_SOURCE = {'AID': 'aid', 'NMS': 'nms'}
const G_DATATABLE_TYPE = {'Device': 'Device', 'Cell': 'Cell', 'TRX': 'TRX'}
const G_TECH_LIST = {'2G': '2G', '3G': '3G', 'FD-LTE': 'FD-LTE', 'TD-LTE': 'TD-LTE', '5G': '5G'}
const G_FIELD_MAP = {
    'DEVICE': {'device_name': 'device_id', 'vendor': 'vendor_id', 'homing': 'parent_device_id', 'equipment_type': 'model'},
    'CELL': {
        '2G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'trx_config': '', 'bandwidth': '',},
        '3G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'rnc_cid', 'lac': 'lac_tac', 'sac': 'sac_ci_eutra', 'iub_type': '', 'bandwidth': '',},
        'FD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        'TD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        '5G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
    }
}

const G_NMS_SRC_ACTIVITY = {
    'Device': ['Rollout'],
    'Cell': ['Rollout', 'Expansion'],
    'Trx': ['Rollout', 'Expansion', 'TRX Expansion']
}