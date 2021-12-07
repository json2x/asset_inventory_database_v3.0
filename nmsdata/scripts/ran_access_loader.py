#NMS DATA LOADER
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetInventory.settings')
django.setup()

from nmsdata.models import Device, Cell, Trx
from django.db import connection
import pandas as pd
import re

#Update or insert rows - Device table.
#---------------------------
def insertDevice(df):
    Device.objects.filter(record_status = 1).update(record_status = 0)

    #--Rename device column name to match nms data model
    #--update_or_create method requires matching column names
    device_column_name = {
        'DN': 'dn',
        'DEVICE_ID': 'device_id',
        'EMS_DEVICE_ID': 'ems_device_id',
        'DEVICE_ALIAS': 'device_alias',
        'DEVICE_IP': 'device_ip',
        'EMS_ID': 'ems_id',
        'VENDOR_ID': 'vendor_id',
        'NE_TYPE': 'ne_type',
        'MODEL': 'model',
        'HW_DESC': 'hardware_description',
        'FNC_DESC': 'functional_description',
        'PARENT_ID': 'parent_device_id',
        'PARENT_DN': 'parentdn',
        'SITE_ID': 'site_id',
        'DEVICE_STATE': 'device_state',
        'SW_VER': 'software_version',
        'INT_DATE': 'integration_date',
        'EOS': 'end_of_support',
        'TSA_SCOPE': 'tsa_scope',
        'PROD_ID': 'product_id',
        'SERIAL_NO': 'serial_number',
        'FREQ_TXRX': 'freq_tx_rx_field',
        'HW_CAP': 'hardware_capacity',
        'DOMAIN': 'domain',
        'NE_OWNER': 'ne_owner',
        'TX_CLUSTER': 'tx_clusterimg',
        'TX_TYPE': 'tx_type',
        'NAT_SP_CODE': 'natspcode',
        'ADMIN_STATE': 'admin_state',
        'SUBDOMAIN': 'subdomain',
        'FUNCTION': 'function',
        'IUBCE_DL_LIC': 'iubce_dl_lic',
        'IUBCE_UL_LIC': 'iubce_ul_lic',
        'S1CU_LIC': 's1cu_lic'
    }
    df.rename(columns = device_column_name, inplace = True)

    #--Read nmsdata_device table
    dict_logs = {}
    for i, row in df.iterrows():
        update_device = row.to_dict()
        update_device["record_status"] = 1

        try:
            device, created = Device.objects.update_or_create(
                dn = row["dn"],
                device_id = row["device_id"],
                ems_id = row["ems_id"],
                subdomain = row["subdomain"],
                defaults = update_device,
            )
            str_create_update = "Inserted" if created else "Updated"
            print("{} {} {} {}".format(str_create_update, device.ems_id, device.device_id, device.subdomain), flush=True)

        except Exception as e:
             dict_logs[i] = update_device.values()

    #append logs
    #print(dict_logs, flush=True)
    return dict_logs
    # df_logs = pd.DataFrame.from_dict(dict_logs, orient = 'index', columns = update_device.keys())
    # df_logs.to_csv("failed_update_or_create_device.csv", index = False)

