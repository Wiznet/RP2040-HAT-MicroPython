# How to Test Loopback Example

![][link-loopback]

## Step 1: Prepare Software

> The following serial terminal program is required for **Loopback** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]  or  &#10004; [**Hercules**][link-hercules]



## Step 2: Prepare hardware

1. Combine WIZnet Ethernet HAT with Raspberry Pi Pico.
2. Connect ethernet cable to Ethernet HAT ethernet port.
3. Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.



If you use W5100S-EVB-Pico, you can skip '1. Combine...'



## Step 3: Setup Loopback Example

> To test the **Loopback example**, minor settings shall be done in code.



1. Setup SPI and Reset pin.

```python
spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
```

2. Initialize ethernet interface and configuration.

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

3. How to operate as a **Loopback Server**.

```py
def server_loop(): 
    s = socket()
    s.bind(('192.168.1.20', 5000)) #Source IP Address
    s.listen(5)
            
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr) 
    print("Loopback server Open!")
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)
```

4. How to operate as a **Loopback Client**.

```python
ef client_loop():
    s = socket()
    s.connect(('192.168.1.11', 5000)) #Destination IP Address
    
    print("Loopback client Connect!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)
```



## Step 4: Upload and Run

# **`Loopback Server Mode`**

1. The Loopback is executed and the server waits in Listen state.

![][link-loopback_server_1]

2. Open the Hercules program to set **[IP Address]** and **[PORT number]** and Connect to the Server.

![][link-loopback_server_2]

3. You can confirm that the client has connected to the server.

![][link-loopback_server_3]

4. If you send the phrase Loopback Test, you can see that you are sending and receiving data.

![][link-loopback_server_4]



# **`Loopback Client Mode`**

1. Open the server in the Hercules program. If you put in the port number and press Listen, the server will open.

![][link-loopback_client_1]

2. When the Client function is retrieved from the loopback source and executed, it connects to the server normally.

![][link-loopback_client_2]

3. You can see that it is connected from the Hercules **[Client Connect status]** server.

![][link-loopback_client_3]

4. If you send the data from the server, you can receive the data you sent.

![][link-loopback_client_4]



## Attach

Attach a flow that operates through [WIRESHARK][link-wireshark].

- [Loopback.pcapng](https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/example/Loopback/loopback.pcapng)




 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)





<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility
[link-wireshark]: https://www.wireshark.org/#download



[link-loopback]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback.png

[link-loopback_server_1]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_server_1.png
[link-loopback_server_2]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_server_2.png
[link-loopback_server_3]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_server_3.png
[link-loopback_server_4]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_server_4.png



[link-loopback_client_1]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_client_1.png
[link-loopback_client_2]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_client_2.png
[link-loopback_client_3]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_client_3.png
[link-loopback_client_4]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/Loopback/Loopback_client_4.png

