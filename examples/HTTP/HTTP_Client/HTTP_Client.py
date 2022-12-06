from usocket import socket
from machine import Pin,SPI
import urequests
import network
import time

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    
#None DHCP
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    
#DHCP
    #nic.ifconfig('dhcp')
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def request():
    r = urequests.get('http://httpbin.org/get')
    #r.raise_for_status
    print(r.status_code)
    print(r.text)
    r= urequests.post('http://httpbin.org/post', json={'WIZnet Test'})
    if not r:
        print('spreadsheet: no response received')
    print(r.json())

def main():
    w5x00_init()
    request()

if __name__ == "__main__":
    main()
