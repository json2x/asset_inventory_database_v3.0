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
    #--Set record status back to '0' before insert or update
    Device.objects.filter(record_status=1).update(record_status=0)

    #--Read nmsdata_device table
    sql = pd.read_sql('SELECT id, ems_id, dn, device_id, subdomain FROM nmsdata_device', connection)
    for i, row in df.iterrows():
        search=sql[(sql.ems_id==row["EMS_ID"]) & (sql.dn==row["DN"]) & (sql.device_id==row["DEVICE_ID"])
         & (sql.subdomain==row["SUBDOMAIN"])]
        if not search.empty:
            if len(search.index) > 1:
                # if greater than 1 == log
                print('Match more than 1 record. Devices wont be updated.')
                print(search)
            else:
                # update
                updateDevice = Device.objects.get(id=search.iloc[0]['id'])
                updateDevice.dn=row["DN"]
                updateDevice.device_id=row["DEVICE_ID"]
                updateDevice.ems_device_id=row["EMS_DEVICE_ID"]
                updateDevice.device_alias=row["DEVICE_ALIAS"]
                updateDevice.device_ip=row["DEVICE_IP"]
                updateDevice.ems_id=row["EMS_ID"]
                updateDevice.vendor_id=row["VENDOR_ID"]
                updateDevice.ne_type=row["NE_TYPE"]
                updateDevice.model=row["MODEL"]
                updateDevice.hardware_description=row["HW_DESC"]
                updateDevice.functional_description=row["FNC_DESC"]
                updateDevice.parent_device_id=row["PARENT_ID"]
                updateDevice.parentdn=row["PARENT_DN"]
                updateDevice.site_id=row["SITE_ID"]
                updateDevice.device_state=row["DEVICE_STATE"]
                updateDevice.software_version=row["SW_VER"]
                updateDevice.integration_date=row["INT_DATE"]
                updateDevice.end_of_support=row["EOS"]
                updateDevice.tsa_scope=row["TSA_SCOPE"]
                updateDevice.product_id=row["PROD_ID"]
                updateDevice.serial_number=row["SERIAL_NO"]
                updateDevice.freq_tx_rx_field=row["FREQ_TXRX"]
                updateDevice.hardware_capacity=row["HW_CAP"]
                updateDevice.domain=row["DOMAIN"]
                updateDevice.ne_owner=row["NE_OWNER"]
                updateDevice.tx_clustering=row["TX_CLUSTER"]
                updateDevice.tx_type=row["TX_TYPE"]
                updateDevice.natspcode=row["NAT_SP_CODE"]
                updateDevice.admin_state=row["ADMIN_STATE"]
                updateDevice.subdomain=row["SUBDOMAIN"]
                updateDevice.function=row["FUNCTION"]
                updateDevice.iubce_dl_lic=row["IUBCE_DL_LIC"]
                updateDevice.iubce_ul_lic=row["IUBCE_UL_LIC"]
                updateDevice.s1cu_lic=row["S1CU_LIC"]
                updateDevice.record_status=1

                updateDevice.save()
                print("Updated {} {} {}".format(updateDevice.ems_id,updateDevice.device_id,updateDevice.subdomain))

        else:
            # insert
            insertDevice = Device(
                dn=row["DN"],
                device_id=row["DEVICE_ID"],
                ems_device_id=row["EMS_DEVICE_ID"],
                device_alias=row["DEVICE_ALIAS"],
                device_ip=row["DEVICE_IP"],
                ems_id=row["EMS_ID"],
                vendor_id=row["VENDOR_ID"],
                ne_type=row["NE_TYPE"],
                model=row["MODEL"],
                hardware_description=row["HW_DESC"],
                functional_description=row["FNC_DESC"],
                parent_device_id=row["PARENT_ID"],
                parentdn=row["PARENT_DN"],
                site_id=row["SITE_ID"],
                device_state=row["DEVICE_STATE"],
                software_version=row["SW_VER"],
                integration_date=row["INT_DATE"],
                end_of_support=row["EOS"],
                tsa_scope=row["TSA_SCOPE"],
                product_id=row["PROD_ID"],
                serial_number=row["SERIAL_NO"],
                freq_tx_rx_field=row["FREQ_TXRX"],
                hardware_capacity=row["HW_CAP"],
                domain=row["DOMAIN"],
                ne_owner=row["NE_OWNER"],
                tx_clusterimg=row["TX_CLUSTER"],
                tx_type=row["TX_TYPE"],
                natspcode=row["NAT_SP_CODE"],
                admin_state=row["ADMIN_STATE"],
                subdomain=row["SUBDOMAIN"],
                function=row["FUNCTION"],
                iubce_dl_lic=row["IUBCE_DL_LIC"],
                iubce_ul_lic=row["IUBCE_UL_LIC"],
                s1cu_lic=row["S1CU_LIC"],
                record_status=1
            )
            insertDevice.save()
            print("Inserted {} {} {}".format(insertDevice.ems_id,insertDevice.device_id,insertDevice.subdomain))


