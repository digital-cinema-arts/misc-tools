# development-tools
 Misc. scripts, applications and libraries for development and testing purposes.



Notes for the test_gatt.py script:


pi@pi-abcs:~/dev/bluetooth/abcs-muse $ sudo hciconfig 
hci1:	Type: Primary  Bus: UART
	BD Address: B8:27:EB:B3:DC:50  ACL MTU: 1021:8  SCO MTU: 64:1
	UP RUNNING PSCAN 
	RX bytes:1577 acl:0 sco:0 events:99 errors:0
	TX bytes:1893 acl:0 sco:0 commands:99 errors:0

hci0:	Type: Primary  Bus: USB
	BD Address: 00:1A:7D:DA:71:0A  ACL MTU: 310:10  SCO MTU: 64:8
	UP RUNNING PSCAN 
	RX bytes:1878 acl:0 sco:0 events:116 errors:0
	TX bytes:3109 acl:0 sco:0 commands:116 errors:1





#!/bin/bash

sudo hciconfig hci0 up

sudo hcitool leinfo  00:55:DA:B0:36:C2
sudo hcitool leinfo  00:55:DA:B0:51:41

sleep 5 

sudo hcitool lecc 00:55:DA:B0:36:C2
sudo hcitool lecc 00:55:DA:B0:51:41



#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-


from bluetooth.ble import DiscoveryService
 
service = DiscoveryService()
devices = service.discover(2)
 
for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))





pi@pi-abcs:~/dev/bluetooth $ 
pi@pi-abcs:~/dev/bluetooth $ sudo gatttool -I
[                 ][LE]> help
help                                           Show this help
exit                                           Exit interactive mode
quit                                           Exit interactive mode
connect         [address [address type]]       Connect to a remote device
disconnect                                     Disconnect from a remote device
primary         [UUID]                         Primary Service Discovery
included        [start hnd [end hnd]]          Find Included Services
characteristics [start hnd [end hnd [UUID]]]   Characteristics Discovery
char-desc       [start hnd] [end hnd]          Characteristics Descriptor Discovery
char-read-hnd   <handle>                       Characteristics Value/Descriptor Read by handle
char-read-uuid  <UUID> [start hnd] [end hnd]   Characteristics Value/Descriptor Read by UUID
char-write-req  <handle> <new value>           Characteristic Value Write (Write Request)
char-write-cmd  <handle> <new value>           Characteristic Value Write (No response)
sec-level       [low | medium | high]          Set security level. Default: low
mtu             <value>                        Exchange MTU for GATT/ATT
[                 ][LE]> connect 00:55:DA:B0:36:C2
Attempting to connect to 00:55:DA:B0:36:C2
Connection successful
[00:55:DA:B0:36:C2][LE]> help
help                                           Show this help
exit                                           Exit interactive mode
quit                                           Exit interactive mode
connect         [address [address type]]       Connect to a remote device
disconnect                                     Disconnect from a remote device
primary         [UUID]                         Primary Service Discovery
included        [start hnd [end hnd]]          Find Included Services
characteristics [start hnd [end hnd [UUID]]]   Characteristics Discovery
char-desc       [start hnd] [end hnd]          Characteristics Descriptor Discovery
char-read-hnd   <handle>                       Characteristics Value/Descriptor Read by handle
char-read-uuid  <UUID> [start hnd] [end hnd]   Characteristics Value/Descriptor Read by UUID
char-write-req  <handle> <new value>           Characteristic Value Write (Write Request)
char-write-cmd  <handle> <new value>           Characteristic Value Write (No response)
sec-level       [low | medium | high]          Set security level. Default: low
mtu             <value>                        Exchange MTU for GATT/ATT
[00:55:DA:B0:36:C2][LE]> characteristics
handle: 0x0002, char properties: 0x20, char value handle: 0x0003, uuid: 00002a05-0000-1000-8000-00805f9b34fb
handle: 0x0006, char properties: 0x4e, char value handle: 0x0007, uuid: 00002a00-0000-1000-8000-00805f9b34fb
handle: 0x0008, char properties: 0x4e, char value handle: 0x0009, uuid: 00002a01-0000-1000-8000-00805f9b34fb
handle: 0x000a, char properties: 0x0a, char value handle: 0x000b, uuid: 00002a04-0000-1000-8000-00805f9b34fb
handle: 0x000d, char properties: 0x14, char value handle: 0x000e, uuid: 273e0001-4c4d-454d-96be-f03bac821358
handle: 0x0010, char properties: 0x10, char value handle: 0x0011, uuid: 273e0008-4c4d-454d-96be-f03bac821358
handle: 0x0013, char properties: 0x10, char value handle: 0x0014, uuid: 273e0009-4c4d-454d-96be-f03bac821358
handle: 0x0016, char properties: 0x10, char value handle: 0x0017, uuid: 273e000a-4c4d-454d-96be-f03bac821358
handle: 0x0019, char properties: 0x10, char value handle: 0x001a, uuid: 273e000b-4c4d-454d-96be-f03bac821358
handle: 0x001c, char properties: 0x10, char value handle: 0x001d, uuid: 273e0002-4c4d-454d-96be-f03bac821358
handle: 0x001f, char properties: 0x10, char value handle: 0x0020, uuid: 273e0003-4c4d-454d-96be-f03bac821358
handle: 0x0022, char properties: 0x10, char value handle: 0x0023, uuid: 273e0004-4c4d-454d-96be-f03bac821358
handle: 0x0025, char properties: 0x10, char value handle: 0x0026, uuid: 273e0005-4c4d-454d-96be-f03bac821358
handle: 0x0028, char properties: 0x10, char value handle: 0x0029, uuid: 273e0006-4c4d-454d-96be-f03bac821358
handle: 0x002b, char properties: 0x10, char value handle: 0x002c, uuid: 273e0007-4c4d-454d-96be-f03bac821358
[00:55:DA:B0:36:C2][LE]> char-desc 00002a05-0000-1000-8000-00805f9b34fb
Error: Invalid start handle: 00002a05-0000-1000-8000-00805f9b34fb
[00:55:DA:B0:36:C2][LE]> char-desc  0x20
handle: 0x0020, uuid: 273e0003-4c4d-454d-96be-f03bac821358
handle: 0x0021, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0022, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0023, uuid: 273e0004-4c4d-454d-96be-f03bac821358
handle: 0x0024, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0025, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0026, uuid: 273e0005-4c4d-454d-96be-f03bac821358
handle: 0x0027, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0028, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0029, uuid: 273e0006-4c4d-454d-96be-f03bac821358
handle: 0x002a, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x002b, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x002c, uuid: 273e0007-4c4d-454d-96be-f03bac821358
handle: 0x002d, uuid: 00002902-0000-1000-8000-00805f9b34fb
[00:55:DA:B0:36:C2][LE]> char-read-uuid 00002a05-0000-1000-8000-00805f9b34fb
Error: Read characteristics by UUID failed: Attribute can't be read
[00:55:DA:B0:36:C2][LE]> char-read-uuid 00002a00-0000-1000-8000-00805f9b34fb
handle: 0x0007 	 value: 4d 75 73 65 2d 33 36 43 32 
[00:55:DA:B0:36:C2][LE]> 






