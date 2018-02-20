#!/usr/bin/env python2

#author : Kade Cooper kaco0964@colorado.edu
#name : terminalFunctions.py
#purpose : File for all teammember to put in modular code. As the file grows we can separate the longer functions into separate files
#date : 2018.02.19
#version: 1.0.8
#version notes (latest): Compatible w/ python2

#Native Python Modules
import os
import sys
import time
#import thread
import subprocess
import csv
from multiprocessing import Process

#This will alert the end tester that the build environment for the hackrf is not present
try:
    from sdr_modules.wifi_rx_rftap import tuneWifi
except ImportError:
    print ("The GnuRadio dependencies are not present in this app! Talk to Pieter/Carlos...")


""" 1. Scan Network - Ensure our antenna can RX Data """

def scanNetwork():

    #Emulate Scan Function
    print("\n\t Running Network Scan w/ HackRF... \n")
    print("\n\t If you wish to quit, press Ctrl C or ^C... \n")
    try:
        #Below is the actual function to run the HackRF
        #tuneWifi.main()
        cli_process = Process(target=cli_progress, args=(101, 20))
        cli_process.start()
        scan_process = Process(target=check_csv_file)
        scan_process.start()
        #Wait until finished
        scan_process.join()
        cli_process.join()
        
        print("\n\t Results saved locally! Can be accessed by Option 2 on the command line... \n")
    except KeyboardInterrupt:
        print("\nscanNetwork: User stopped scan!!! Partial Data saved. Press enter to return to main program.")
    

""" 2. Display Network Data - Interactive Graphs & Statistics """

def displayNetworkData():
    print("\t Graphs Here \n")

""" 3. Decode Network Data - Scan, capture, parse various network protocols """

def decodeNetworkData():
    print("\t BeepBoopBeep\n")

""" 4. View Database - View saved network data """

def viewDatabase():
    print("\t MySQL \n")

""" 5. Test Summary - Provide quick network/system checks in an easy to read format """

def sdrWifiTests():
    wifi_return_code = subprocess.checkoutput("")
    #If wifi_return_code is true than a wireless service has been turned off
    if (wifi_return_code):
        print("\t Wifi: {} \n".format(passedCheck))
    else:
        passedCheck="On"
        print("\t Wifi: {} \n".format(passedCheck))

def sdrBluetoothTests():
    print("\t BlueTooth: {} \n".format(passedCheck))


def testSummary():

    passedCheck = "Off"
    
    print("SDR Hardware Check: \n")
    sdrWifiTests(passedCheck)
    sdrBluetoothTests(passedCheck)
    print("\t ZigBee: {} \n".format(passedCheck))
    print("\t GSM: {} \n".format(passedCheck))
    print("Systems Check: \n")
    print("\t Antenna RX: {} \n".format(passedCheck))
    print("\t Antenna TX: {} \n".format(passedCheck))
    print("\t Sample Packet Decode: {} \n".format(passedCheck))
    

    print("System Hardware Check: \n")
    print("\t Wifi: {} \n".format(passedCheck))
    print("\t Bluetooth: {} \n".format(passedCheck))
    print("\t Database: {} \n".format(passedCheck))
    
""" 6. Settings Page - Save user preferences & configurations for network data manipulation """

def settingsPage():
    print("\t ;)  \n")


"""###########################################
########## SYSTEM OUTPUT SECTION ##########
###############################################"""

def check_csv_file():
    if not os.path.isfile('./network_scan_output/hackRFTestOutput.csv'):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
    else:
        with open('./network_scan_output/hackRFTestOutput.csv') as csvFile:
            #Use csv parser
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                print(row)

def cli_progress(end_val, bar_length):
    for i in xrange(0, end_val):
        percent = float(i) / end_val
        hashes = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(hashes))
        #Emulate progress...
        time.sleep(0.1)
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()
    print("\n")
