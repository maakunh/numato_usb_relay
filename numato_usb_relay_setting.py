#numato_usb_relay_setting.py
#Author: Masafumi Hiura
#URL: https://github.com/maakunh/numato_usb_relay
#This code is imported by relaywrite.py.
#You write your environment parameters in this code.
#These parameters below are samples.

def dbPath():
    return r'\\DESKTOP-2322PPH\Users\Public\numato\numato.db'

#this module test
#You can test epever_control_setting.py in command line console.
def test():
    print('numato_usb_relay_dbPath = ' + numato_usb_relay_dbPath())
if __name__ == '__main__':
    test()