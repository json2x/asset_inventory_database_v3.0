import os
import sys, getopt
import django
import pandas as pd
import glob
import re
import datetime

from nmsdata.scripts.ran_access_loader import insertDevice, insertCell, insertTrx

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetInventory.settings')
django.setup()


#--FILE paths containing the csv files for Linux OS
NMS_DEVICES = '/home/jcm/mnt/RAN/RAN_DEVICE*'
NMS_CELLS = '/home/jcm/mnt/RAN/RAN_CELL*'
NMS_TRX = '/home/jcm/mnt/RAN/RAN_TRX*'


sys.path.append('/home/jdortaliz/ovim_asset_inventory_database')

#Obtain filepath of the latest csv.
#---------------------------
def getLatestFile(filePath):
    print("Getting Latest File from",filePath)
    list_of_files = glob.glob(filePath)
    latest_file = max(list_of_files, key=os.path.getctime)
    print("Latest file:",latest_file)
    
    return latest_file


if __name__ == "__main__":
    starTime = datetime.datetime.now()
    print("---START OF SCRIPT---")
    print("--------")
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ht:",["type="])
        if len(opts) > 0:
            type = None;help = False
          
            for opt, arg in opts:
                if opt=='-h':
                    help = True
                elif opt in ('-t', '--type'):
                    type = arg

            if type=='device':
                #call insertDevice
                print("Loading RAN DEVICE to nmsdata_device table")
                insertDevice(pd.read_csv(getLatestFile(NMS_DEVICES),low_memory=False))
            elif type=='cell':
                #call insertCell
                print("Loading RAN CELL to msdata_cell table")
                insertCell(pd.read_csv(getLatestFile(NMS_CELLS),low_memory=False))
            elif type=='trx':
                #call insertTrx
                print("Loading RAN TRX to nmsdata_trx table")
                insertTrx(pd.read_csv(getLatestFile(NMS_TRX),low_memory=False))

            elif help:
                print("help:")
                print("Format: test.py -t <option>")
                print("Options are : device|cell|trx")
                print("")
            
            else:
                print("Invalid argument")
                print("Argument options:")
                print(" -t Type of option required. Options are : device|cell|trx")
                sys.exit('Required argument missing')
        else:
            sys.exit('Input required')

    except getopt.GetoptError:
        print("Invalid argument")
        print("Format: test.py -t <option>")
        print("Options are : device|cell|trx")

    endTime = datetime.datetime.now()
    deltaDt = endTime - starTime
    print(deltaDt)
    print("---END OF SCRIPT---")
