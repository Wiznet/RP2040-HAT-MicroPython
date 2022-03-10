## Quick Start Firmware
* **▶ [Latest Firmware release(firmware list)](https://github.com/Wiznet/RP2040-HAT-MicroPython/releases)**

## Quick Watch YouTube

 [![UPIO](http://img.youtube.com/vi/86opIykPE-U/0.jpg)](https://youtu.be/86opIykPE-U)

## Quick micropython Code

```python
import network
from machine import Pin,SPI

spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
nic = network.WIZNET5K(spi,Pin(17),Pin(20))

# If you use the Dynamic IP(DHCP), you must use the "nic.active(True)".
# If you use the Static IP, you must use the "nic.ifconfig("IP","subnet","Gateway","DNS")".
    # nic.ifconfig(('192.168.100.13','255.255.255.0','192.168.100.1','8.8.8.8'))
nic.active(True) 

```

