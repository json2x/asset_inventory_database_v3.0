import os
import sys, getopt
import django
import pandas as pd
import glob
import re
import datetime
import concurrent.futures
#from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool as Pool

from nmsdata.scripts.ran_access_loader import insertDevice, insertCell, insertTrx

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetInventory.settings')
django.setup()


#--FILE paths containing the csv files for Linux OS
NMS_DEVICES = '/home/jcm/mnt/RAN/RAN_DEVICE*'
NMS_CELLS = '/home/jcm/mnt/RAN/RAN_CELL*'
NMS_TRX = '/home/jcm/mnt/RAN/RAN_TRX*'


sys.path.append('/home/jcm/mnt/RAN')

#Multithreading
def MultithreadTableUpdate(chunksize, nmspath, functionName):
    df = pd.read_csv(getLatestFile(nmspath),low_memory=False)
    df_range = len(df.index)//chunksize + 1

    print('Df size:', df.index)
    print('Df split count:', chunksize)
    print('Df chunk size:', df_range)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        dfs = []
        for i in range(chunksize):
            if i == (chunksize-1):
                dfs.append(df.iloc[i*df_range:])
            else:
                start = i*df_range
                end = start + df_range
                dfs.append(df.iloc[start:end])
            
        executor.map(functionName, dfs)
        executor.shutdown(wait=True)

#Multiprocessing
def MultiprocessTableUpdate(chunksize, nmspath, functionName):
    df = pd.read_csv(getLatestFile(nmspath),low_memory=False)
    df_range = len(df.index)//chunksize + 1

    print('Df size:', len(df.index))
    print('Df split count:', chunksize)
    print('Df chunk size:', df_range)
    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:
        dfs = []
        #failed_rows = {}
        processes = [ 
            executor.submit(functionName, df.iloc[i*df_range:]) if i == chunksize-1 \
            else executor.submit(functionName,  df.iloc[i*df_range:(i*df_range)+df_range]) \
            for i in range(chunksize)
        ]

        # for i in range(chunksize):
        #     if i == chunksize-1:
        #         dfs.append(df.iloc[i*df_range:])
        #     else:
        #         start = i*df_range
        #         end = start + df_range
        #         dfs.append(df.iloc[start:end])
        
        # processes = executor.map(functionName, dfs)

        # if concurrent.futures.wait(processes):
        #     print(failed_rows)
        for process in concurrent.futures.as_completed(processes):
            process.result()
        # for process in concurrent.futures.as_completed(processes):
        #     failed_rows.update(process.result())
        # print(failed_rows)

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
        opts, args = getopt.getopt(sys.argv[1:],"ht:c:",["type=", "chunksize="])
        if len(opts) > 0:
            type = None;help = False;chunksize = None

            for opt, arg in opts:
                if opt=='-h':
                    help = True
                elif opt in ('-t', '--type'):
                    type = arg
                elif opt in ('-c', '--chunksize'):
                    chunksize = int(arg)

            if type=='device':
                if chunksize:
                    try:
                        # call thread creator
                        #MultithreadTableUpdate(int(chunksize), NMS_DEVICES, insertDevice)
                        MultiprocessTableUpdate(int(chunksize), NMS_DEVICES, insertDevice)
                    except Exception as e:
                        #call insertdevice
                        print("Error {}.".format(e))
                else:
                    print("Loading RAN DEVICE to nmsdata_device table")
                    insertDevice(pd.read_csv(getLatestFile(NMS_DEVICES),low_memory=False))

            elif type=='cell':
                if chunksize:
                    try:
                        # call thread creator
                        #MultithreadTableUpdate(int(chunksize), NMS_CELLS, insertCell)
                        MultiprocessTableUpdate(int(chunksize), NMS_CELLS, insertCell)
                    except Exception as e:
                        #call insertdevice
                        print("Error {}.".format(e))
                else:
                    #call insertCell
                    print("Loading RAN CELL to msdata_cell table")
                    insertCell(pd.read_csv(getLatestFile(NMS_CELLS),low_memory=False))

            elif type=='trx':
                if chunksize:
                    try:
                        # call thread creator
                        #MultithreadTableUpdate(int(chunksize), NMS_TRX, insertTrx)
                        MultiprocessTableUpdate(int(chunksize), NMS_TRX, insertTrx)
                    except Exception as e:
                        #call insertdevice
                        print("Error {}.".format(e))
                else:
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
        print("Format 2: test.py -t <option> -c <chunksize>")
        print("Options for -t are : device|cell|trx")

    endTime = datetime.datetime.now()
    deltaDt = endTime - starTime
    print(deltaDt)
    print("---END OF SCRIPT---")
