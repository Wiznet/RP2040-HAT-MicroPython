## Quick Start Firmware
* Currently, 
**▶ [Latest Firmware release(firmware list)](https://github.com/Wiznet/RP2040-HAT-MicroPython/releases)**

* [UPIP?(**refer to micropython document**)](https://docs.micropython.org/en/latest/reference/packages.html#upip-package-manager)
## Quick Start YouTube

 [![UPIO](http://img.youtube.com/vi/3-w5iO6PuvQ/0.jpg)](https://youtu.be/3-w5iO6PuvQ)
<code>
import network
import usocket
from machine import Pin,SPI
import upip
import time

spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
nic = network.WIZNET5K(spi,Pin(17),Pin(20))
nic.active(True)
time.sleep(0.1)
upip.install("micropython-urequests")

#upip.install("webrepl")
</code>