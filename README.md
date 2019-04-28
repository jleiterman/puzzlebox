# puzzlebox
software for escape room in a box puzzle game

### system test
`systemtest.py` is a file that runs through unit tests that validate the configuration and functionality of components.  Where possilbe tests are automated but some tests require humansto validate by changing physical inputs or by reading displayesand verifying that they are displaying proberly

### lcd display info
https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/

Install OLED Python Library
In order to display text, shapes and images you can use the Adafruit Python library. It should work with all SSD1306 based displays including their own 128×32 and 128×64 devices.

To install the library run the following command :

`git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git`
Once that completes navigate to the library’s directory :

`cd Adafruit_Python_SSD1306`
and install the library for Python 2 :

sudo python setup.py install
and/or Python 3 :

`sudo python3 setup.py install`
This process will give you ability to include the library within your own Python scripts.


OLED Pin    Pi GPIO Pin    Notes
Vcc         1              *3.3V
Gnd         14 **          Ground
SCL         5              I2C SCL
SDA         3              I2C SCA

