#relaywrite.py Update: 03/09/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/numato_usb_relay
#This code uses for relays on/off.
#
#this code needs Numato Lab USB relay module
## https://numato.com/product-category/automation/relay-modules/usb-relay/
#
#This code needs external codes below...
#->pyserial
## https://github.com/pyserial/pyserial

import sys
import serial
import datetime
import mysql.connector as MySQLdb

import numato_usb_relay_setting

#connect database
if(numato_usb_relay_setting.db_unix_socket() != ''):
    conn = MySQLdb.connect(unix_socket=numato_usb_relay_setting.db_unix_socket(), user=numato_usb_relay_setting.db_user(), passwd=numato_usb_relay_setting.db_passwd(), host=numato_usb_relay_setting.db_host(), database=numato_usb_relay_setting.db_db())
else:
    conn = MySQLdb.connect(user=numato_usb_relay_setting.db_user(), passwd=numato_usb_relay_setting.db_passwd(), host=numato_usb_relay_setting.db_host(), database=numato_usb_relay_setting.db_db())
cur = conn.cursor()

if (len(sys.argv) < 4):
	print("Usage: relaywrite.py <PORT> <BAUDRATE> <RELAYNUM> <COMMAND: on/off>")
	print ("For example, relaywrite.py COM2 9600 1 on")
	conn.close()
	sys.exit(0)
else:
	portName = sys.argv[1]
	baudRate = int(sys.argv[2])
	relayNum = sys.argv[3]
	relayCmd = sys.argv[4]

#Open port for communication
serPort = serial.Serial(portName, baudRate, timeout=1)

#Send the command
cmd = "relay " + str(relayCmd) + " " + str(relayNum) + "\n\r"
serPort.write(cmd.encode())
print("Command sent...")

#Record to database(numato.db)
dt_now = datetime.datetime.now()
query = 'INSERT INTO numato_relay_operation_history VALUES("' +  dt_now.strftime('%Y/%m/%d %H:%M:%S') + '", "' +  portName + '", "'+ relayNum + '", "' + relayCmd + '")'
cur.execute(query)
conn.commit()
conn.close()

#Close the port
serPort.close()