#Update or insert rows - Cell table.
#---------------------------
def insertCell(df):
    #--Set record status back to '0' before insert or update
    Cell.objects.filter(record_status=1).update(record_status=0)
    
    #--Read nmsdata_cell table
    sql = pd.read_sql('SELECT id, ems_id, dn, cell_name, parent_id, band, subdomain FROM nmsdata_cell', connection)
    for i, row in df.iterrows():
        search=sql[(sql.ems_id==row["EMS_ID"]) & (sql.dn==row["DN"]) & (sql.cell_name==row["CELL_NAME"])
         & (sql.parent_id==row["PARENT_ID"]) & (sql.subdomain==row["SUBDOMAIN"])]
         
        band_formatted = re.search(r'\d+',str(row["BAND"]))
        band_formatted = band_formatted.group()
        if band_formatted == '':
            band_formatted = str(row["BAND"])

        if not search.empty:
            if len(search.index) > 1:
                # if greater than 1 == log
                print('Match more than 1 record. Cell wont be updated.')
                print(search)
            else:
                # update
                updateCell = Cell.objects.get(id=search.iloc[0]['id'])
                updateCell.ems_cell_id=row["EMS_CELL_ID"]
                updateCell.ems_id=row["EMS_ID"]
                updateCell.cell_name=row["CELL_NAME"]
                updateCell.dn=row["DN"]
                updateCell.site=row["SITE_ID"]
                updateCell.parent_id=row["PARENT_ID"]
                updateCell.parent_dn=row["PARENT_DN"]
                updateCell.tech=row["TECH"]
                updateCell.band=band_formatted
                updateCell.admin_state=row["ADMIN_STATE"]
                updateCell.alias=row["ALIAS"]
                updateCell.lac_tac=row["LAC_TAC"]
                updateCell.sac_ci_eutra=row["SAC_CI_EUTRA"]
                updateCell.rnc_cid=row["RNC_CID"]
                updateCell.phy_cid=row["PHY_CID"]
                updateCell.lcr_cid=row["LCR_CID"]
                updateCell.mcc=row["MCC"]
                updateCell.mnc=row["MNC"]
                updateCell.nodeid=row["NODEID"]
                updateCell.sector_id=row["SECTOR_ID"]
                updateCell.carrier=row["CARRIER"]
                updateCell.ne_type=row["NE_TYPE"]
                updateCell.subdomain=row["SUBDOMAIN"]
                updateCell.function=row["FUNCTION"]
                updateCell.sdcch_cap=row["SDCCH_CAP"]
                updateCell.tch_cap=row["TCH_CAP"]
                updateCell.homing_id=row["HOMING_ID"]
                updateCell.dlear_fcn=row["DLEARFCN"]
                updateCell.ulear_dcn=row["ULEARFCN"]
                updateCell.dlc_hbw=row["DLCHBW"]
                updateCell.ulc_hbw=row["ULCHBW"]
                updateCell.rac=row["RAC"]
                updateCell.ncc=row["NCC"]
                updateCell.bcc=row["BCC"]
                updateCell.nnode_id=row["NNODEID"]
                updateCell.nbscid=row["NBSCID"]
                updateCell.psc=row["PSC"]
                updateCell.bcchno=row["BCCHNO"]
                updateCell.record_status=1

                updateCell.save()
                print("Updated {} {} {} {} {}".format(updateCell.ems_id,updateCell.cell_name, \
                    updateCell.parent_id, updateCell.band,updateCell.subdomain))

        else:
            # insert
            insertCell = Cell(
                ems_cell_id=row["EMS_CELL_ID"],
                ems_id=row["EMS_ID"],
                cell_name=row["CELL_NAME"],
                dn=row["DN"],
                site=row["SITE_ID"],
                parent_id=row["PARENT_ID"],
                parent_dn=row["PARENT_DN"],
                tech=row["TECH"],
                band=band_formatted,
                admin_state=row["ADMIN_STATE"],
                alias=row["ALIAS"],
                lac_tac=row["LAC_TAC"],
                sac_ci_eutra=row["SAC_CI_EUTRA"],
                rnc_cid=row["RNC_CID"],
                phy_cid=row["PHY_CID"],
                lcr_cid=row["LCR_CID"],
                mcc=row["MCC"],
                mnc=row["MNC"],
                nodeid=row["NODEID"],
                sector_id=row["SECTOR_ID"],
                carrier=row["CARRIER"],
                ne_type=row["NE_TYPE"],
                subdomain=row["SUBDOMAIN"],
                function=row["FUNCTION"],
                sdcch_cap=row["SDCCH_CAP"],
                tch_cap=row["TCH_CAP"],
                homing_id=row["HOMING_ID"],
                dlear_fcn=row["DLEARFCN"],
                ulear_dcn=row["ULEARFCN"],
                dlc_hbw=row["DLCHBW"],
                ulc_hbw=row["ULCHBW"],
                rac=row["RAC"],
                ncc=row["NCC"],
                bcc=row["BCC"],
                nnode_id=row["NNODEID"],
                nbscid=row["NBSCID"],
                psc=row["PSC"],
                bcchno=row["BCCHNO"],
                record_status=1
            )
            insertCell.save()
            print("Inserted {} {} {} {} {}".format(insertCell.ems_id, insertCell.cell_name, \
                insertCell.parent_id, insertCell.band,insertCell.subdomain))

