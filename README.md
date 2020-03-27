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

pin mapping for small screen
```
OLED Pin    Pi GPIO Pin    Notes
GND         14             Ground
Vcc         1              3.3V
SCL         5              I2C SCL
SDA         3              I2C SCA
```
pin mapping for 4 digit display
```
HW-069      Pi GPIO Pin    Notes
CLK         40             PCM DOUT
DIO         38             PCM DIN
VCC         4              5V
GND         6              Ground
```


SSH1106
from `https://hiletgo.com/ProductDetail/2157364.html` driver chip is SSH1106

magic line is `sudo -H pip install --upgrade --ignore-installed pip setuptools`
new magic line as of 2020-03-26 `sudo pip install --index-url=https://pypi.python.org/simple/ setuptools`
or possibly a combination of the previous two lines!!

additional usefull note install Adafruit from the git 
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
`sudo python seup.py install`
now this works
```
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
```

```
sudo pip install wiringpi
sudo pip install luma.core
sudo pip install luma.oled

Use `sudo raspi-config' to enable the I2C interface

Make Python and pip version 3 by default

sudo rm /usr/bin/python
sudo rm /usr/bin/pip
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo ln -s /usr/bin/pip3 /usr/bin/pip
sudo python setup.py install

git clone https://github.com/jleiterman/puzzlebox
git clone https://github.com/depklyon/raspberrypi-python-tm1637
cd raspberrypi-python-tm1637
sudo python setup.py install
```
