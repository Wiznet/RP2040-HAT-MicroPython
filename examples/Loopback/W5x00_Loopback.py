import network
import time
from usocket import socket
from machine import Pin,SPI
import rp2

def init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())

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

def client_loop():
    s = socket()
    s.connect(('192.168.1.11', 5000)) #Destination IP Address
    
    print("Loopback client Connect!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)
            
def main():
    init()
    server_loop() #Loopback Server Mode
    #client_loop() #Loopback client Mode

if __name__ == "__main__":
    main()
