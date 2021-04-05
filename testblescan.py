# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

import bluetooth._bluetooth as bluez

import time
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	#print "----------"
	for beacon in returnedList:
            mac_addr = beacon.split(',')
            if "00:c0:b1:c0:2a:d5"  in  mac_addr[0] :
                    print(beacon)
					#print((float(-58-int(mac_addr[5]))/20))
					print(round(10**(float(-69-int(mac_addr[5]))/20),2))
                    #print(mac_addr[0])
                    #print('finds')
			if "00:c0:b1:c0:2a:d5"  in  mac_addr[0] or "00:c0:b1:c0:2a:d8"  in  mac_addr[0]:
				    #print(beacon)
					#print(mac_addr[5])
					#print('finds')