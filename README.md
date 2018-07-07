# PW-Sat2-EGSE
Software for PW-Sat2 Flight Model EGSE: health check software, EGSE Box v1

# PW-Sat2 EGSE Box v1.0

![dsc_3927](https://user-images.githubusercontent.com/6267528/42413528-b9d6f1a8-8222-11e8-9e28-1fd7c849faef.JPG)

Electrical Ground Support Equipment Box is an ultimate solution created to test and maintain flight model of PW-Sat2 spacecraft via umbilical cable. Its main functions include:
* external kill-switch of the satellite
* current probe on kill-switch line
* communication with on-board computer (OBC) via UART
* I2C bus and payload and UART sniffing

![dsc_3904](https://user-images.githubusercontent.com/6267528/42413513-806ea3ca-8222-11e8-9bac-681745ecf1c2.JPG)



## Technical details

### Kill switch
As kill switch key switch is used. LED diode indicates the state (on/off).

### Current probe

Current probe is based on Allegro MicroSystems ACS712ELCTR-05B-T Hall effect linear current sensor. Output analog signal from the sensor is digitized by Digilent Analog Discovery 2 scope. Analog Discovery 2 also provides 5 V supply for current sensor IC. Resolution of single milliamps can be achieved.

![vlcsnap-2018-07-07-20h09m29s593](https://user-images.githubusercontent.com/6267528/42413502-26df1510-8222-11e8-968d-9449a5192b0c.png)

### I2C bus and payload sniffing

8 channel logic states analyzer is used to record all data transmissions on I2C buses and OBC UART.

### UART Communication with OBC

UART to USB converter based on FT232 chip is used to communicate with on-board computer.

![img_20180302_192208](https://user-images.githubusercontent.com/6267528/42413545-16c678e8-8223-11e8-83e0-b5dc84e1e0ca.jpg)

## Repository contents

The repository contains WaveForms workspace file `(*.dwf3work)` with configured power supply for current probe and calibration formula apploed in WaveForms scope view (sensor's output voltage to current).

## Practival information
It's good idea to adjust actual offset voltage (at zero current) because it strongly depends on ambient temperature.
Offset voltage is highlighted in yellow:
![image](https://user-images.githubusercontent.com/6267528/42413646-b87bf036-8224-11e8-9ef0-7db59b9c4a27.png)


# PW-Sat2 Flight Model Health Check Software