#Update or insert rows - Trx table.
#---------------------------
def insertTrx(df):
    #--Set record status back to '0' before insert or update
    Trx.objects.filter(record_status=1).update(record_status=0)
    
    #--Read nmsdata_trx table
    sql = pd.read_sql('SELECT id, ems_id, trx_name, parent_id, homing_bts, homing_id FROM nmsdata_trx', connection)
    for i, row in df.iterrows():
        search=sql[(sql.ems_id==row["EMS_ID"]) & (sql.trx_name==row["TRX_NAME"]) & (sql.parent_id==row["PARENT_ID"])
         & (sql.homing_bts==row["HOMING_BTS"]) & (sql.homing_id==row["HOMING_ID"])]
        if not search.empty:
            if len(search.index) > 1:
                # if greater than 1 == log
                print('Match more than 1 record. Trx wont be updated.')
                print(search)
            else:
                # update
                updateTrx = Trx.objects.get(id=search.iloc[0]['id'])
                updateTrx.ems_trx_id=row["EMS_TRX_ID"]
                updateTrx.ems_id=row["EMS_ID"]
                updateTrx.trx_name=row["TRX_NAME"]
                updateTrx.dn=row["DN"]
                updateTrx.site_id=row["SITE_ID"]
                updateTrx.parent_id=row["PARENT_ID"]
                updateTrx.parent_dn=row["PARENT_DN"]
                updateTrx.admin_state=row["ADMIN_STATE"]
                updateTrx.e1_assignment=row["E1_ASSIGNMENT"]
                updateTrx.homing_bts=row["HOMING_BTS"]
                updateTrx.homing_id=row["HOMING_ID"]
                updateTrx.trxfreq=row["TRXFREQ"]
                updateTrx.record_status=1

                updateTrx.save()
                print("Updated {} {} {}".format(updateTrx.ems_id, updateTrx.trx_name, updateTrx.parent_id))
        else:
            # insert
            insertTrx = Trx(
                ems_trx_id=row["EMS_TRX_ID"],
                ems_id=row["EMS_ID"],
                trx_name=row["TRX_NAME"],
                dn=row["DN"],
                site_id=row["SITE_ID"],
                parent_id=row["PARENT_ID"],
                parent_dn=row["PARENT_DN"],
                admin_state=row["ADMIN_STATE"],
                e1_assignment=row["E1_ASSIGNMENT"],
                homing_bts=row["HOMING_BTS"],
                homing_id=row["HOMING_ID"],
                trxfreq=row["TRXFREQ"],
                record_status=1
            )
            insertTrx.save()
            print("Inserted {} {} {}".format(insertTrx.ems_id, insertTrx.trx_name, insertTrx.parent_id))


