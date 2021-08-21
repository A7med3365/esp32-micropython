# This file is executed on every boot (including wake-boot from deepsleep)
#import esp #esp.osdebug(None)
import webrepl
import network
print('hello')

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='Ahmed') # set the ESSID of the access point
ap.config(max_clients=10) # set how many clients can connect to the network
ap.active(True)         # activate the interface

webrepl.start()
