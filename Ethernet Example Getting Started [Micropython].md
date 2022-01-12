

:rocket:Ethernet Example Getting Started [MicroPython]
===========================


> These sections will guide you through a series of steps from configuring development environment to running ethernet examples using the **WIZnet's ethernet products**.

- [Hardware requirements](#hardware_requirements)
- [Development environment configuration](#development_environment_configuration)
  - [STEP1 : **Installing Micropython**](#step1--installing-circuitpython)
  - [STEP2 : **Setup Ethernet Libraray**](#step2--setup-wiznet-ethernet-libraray)
- [Ethernet example structure](#ethernet_example_structure)
- [Ethernet example testing](#Ethernet_example_testing)
- [Documentation](#Documentation)



<a name="hardware_requirements"></a>

# :hammer:Hardware requirements

> The ethernet examples use **Raspberry Pi Pico** and **WIZnet Ethernet HAT** ethernet I/O module built on WIZnet's [**W5100S**][link-w5100s] ethernet chip or **W5100S-EVB-Pico** ethernet I/O module built on [**RP2040**][link-rp2040] and WIZnet's [**W5100S**][link-w5100s] ethernet chip.

| Image                                                        | Name                                                      | Etc                                                          |
| ------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------ |
| <image src= "./images/START/raspberrypi_pico.PNG" width="200px" height="110px"> | [**Raspberry Pi Pico**][link-raspberry_pi_pico]           | [Pico Document](https://www.raspberrypi.org/documentation/microcontrollers/raspberry-pi-pico.html) |
| <image src= "./images/START/WIZnet-Ethernet-HAT-1.png" width="240px" height="80px"> | [**WIZnet Ethernet HAT**][link-wiznet_ethernet_hat]       | [Ethernet HAT Datasheet](https://docs.wiznet.io/Product/Open-Source-Hardware/wiznet_ethernet_hat) |
| <image src= "./images/START/W5100S-EVB-Pico_1.png" width="250px" height="90px"> | [**WIZnet W5100S-EVB-Pico**][link-wiznet_W5100S_evb_pico] | [W5100S-EVB-Pico Datasheet][link-wiznet_W5100S_evb_pico]     |

> ### Pin Diagram

**`WIZnet Ethernet HAT`**

Ethernet-HAT has the same pin arrangement and pin spacing as Raspberry Pi Pico. The W5100S and RJ45 are built-in, Ethernet can be used by plugging into the Raspberry pi pico. **One thing to note when using HAT is to look carefully at the direction and plug it in**. There is a USB shape marked, and this direction and the USB direction of Pico must be the same.

![][link-PICO_HAT]

------

**`WIZnet W5100S-EVB-Pico`**

In the W5100S-EVB-Pico board, GPIO pins are connected the same as the Raspberry Pi Pico board.  If Pico uses Ethernet, **PIO16, GPIO17, GPIO18, GPIO19, GPIO20**, and **GPIO21** pins cannot be used. It is a pin used inside the RP2040 board.

![][link-PICO_EVB]

| I/O  | Pin Name | Description                                    |
| :--- | -------- | ---------------------------------------------- |
| I    | GPIO16   | Connected to **MISO** on W5100S                |
| O    | GPIO17   | Connected to **CSn** on W5100S                 |
| O    | GPIO18   | Connected to **SCLK** on W5100S                |
| O    | GPIO19   | Connected to **MOSI** on W5100S                |
| O    | GPIO20   | Connected to **RSTn** on W5100S                |
| I    | GPIO21   | Connected to **INTn** on W5100S                |
| I    | GPIO24   | VBUS sense - high if VBUS is present, else low |
| O    | GPIO25   | Connected to user LED                          |
| I    | GPIO25   | Used in ADC mode (ADC3) to measure VSYS/3      |

<a name="development_environment_configuration"></a>

# :bulb:Development environment configuration

> To test the ethernet examples, the development environment must be configured to use Raspberry Pi Pico. The ethernet examples were tested by configuring the development environment for **Windows**. Please refer to the '**9.2. Building on MS Windows**' section of '**Getting started with Raspberry Pi Pico**' document below and configure accordingly.

![][link-Micropython]



<a name="step1--installing-circuitpython"></a>

## STEP - 1 : [**Installing Micropython**][link-Installing Micropython]

:warning:**Notice**

Install `Thonny IDE` on Raspberry Pi Pico by referring to the link above.:point_down:

 - **https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0**



------

- The drive will be called **RPI-RP2** on all RP2040 boards. Download the **UF2**(firmware.uf2) file from the link below and put the file in Pico.

File link - [firmware.uf2](https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/firmware.uf2?raw=true)

![][link-firmware]

- You can also access the firmware installation menu if you click on **MicroPython (Raspberry Pi Pico)** in the status bar and choose ‘Configure interpreter …’.

![][link-setup_1]

- The interpreter settings will open. Click on **Install or update firmware**. 

![][link-setup_2]

- You will be prompted to plug in your Raspberry Pi Pico while you hold the BOOTSEL button.

![][link-setup_3]

- Then you can click **Install**. Wait for the installation to complete and click **Close**.

![][link-setup_4]

- Look at the Shell panel at the bottom of the Thonny editor. You should see something like this:

![][link-setup_5]



<a name="step2--setup-wiznet-ethernet-libraray"></a>

# STEP - 2 : [**Setup Ethernet Libraray**][link-Setup Ethernet Libraray]

`First, import the library of the function you want to use from the library to your PC. To uploading a file to using Thonny IDE, follow these next steps.`

**[Micropython Ethernet Libraries][link-Setup Ethernet Libraray]**

- Create a new file, Save it in your computer with the exact name that you want, for example “**(your library name).py**”
- Go to **Open > This computer**

![][link-mpy_lib_1]

- The file should be saved on RPi Pico with the name **“(your library name).py”**
- Go to **File > Save as > Raspberry Pi Pico**

![][link-mpy_lib_2]





<a name="ethernet_example_structure"></a>

# :open_file_folder:Ethernet example structure

Ethernet examples are available at '**RP2040-HAT-MicroPython/example/**' directory. As of now, following examples are provided.

- [**Loopback**][link-loopback]
- [**HTTP**][link-HTTP]
  - [WebServer][link-WebServer]
  - [WebClient][link-WebClient]
- [**MQTT**][link-MQTT]
  - [Publish][link-MQTT_Pub]
  - [Subscribe][link-MQTT_Sub]

<a name="Ethernet_example_testing"></a>

# :pushpin:Ethernet example testing

Check if the network is connected normally and if the data is sent to each other.

[w5x00_Ping_Test.py](https://github.com/Wiznet-OpenHardware/RP2040-HAT-MicroPython/blob/main/example/PING_TEST/w5x00_Ping_Test.py)

> This is the code to set the IP of 192.168.1.20
>
> I hope that the PC also has an environment that communicates with 192.168.1.xxx.

1. Copy the content to code.py on your RPi Pico and run.

![][link-ping_1]

2. Press the `Win+R` key to enter cmd and press Enter or OK to execute the **command prompt**.

![][link-ping_2]

3. When the command prompt window appears, type the **ping command** and press Enter.

```
ping 192.168.1.20 (-option)
```

![][link-ping_3]

4. Ping tests begin as packets are exchanged between hosts. If you look at the time and loss rate among the statistical results, you can find out the status of the Internet network. 

![][link-ping_4]





<a name="Documentation"></a>

# :books:Documentation

Documentation for WIZnet Ethernet HAT and Raspberry pi pico board
## Raspberry Pi Pico
 [**Raspberry Pi Pico Datasheet**](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)

  An RP2040-based microcontroller board

 [**Getting started with Raspberry Pi Pico**](https://www.raspberrypi.org/documentation/microcontrollers/raspberry-pi-pico.html)

 C/C++ development with Raspberry Pi Pico and other RP2040-based microcontroller boards

## WIZnet Ethernet HAT & EVB
 [**WIZnet Ethernet HAT**](https://docs.wiznet.io/Product/Open-Source-Hardware/wiznet_ethernet_hat)

 [**W5100S-EVB-Pico**](https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico)

Please refer to 'README.md' in each examples directory to find detail guide for testing ethernet examples.





<!--

Link

-->

[link-Installing Micropython]:https://thonny.org/
[link-w5100s]: https://docs.wiznet.io/Product/iEthernet/W5100S/overview
[link-rp2040]: https://www.raspberrypi.org/products/rp2040/



[link-PICO_HAT]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/HAT.png
[link-PICO_EVB]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/EVB.png

[link-raspberry_pi_pico]: https://www.raspberrypi.org/products/raspberry-pi-pico
[link-wiznet_ethernet_hat]: https://docs.wiznet.io/Product/Open-Source-Hardware/wiznet_ethernet_hat
[link-wiznet_W5100S_evb_pico]:https://docs.wiznet.io/Product/iEthernet/W5100S/w5100s-evb-pico
[link-library]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/libraries



[link-Micropython]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/MicroPython_Thonny.png
[link-Setup Ethernet Libraray]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/libraries
[link-firmware]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/firmware.png
[link-setup_1]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/thonny-configure-interpreter.png
[link-setup_2]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/thonny-interpreter-settings.png
[link-setup_3]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/thonny-bootsel.png
[link-setup_4]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/thonny-firmware-install.png
[link-setup_5]: https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/repl-connected.png

[link-mpy_lib_1]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/mpy_lib_1.png
[link-mpy_lib_2]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/mpy_lib_2.png



[link-loopback]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/Loopback
[link-HTTP]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/HTTP
[link-WebServer]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/HTTP/HTTP_Server
[link-WebClient]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/HTTP/HTTP_Client
[link-MQTT]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/MQTT
[link-MQTT_Pub]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/MQTT/Publish
[link-MQTT_Sub]:https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/example/MQTT/Subscribe



[link-ping_1]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/Pico_ping.png
[link-ping_2]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/pico_ping2.png
[link-ping_3]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/pico_ping3.png
[link-ping_4]:https://github.com/Wiznet/RP2040-HAT-MicroPython/blob/main/images/START/pico_ping4.png


_[▲ Back to Top](#Ethernet_Example_Getting_Started)_ 

