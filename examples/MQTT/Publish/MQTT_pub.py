from umqttsimple import MQTTClient
from usocket import socket
from machine import Pin,SPI
import network
import time

#mqtt config
mqtt_server = '192.168.1.2'
client_id = 'wiz'
topic_pub = b'hello'
topic_msg = b'Hello Pico'

last_message = 0
message_interval = 5
counter = 0

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
    
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

#reconnect & reset
def reconnect():
    print('Failed to connected to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
    
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

if __name__ == "__main__":
    main()


