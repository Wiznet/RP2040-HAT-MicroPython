# How to WebServer Example

![][link-http]


## Step 1: Prepare Software

> The following serial terminal program is required for **Webserver** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]




## Step 2: Prepare hardware

1. Combine WIZnet Ethernet HAT with Raspberry Pi Pico.
2. Connect ethernet cable to Ethernet HAT ethernet port.
3. Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.



If you use W5100S-EVB-Pico, you can skip '1. Combine...'



## Step 3: Setup Webserver Example

> To test the **Webserver example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_http]

2. Setup SPI and Reset pin.

```python
spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
```

3. Initialize ethernet interface and configuration.

```python
#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    
    #DHCP
    #nic.ifconfig('dhcp')
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
```

4. HTML request

```python
html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raspberry Pi Pico Web server - WIZnet W5100S</title>
    </head>
    <body>
    <div align="center">
    <H1>Raspberry Pi Pico Web server & WIZnet Ethernet HAT</H1>
    <h2>Control LED</h2>
    PICO LED state: <strong>""" + led_state + """</strong>
    <p><a href="/?led=on"><button class="button">ON</button></a><br>
    </p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a><br>
    </p>
    </div>
    </body>
    </html>
    """
```

5. Run Pico to open the web server.

```python
while True:
        conn, addr = s.accept()
        print('Connect from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        #print('Content = %s' % request)
        led_on = request.find('/?led=on')
        led_off = request.find('/?led=off')
        if led_on == 6:
            print("LED ON")
            led.value(1)
        if led_off == 6:
            print("LED OFF")
            led.value(0)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Connection: close\n\n')
        conn.send(response)
        conn.close()
```



## Step 4: Upload and Run

1. When you execute the code, you open Websever and wait.

![][link-webserver_1]

2. If you open the HTML web page and enter 192.168.1.20 and you will see the server connected

![][link-webserver_2]

3. If you press the ON button below, the LED built into the Pico turns on.

![][link-webserver_3]

3. The LED turns on and outputs a text message called LED ON., Likewise, if you press OFF, the LED turns off.

![][link-webserver_4]![][link-webserver_5]



## Attach

Attach a flow that operates through [WIRESHARK][link-wireshark].

- [HTTP_Server.pcapng](https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/example/HTTP/HTTP_Server/HTTP_Server.pcapng)


 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)



<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-http]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/HTTP.png

[link-wireshark]: https://www.wireshark.org/#download



[link-thonny_http]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/Thonny_conf_1.png



[link-webserver_1]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/webserver_1.png
[link-webserver_2]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/webserver_2.png
[link-webserver_3]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/webserver_3.png
[link-webserver_4]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/webserver_4.png
[link-webserver_5]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/HTTP/Webserver_6.jpg

