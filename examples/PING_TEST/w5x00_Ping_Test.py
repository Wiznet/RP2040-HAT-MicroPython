from usocket import socket
from machine import Pin,SPI
import network
import time

led = Pin(25, Pin.OUT)

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    print(nic.ifconfig())
        
def main():
    w5x00_init()

    while True:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)

if __name__ == "__main__":
    main()