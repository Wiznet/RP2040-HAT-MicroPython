# How to Test MQTT Publish Example

![][link-mqtt]

## Step 1: Prepare Software

> The following serial terminal program is required for **MQTT Publish** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]  or  &#10004; [**Mosquitto**][link-mosquitto]



## Step 2: Prepare hardware

1. Combine WIZnet Ethernet HAT with Raspberry Pi Pico.
2. Connect ethernet cable to Ethernet HAT ethernet port.
3. Connect Raspberry Pi Pico to desktop or laptop using 5 pin micro USB cable.



If you use W5100S-EVB-Pico, you can skip '1. Combine...'



## Step 3: Setup MQTT Publish Example

To test the **MQTT Publish example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_mqtt]

2. Create a new file by pressing the **New File** button. Copy the *umqttsimple* library code into it. You can access the *umqttsimple* library code in the following link: https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py

![][link-mqtt_lib]

3. Setup SPI and Reset pin.

```python
spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
```

4. Initialize ethernet interface and configuration.

```python
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
```

5. In the MQTT configuration, the broker IP address is the IP of your desktop.

```python
#mqtt config
mqtt_server = '192.168.1.11'
client_id = 'wiz'
topic_pub = b'hello'
topic_msg = b'Hello Pico'

last_message = 0
message_interval = 5
counter = 0

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client
```

6. going to use MQTT Publish.

```python
#MQTT Publish
def main():
    w5x00_init()
    try:
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    
    while True:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
        
    client.disconnect()
```



## Step 4: Upload and Run

1. Create broker using mosquitto by executing the following command. If the broker is created normally, the broker's IP address is the current IP of your desktop or laptop, and the port is 1883 by default.

```
mosquitto -c mosquitto.conf -p 1883 -v
```

![][link-mqtt_1]

2. If the MQTT publish example works normally on Raspberry Pi Pico, you can see the network information of Raspberry Pi Pico, connecting to the broker and publishing the message.

![][link-mqtt_2]

3. Subscribe to the broker with the above command. Subscribe will receive a message from the broker.

```
mosquitto_sub -h 192.168.1.11 -t hello
```

![][link-mqtt_3]



## Appendix

- In Mosquitto versions earlier than 2.0 the default is to allow clients to connect without authentication. In 2.0 and up, you must choose your authentication options explicitly before clients can connect. Therefore, if you are using version 2.0 or later, refer to following link to setup 'mosquitto.conf' in the directory where Mosquitto is installed.

    - [**Authentication Methods**][link-authentication_methods]
    
    ![][link-mqtt_conf]



## Attach

Attach a flow that operates through [WIRESHARK][link-wireshark].

- [MQTT_pub.pcapng](https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/example/MQTT/Publish/MQTT_pub.pcapng)




 [**◀ Go to Ethernet example structure**](#ethernet_example_structure)



<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-mosquitto]: https://mosquitto.org/download/
[link-wireshark]: https://www.wireshark.org/#download
[link-mqtt-lib]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/libraries/umqttsimple.py



[link-mqtt]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT.png
[link-thonny_mqtt]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/Thonny_conf_1.png
[link-mqtt_lib]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT_lib.png
[link-mqtt_1]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT_pub2.png
[link-mqtt_2]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT_pub3.png
[link-mqtt_3]:  https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT_pub4.png
[link-mqtt_conf]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/static/images/MQTT/MQTT_conf.png



[link-authentication_methods]: https://mosquitto.org/documentation/authentication-methods/

