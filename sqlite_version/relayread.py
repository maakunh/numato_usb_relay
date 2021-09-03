#relayread.py Update: 26/08/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/numato_usb_relay
#This code uses for read the status of a relay and standard output this status.
#
#this code needs Numato Lab USB relay module
## https://numato.com/product-category/automation/relay-modules/usb-relay/
#
#This code needs external codes below...
#->pyserial
## https://github.com/pyserial/pyserial

import sys
import serial

if (len(sys.argv) < 3):
	print("Usage: relayread.py <PORT> <BAUDRATE> <RELAYNUM>")
	sys.exit(0)
else:
	portName = sys.argv[1]
	baudRate = int(sys.argv[2])
	relayNum = sys.argv[3]

#Open port for communication
serPort = serial.Serial(portName, baudRate, timeout=1)

#Send "relay read" command
cmd = "relay read "+ relayNum + "\n\r"
serPort.write(cmd.encode())

response = serPort.read(25)

if(response.find(bytes(b"on")) > 0):
	print("on")
elif(response.find(bytes(b"off")) > 0):
	print("off")
#Close the port
serPort.close()