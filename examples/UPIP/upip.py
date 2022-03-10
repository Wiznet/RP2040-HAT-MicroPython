import network
import usocket
from machine import Pin,SPI
import upip
import ussl
import upip
import time

spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
nic = network.WIZNET5K(spi,Pin(17),Pin(20))
nic.active(True)
time.sleep(0.1)
upip.install("micropython-urequests")

#upip.install("webrepl")