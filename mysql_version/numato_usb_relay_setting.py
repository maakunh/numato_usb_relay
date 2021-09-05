#numato_usb_relay_setting.py
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/numato_usb_relay
#This code is imported by relaywrite.py.
#You write your environment parameters in this code.
#These parameters below are samples.

def db_unix_socket():
    return ''

def db_user():
    return 'numato'

def db_passwd():
    return 'numato_relay01'

def db_host():
    return '192.168.11.16'

def db_db():
    return 'numato_relay'

def relay_on():
    return '1'

def relay_off():
    return '0'
    
#this module test
def test():
    print(db_unix_socket)
    print(db_user)
    print(db_passwd)
    print(db_host)
    print(db_db)
if __name__ == '__main__':
    test()