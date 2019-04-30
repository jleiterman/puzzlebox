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

SSH1106

from `https://hiletgo.com/ProductDetail/2157364.html` driver chip is SSH1106

magic line is `sudo -H pip install --upgrade --ignore-installed pip setuptools`

now this works
```
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 10), "All Your Base are\nbelong to us!", fill="white")
```


A
A
D
magic line is sudo -H pip install --upgrade --ignore-installed pip setuptools`
