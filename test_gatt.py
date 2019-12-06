#!/usr/bin/env python

import pygatt
import bitstring
import logging
from time import time, sleep, strftime, gmtime, localtime
from binascii import hexlify

MUSE_GATT_ATTR_STREAM_TOGGLE = '273e0001-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_TP9 = '273e0003-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_AF7 = '273e0004-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_AF8 = '273e0005-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_TP10 = '273e0006-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_RIGHTAUX = '273e0007-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_GYRO = '273e0009-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_ACCELEROMETER = '273e000a-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_TELEMETRY = '273e000b-4c4d-454d-96be-f03bac821358'
MUSE_GATT_ATTR_PPG1 = "273e000f-4c4d-454d-96be-f03bac821358"
MUSE_GATT_ATTR_PPG2 = "273e0010-4c4d-454d-96be-f03bac821358"
MUSE_GATT_ATTR_PPG3 = "273e0011-4c4d-454d-96be-f03bac821358"

# Change these MAC addresses to the Muse headbands you life to connect to

address1 = '00:55:DA:B0:51:41'
address2 = '00:55:DA:B0:36:C2'


def callback_func(handle, rawData):
    binaryData = '{}'.format(hexlify(str(rawData)))
    print("callback_func() - binaryData: ", binaryData)
#     wait_for_interrupt = False
    bit_decoder = bitstring.Bits(bytes=rawData)
    pattern = "uint:16,uint:16,uint:16,uint:16,uint:16"  # The rest is 0 padding
    data = bit_decoder.unpack(pattern)

    battery = data[1] / 512
    fuel_gauge = data[2] * 2.2
    adc_volt = data[3]
    temperature = data[4]
        
    print ("callback_func() - battery: ", battery)
    print ("callback_func() - fuel_gauge: ", fuel_gauge)
    print ("callback_func() - adc_volt: ", adc_volt)
    print ("callback_func() - temperature: ", temperature)




date_time_now = strftime('%Y-%m-%d-%H.%M.%S', gmtime())
log_filename = './gatt-test.log'
                    
                    
# DEBUG INFO  WARNING  ERROR  CRITICAL 
logging.basicConfig(filename=log_filename, 
                    format='%(asctime)s - %(message)s', 
                    level=logging.DEBUG)
logging.getLogger('pygatt').setLevel(logging.DEBUG)

adapter1 = pygatt.GATTToolBackend('hci0')
adapter2 = pygatt.GATTToolBackend('hci0')

                
while True:

    try:

        adapter1.start()
        adapter2.start()
    
        num_tries = 9
        
        while num_tries > 0:
            print("Trying to connect to first Muse")
        #     device1 = adapter1.connect(address1, timeout=30, address_type=pygatt.BLEAddressType.random)
            device1 = adapter1.connect(address1, timeout=10)
            value1 = device1.subscribe(MUSE_GATT_ATTR_TELEMETRY, callback=callback_func)

            print("First Muse: ", device1)

            if device1:
                cmd = [0x02, 0x64, 0x0a]
                print("First Muse: ", cmd)
                device1.char_write_handle(0x000e, cmd, False)    
                cmd = [0x02, 0x73, 0x0a]        
                print("First Muse: ", cmd)
                device1.char_write_handle(0x000e, cmd, False)  
                cmd = [0x03, 0x76, 0x31, 0x0a]  
                print("First Muse: ", cmd)
                device1.char_write_handle(0x000e, cmd, False)  
                break
            
            num_tries = num_tries - 1

        num_tries = 9
        
        while num_tries > 0:
            print("Trying to connect to second Muse")

        #     device2 = adapter1.connect(address2, timeout=30, address_type=pygatt.BLEAddressType.random)
            device2 = adapter2.connect(address2, timeout=10)
            value2 = device2.subscribe(MUSE_GATT_ATTR_TELEMETRY, callback=callback_func)

            print("Second Muse: ", device2)

            if device2:
                cmd = [0x02, 0x64, 0x0a]
                print("Second Muse: ", cmd)
                device2.char_write_handle(0x000e, cmd, False)
                cmd = [0x02, 0x73, 0x0a]        
                print("Second Muse: ", cmd)
                device2.char_write_handle(0x000e, cmd, False)
                cmd = [0x03, 0x76, 0x31, 0x0a]  
                print("Second Muse: ", cmd)
                device2.char_write_handle(0x000e, cmd, False)
                break

            num_tries = num_tries - 1

        if device1 and device2:
            break
            
            
    except pygatt.exceptions.BLEError as error:
            print("error", error)
            adapter1.stop()
            adapter2.stop()


wait_for_interrupt = True

while wait_for_interrupt:

    try:
    
        print("Waiting for telemetry interrupt")
        sleep(60)
    
        cmd = [0x02, 0x6b, 0x0a]
        device1.char_write_handle(0x000e, cmd, False)
        print("Sent keep alive to First Muse: ", cmd)

        device2.char_write_handle(0x000e, cmd, False)
        print("Sent keep alive to Second Muse: ", cmd)

    except pygatt.exceptions.BLEError as error:
            print("BLE error", error)
            adapter1.stop()
            adapter2.stop()

    except pygatt.exceptions.NotConnectedError as error:
            print("Not coonnected error", error)
            adapter1.stop()
            adapter2.stop()


adapter1.stop()
adapter2.stop()

print("Done")
