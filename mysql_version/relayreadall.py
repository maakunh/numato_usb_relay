#relayreadall.py Update: 03/09/2021
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/numato_usb_relay
#This code uses for read the status of a relay and record this status to database.
#
#this code needs Numato Lab USB relay module
## https://numato.com/product-category/automation/relay-modules/usb-relay/
#
#This code needs external codes below...
#->pyserial
## https://github.com/pyserial/pyserial

import sys
import datetime
import serial
import mysql.connector as MySQLdb

import numato_usb_relay_setting


#connect database
if(numato_usb_relay_setting.db_unix_socket() != ''):
    conn = MySQLdb.connect(unix_socket=numato_usb_relay_setting.db_unix_socket(), user=numato_usb_relay_setting.db_user(), passwd=numato_usb_relay_setting.db_passwd(), host=numato_usb_relay_setting.db_host(), database=numato_usb_relay_setting.db_db())
else:
    conn = MySQLdb.connect(user=numato_usb_relay_setting.db_user(), passwd=numato_usb_relay_setting.db_passwd(), host=numato_usb_relay_setting.db_host(), database=numato_usb_relay_setting.db_db())

cur = conn.cursor()


if (len(sys.argv) < 2):
        print("Usage: relayreadall.py <PORT>")
        conn.close()
        sys.exit(0)
else:
        portName = sys.argv[1]
        baudRate = int(sys.argv[2])

#Open port for communication
serPort = serial.Serial(portName, baudRate, timeout=1)

dt_now = datetime.datetime.now()

#relay readall command response binary data include of hex number character(8bits)
#ex.  "relay readall\n\n\rA4\n\r" -> "A4" is all relay status.
#1: on, 0: off
#first bit is last number relay status, last bit is first number relay status
cmd = "relay readall" + "\n\r"
serPort.write(cmd.encode())

response = serPort.read(25)
print(response)
strresponse = response.decode()
print(strresponse[len("relay_readall") + 3 : len("relay_readall") + 3 + 2])
binresponse = format(int(strresponse[len("relay_readall") + 3 : len("relay_readall") + 3 + 2], 16), '0>8b')     #change hex character to 8bit bin charactor format
relayNum = 0
for num in range(len(binresponse)):
        relayNum = len(binresponse) - 1 - num
        relay_status = binresponse[num : num + 1]

        if relay_status == numato_usb_relay_setting.relay_on():
                query = 'UPDATE numato_relay_status SET status = "ON", date = "' + dt_now.strftime('%Y/%m/%d %H:%M:%S') + '" where relay_num = "' + str(relayNum) + '" and port = "' + portName + '"'
                print (query)
                cur.execute(query)
                conn.commit()
        elif relay_status == numato_usb_relay_setting.relay_off():
                query = 'UPDATE numato_relay_status SET status = "OFF", date = "' + dt_now.strftime('%Y/%m/%d %H:%M:%S') + '" where relay_num = "' + str(relayNum) + '" and port = "' + portName + '"'
                print (query)
                cur.execute(query)
                conn.commit()
  
serPort.close()
conn.close()
