#!/usr/bin/env python

'''

This script will reroute OSC messages and parse them out for use in Neuromore


'''

import sys, os
import argparse
from time import time, sleep, strftime, gmtime
import logging
import numpy as np

# OSC 
from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer, ServerClass
from oscpy.client import send_message, send_bundle
# from oscpy.server import OSCThreadServer
from oscpy import __version__

# Import MIDI library
import mido



osc_server_addr = '127.0.0.1'
# osc_server_addr = '192.168.1.123'
osc_server_port = 5001
osc_client_addr = '127.0.0.1'
# osc_client_addr = '192.168.1.123'
osc_client_port = 5022

osc_client = 0
osc_server = 0

def callback_ping(val1):
#     print("Data values: {}".format(val1))
    
    global osc_client
    osc_client.send_message(b'/ping', [val1], safer=True)



def callback_route_data(val1, val2, val3, val4, val5):
#     print("Data values: {}".format(val1), " {}".format(val2), 
#             " {}".format(val3), " {}".format(val4), " {}".format(val5))

    global osc_client

    osc_client.send_message(b'/muse/eeg0', [val1], safer=True)                                                   
    osc_client.send_message(b'/muse/eeg1', [val2], safer=True)                                                   
    osc_client.send_message(b'/muse/eeg2', [val3], safer=True)                                                   
    osc_client.send_message(b'/muse/eeg3', [val4], safer=True)                                                   
    osc_client.send_message(b'/muse/eeg4', [val5], safer=True)                                                   




def route_OSC_data(osc_client, osc_server):

    #    /muse/annotation sssss  /Marker/1 Plain String instance  

    for loop_counter in range(0,100000000):
        sleep(0.1)
        osc_client.send_message(b'/ping', [np.sin(loop_counter % 10)], safer=True)



 
def main():
 
    global osc_client
    osc_client = OSCClient(osc_client_addr, osc_client_port)
        
#     if args.verbose:
#         print("osc_server_addr: ", osc_server_addr)
#         print("osc_server_port: ", osc_server_port)
#         print("osc_client_addr: ", osc_client_addr)
#         print("osc_client_port: ", osc_client_port)

    osc_server = OSCThreadServer()
    sock = osc_server.listen(address=osc_server_addr, port=osc_server_port, default=True)
    osc_server.bind(b'/muse/eeg', callback_route_data)
    osc_server.bind(b'/ping', callback_ping)
#     osc_server.bind(b'/muse/elements/alpha_absolute', callback_alpha_abs)
#     osc_server.bind(b'/muse/elements/beta_absolute', callback_beta_abs)
#     osc_server.bind(b'/muse/elements/delta_absolute', callback_delta_abs)
#     osc_server.bind(b'/muse/elements/gamma_absolute', callback_gamma_abs)


#     route_OSC_data(osc_client, osc_server)
 
    loop_counter = 0
    
    while True:
        try:
  
            sleep(0.1)
            osc_client.send_message(b'/ping', [np.sin(loop_counter % 10)], safer=True)
            loop_counter =+ 1
        
        except KeyboardInterrupt:
                print('KeyboardInterrupt')

                try:
                    sys.exit(0)
                except SystemExit:

                    print('Finished')
                    os._exit(0)
            

    sys.exit(0)



 
 
 
if __name__ == '__main__':

    date_time_now = strftime('%Y-%m-%d-%H.%M.%S', gmtime())

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", help="Use the RGB LED matrix display - (0/1)", action="store_true")
    parser.add_argument("-w", "--write_data", help="Write EEG data to disk", action="store_true")    
    
    parser.add_argument("-m", "--midi", help="Send data to MIDI output", action="store_true")
#     parser.add_argument("-osc", "--OSC", help="Send data to OSC client - (0/1)", action="store_true")
    parser.add_argument("-osc_server", "--OSC_SERVER", 
                            help="Recive data as an OSC server - (0/1)", action="store_true")
    parser.add_argument("--OSC_IP", help="IP of the OSC client")
    parser.add_argument("--OSC_PORT", help="Port number of OSC client)", type=int)
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", type=int)
    parser.add_argument("-l", "--logging_level", 
                        help="Logging verbosity: 1 = info, 2 = warning, 2 = debug", type=int)
    args = parser.parse_args()


    if args.verbose:
        print("verbose turned on")
        print(args.verbose)

    if args.logging_level:
        print("logging_level:")
        print(args.logging_level)
    
    if args.midi:
        print("midi turned on")
        print(args.midi)

 
    if args.OSC_IP:
        print("OSC_IP turned on")
        osc_client_addr = args.OSC_IP
        print(args.OSC_IP)

    if args.OSC_PORT:
        print("OSC_PORT turned on")
        osc_client_port = args.OSC_PORT
        print(args.OSC_PORT)

              
    if args.logging_level:
        print("logging_level:")
        print(args.logging_level)
        log_filename = './logs/abcs-system-' + date_time_now +'.log'
        directory = os.path.dirname(log_filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

     
    if args.logging_level > 2:
        # logging.basicConfig()
        # DEBUG INFO  WARNING  ERROR  CRITICAL 
        logging.basicConfig(filename=log_filename, 
                            format='%(asctime)s - %(message)s', 
                            level=logging.DEBUG)

    if args.logging_level == 2:
        # logging.basicConfig()
        # DEBUG INFO  WARNING  ERROR  CRITICAL 
        logging.basicConfig(filename=log_filename, 
                            format='%(asctime)s - %(message)s', 
                            level=logging.CRITICAL)

    if args.logging_level == 1:
        # logging.basicConfig()
        # DEBUG INFO  WARNING  ERROR  CRITICAL 
        logging.basicConfig(filename=log_filename, 
                            format='%(asctime)s - %(message)s', 
                            level=logging.ERROR)

    if args.logging_level == 0:
        # logging.basicConfig()
        # DEBUG INFO  WARNING  ERROR  CRITICAL 
        logging.basicConfig(filename=log_filename, 
                            format='%(asctime)s - %(message)s', 
                            level=logging.NOTSET)
                            
                            
    logging.error('ERROR: Start logging to a log file ...')
    logging.critical('CRITICAL: Start logging to a log file ...')
    logging.warning('WARNING: Writing to log file ...')
    logging.info('INFO: Start logging to a log file ...')
    logging.debug('DEBUG: Starting logging at: ' + date_time_now)


    main()
    
    
    sys.exit(0)
