from usocket import socket
from machine import Pin,SPI
import time

def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20))
    nic.active(True)
# If you use the Dynamic IP(DHCP), you must use the "nic.ifconfig('dhcp')".
    nic.ifconfig('dhcp')
# If you use the Static IP, you must use the  "nic.ifconfig("IP","subnet","Gateway","DNS")".
    #nic.ifconfig(('192.168.100.13','255.255.255.0','192.168.100.1','8.8.8.8'))
       
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
        
def main():
    w5x00_init()
    
if __name__ == "__main__":
    main()