#Update or insert rows - Cell table.
#---------------------------
def insertCell(df):
    Cell.objects.filter(record_status = 1).update(record_status = 0)

    #--Rename cell column name to match nmsdata_cell model
    #--update_or_create method requires matching column names
    cell_column_name = {
        'EMS_CELL_ID': 'ems_cell_id',
        'EMS_ID': 'ems_id',
        'CELL_NAME': 'cell_name',
        'DN': 'dn',
        'SITE_ID': 'site',
        'PARENT_ID': 'parent_id',
        'PARENT_DN': 'parent_dn',
        'TECH': 'tech',
        'BAND': 'band',
        'ADMIN_STATE': 'admin_state',
        'ALIAS': 'alias',
        'LAC_TAC': 'lac_tac',
        'SAC_CI_EUTRA': 'sac_ci_eutra',
        'RNC_CID': 'rnc_cid',
        'PHY_CID': 'phy_cid',
        'LCR_CID': 'lcr_cid',
        'MCC': 'mcc',
        'MNC': 'mnc',
        'NODEID': 'nodeid',
        'SECTOR_ID': 'sector_id',
        'CARRIER': 'carrier',
        'NE_TYPE': 'ne_type',
        'SUBDOMAIN': 'subdomain',
        'FUNCTION': 'function',
        'SDCCH_CAP': 'sdcch_cap',
        'TCH_CAP': 'tch_cap',
        'HOMING_ID': 'homing_id',
        'DLEARFCN': 'dlear_fcn',
        'ULEARFCN': 'ulear_dcn',
        'DLCHBW': 'dlc_hbw',
        'ULCHBW': 'ulc_hbw',
        'RAC': 'rac',
        'NCC': 'ncc',
        'BCC': 'bcc',
        'NNODEID': 'nnode_id',
        'NBSCID': 'nbscid',
        'PSC': 'psc',
        'BCCHNO': 'bcchno'
    }
    df.rename(columns = cell_column_name, inplace = True)

    #--Read nmsdata_cell table
    dict_logs = {}
    for i, row in df.iterrows():
        update_cell = row.to_dict()
        update_cell["record_status"] = 1

        try:
            cell, created = Cell.objects.update_or_create(
                ems_id = row["ems_id"],
                cell_name = row["cell_name"],
                parent_id = row["parent_id"],
                band = row["band"],
                subdomain = row["subdomain"],
                defaults = update_cell,
            )
            str_create_update = "Inserted" if created else "Updated"
            print("{} {} {} {} {} {}".format(str_create_update, cell.ems_id, cell.cell_name, cell.parent_id, cell.band,cell.subdomain), flush=True)

        except Exception as e:
             dict_logs[i] = update_cell.values()

    #append logs
    #print(dict_logs, flush=True)
    return dict_logs
    # df_logs = pd.DataFrame.from_dict(dict_logs, orient = 'index', columns = update_cells.keys())
    # df_logs.to_csv("failed_update_or_create_cell.csv", index = False)

#Update or insert rows - Trx table.
#---------------------------
def insertTrx(df):
    Trx.objects.filter(record_status = 1).update(record_status = 0)

    #--Rename trx column name to match nmsdata_trx model
    #--update_or_create method requires matching column names
    trx_column_name = {
        'EMS_TRX_ID': 'ems_trx_id',
        'EMS_ID': 'ems_id',
        'TRX_NAME': 'trx_name',
        'DN': 'dn',
        'SITE_ID': 'site_id',
        'PARENT_ID': 'parent_id',
        'PARENT_DN': 'parent_dn',
        'ADMIN_STATE': 'admin_state',
        'E1_ASSIGNMENT': 'e1_assignment',
        'HOMING_BTS': 'homing_bts',
        'HOMING_ID': 'homing_id',
        'TRXFREQ': 'trxfreq'
    }
    df.rename(columns = trx_column_name, inplace = True)

    #--Read nmsdata_trx table
    dict_logs = {}
    for i, row in df.iterrows():
        update_trx = row.to_dict()
        update_trx["record_status"] = 1

        try:
            trx, created = Trx.objects.update_or_create(
                ems_id = row["ems_id"],
                trx_name = row["trx_name"],
                parent_id = row["parent_id"],
                defaults = update_trx,
            )
            str_create_update = "Inserted" if created else "Updated"
            print("{} {} {} {}".format(str_create_update, trx.ems_id, trx.trx_name, trx.parent_id), flush=True)

        except Exception as e:
             dict_logs[i] = update_trx.values()

    #append logs
    #print(dict_logs, flush=True)
    return dict_logs
    # df_logs = pd.DataFrame.from_dict(dict_logs, orient = 'index', columns = update_trx.keys(), flush=True)
    # df_logs.to_csv("failed_update_or_create_trx.csv", index = False)
