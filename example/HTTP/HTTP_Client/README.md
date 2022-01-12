# How to WebClient Example

![][link-http]


## Step 1: Prepare Software

> The following serial terminal program is required for **Webclient** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]




## Step 2: Prepare hardware

1. Combine WIZnet Ethernet HAT with Raspberry Pi Pico.
2. Connect ethernet cable to Ethernet HAT ethernet port.
3. Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.



If you use W5100S-EVB-Pico, you can skip '1. Combine...'



## Step 3: Setup WebClinet Example

To test the **Webclient example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_http]

2. Create a new file by pressing the **New File** button. Copy the ***urequest.py*** library code into it. You can access the *urequest* library code in the following link - https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/libraries/urequest.py

![][link-request_lib]

3. Setup SPI and Reset pin.

```python
spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
```

2. Initialize ethernet interface and configuration.

```python
nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
while not nic.isconnected():
    time.sleep(1)
    print(nic.regs())
```

3. HTML request, Access **HTML **.

```python
def request():
    #get
    r = urequest.get("http://httpbin.org/get")
    r.raise_for_status()
    print(r.status_code)
    print(r.text)
    
    #post
    r = urequest.post("http://httpbin.org/post", json={'Hello': 'WIZnet'})
    print(r.json())
```



## Step 4: Upload and Run

1. Use DNS to access the address of the server. After that, it accesses the server in each URL and prints the contents. The text of each URL is as follows.

![][link-webclient_1]

2. Text content in **HTML**.

![][link-webclient_2]



## Attach

Attach a flow that operates through [WIRESHARK][link-wireshark].

- [HTTP_Client.pcapng](https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/HTTP/HTTP_Client)



 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)





<!--
Link
-->

[link-thonny]: https://thonny.org/

[link-wireshark]: https://www.wireshark.org/#download



[link-http]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/HTTP/HTTP.png
[link-thonny_http]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/HTTP/Thonny_conf_1.png
[link-request_lib]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/HTTP/webclient_request.png
[link-webclient_1]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/HTTP/webclient_1.png
[link-webclient_2]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/HTTP/webclient_2.png
