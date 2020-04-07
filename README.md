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
```

breakout board	physical pin	Pi GPIO Pin	Color	Notes
40		01		3V		orange	LCD display 3V
39		02				
38		03		2		brown	LCD display I2C SCA
37		04		5V		blue	4digit display 5V
36		05		3		red	LCD display I2C SCL
35		06		GND		green	4digit display ground
34		07		04		purple	4digit display DIO (PCM DIN)
33		08   		14		blue 	switch 1  
32		09		GND		yellow	LCD display ground
31		10		15		purple	switch 2
30		11		17		grey	4digit display CLK (PCM DOUT)
29		12		18		grey	switch 3
28		13		27		white	rotate A left
27		14   		GND		green	switchs' ground
26		15		22		black	rotate A right
25		16		23		white	switch 4
24		17
23		18		24		black	switch 5
22		19		10 		grey	rotate A push
21		20		GND		brown	rotate A ground
20		21
19		22		25		brown	switch 6
18		23		11		white	white button
17		24		07		red	switch 8
16		25
15		26		08		orange	switch 7
14		27
13		28
12		29		5		black	black button
11		30
10		31		6		blue	blue button
09		32		12		yellow	switch 9
08		33		13		green	green button
07		34		GND		brown	rotate B ground
06		35		19		yellow	yellow button
05		36		16		orange	rotate B right
04		37		26		red	red button
03		38		20		red	rotate B left
02		39		GND		orange	buttons' ground
01		40		21		yellow	rotate B push
```

SSH1106
from `https://hiletgo.com/ProductDetail/2157364.html` driver chip is SSH1106

magic line is `sudo -H pip install --upgrade --ignore-installed pip setuptools`
new magic line as of 2020-03-26 `sudo pip install --index-url=https://pypi.python.org/simple/ setuptools`
or possibly a combination of the previous two lines!!

additional usefull note install Adafruit from the git 

`sudo python seup.py install`
now this works
```
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
```
## System Setup

use the utility `sudo raspi-config` to enable the I2C interface and login into the wireless router

special instructions for rasbian light
`sudo apt-get update`
install pip `sudo apt-get install python3-pip`
install git `sudo apt-get install git`

`sudo apt-get install libopenjp2-7`
`sudo apt install libtiff5`

Make Python and pip version 3 by default
```
` (only needed for rasbian light)
sudo rm /usr/bin/python
sudo rm /usr/bin/pip
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo ln -s /usr/bin/pip3 /usr/bin/pip
```

```
sudo pip install wiringpi
sudo pip install luma.core
sudo pip install luma.oled
sudo pip install gpiozero
```

install python library for the red led
```
git clone https://github.com/depklyon/raspberrypi-python-tm1637
cd raspberrypi-python-tm1637
sudo python setup.py install
```

download the repository and test
```
git clone https://github.com/jleiterman/puzzlebox
cd puzzlebox
./systemtest.py
```
