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
    
    #None DHCP
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    
    #DHCP
    #nic.ifconfig('dhcp')
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def web_page():
    if led.value()==1:
        led_state="ON"
    else:
        led_state="OFF"
        
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
    return html

def main():
    w5x00_init()
    s = socket()
    s.bind(('192.168.1.20', 80))
    s.listen(5)

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
        conn.send('Connection: close\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Content-Length: %s\n\n' % len(response))
        conn.send(response)
        conn.close()

if __name__ == "__main__":
    main()