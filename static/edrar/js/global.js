var G_LOGGED_ACTIVITY = {}
var G_NE_DATA = {};
var G_DISCARDED_NE_DATA = {
    'nms': {
        'DEVICE': [],
        'CELL': [],
        'TRX': [],
    }, 
    'aid': {
        'DEVICE': [],
        'CELL': [],
        'TRX': [],
    }
}
const G_DATA_SOURCE = {'AID': 'aid', 'NMS': 'nms'}
const G_DATATABLE_TYPE = {'Device': 'Device', 'Cell': 'Cell', 'TRX': 'TRX'}
const G_TECH_LIST = {'2G': '2G', '3G': '3G', 'FD-LTE': 'FD-LTE', 'TD-LTE': 'TD-LTE', '5G': '5G'}
const G_FIELD_MAP = {
    'DEVICE': {'device_name': 'device_id', 'vendor': 'vendor_id', 'homing': 'parent_device_id', 'equipment_type': 'model'},
    'CELL': {
        '2G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'trx_config': '', 'bandwidth': '', 'omip': '', 'abis': ''},
        '3G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'rnc_cid', 'lac': 'lac_tac', 'sac': 'sac_ci_eutra', 'iub_type': '', 'bandwidth': '', 'omip': '', 'iubip': ''},
        'FD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        'TD-LTE':   {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
        '5G':       {'bts_id': 'nodeid', 'cell_name': 'cell_name', 'cell_id': 'sac_ci_eutra', 'lac': 'lac_tac', 'pci': 'phy_cid', 'bandwidth': '', 'omip': '', 's1_c': '', 's1_u': '',},
    },
    'ALL': {
        'site_status': '', 'user': '', 'counterpart': '', 'remarks': ''
    }
};
const G_NMS_SRC_ACTIVITY = {
    'DEVICE': ['Rollout', 'BTS Swap'],
    'CELL': ['Rollout', 'Expansion', 'BTS Swap'],
    'TRX': ['Rollout', 'Expansion', 'TRX Expansion', 'BTS Swap', 'Site Reconfig']
}