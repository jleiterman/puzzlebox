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

To autorun the program add it to the sudo crontab `sudo crontab -e` add the line pointing the the program you want to autorun for example `@reboot python /home/pi/puzzlebox/july4th2020.py`



when using cavas the corrdinate system starts in the upper left corner of the screen and 
draw.text((<pixels right of upper left corner>,<pixel down from upper left corner>)...

draw.rectange((<top left pixels right of upper left corner>    , <top left pixels down of upper left corner>,
               <bottom right pixels right of upper left corner>, <bottom right pixels down of upper left corner>)...

text 7 points high 6 points wide 9 points with two spaces above is a comfortable spacing for reading

the screen is 64 pixel high by 128 wide.

Screen holds a max of 21 characters wide with two extra pixels
Using \n for new lines you can get 4

#lcd_text("123456789012345678901\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11")
#sleep(10) 
with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.text((1, 0),"123456789012345678901\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11", fill="white")

with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.text((1,2),"This is text it goes \nFrom Left to right bu\nt you must realize th\nat you can only fit s", fill="white")

with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.text((1,-2),"This is text it goes ", fill="white")
    draw.text((1,5), "From Left to right bu", fill="white")
    draw.text((1,12),"t if you space by 7  ", fill="white")
    draw.text((1,19),"points  you can  get ", fill="white")
    draw.text((1,26),"a total of nine lines", fill="white")
    draw.text((1,33),"which is a lot but wh", fill="white")
    draw.text((1,40),"ile this is readable ", fill="white")
    draw.text((1,47),"it is very tight and ", fill="white")
    draw.text((1,55),"I would recommend goi", fill="white")

with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.text((1,0), "This is text it goes ", fill="white")
    draw.text((1,9), "From Left to right bu", fill="white")
    draw.text((1,18),"t if you space by 9  ", fill="white")
    draw.text((1,27),"points it seems like ", fill="white")
    draw.text((1,36),"a reasonable compromi", fill="white")
    draw.text((1,45),"se giving seven lines", fill="white")
    draw.text((1,54),"of text as a soft lim", fill="white")

    
with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.rectangle((0,0,127,9),outline="white",fill="white")
    draw.rectangle((14,12,127,13),outline="white",fill="white")
    draw.rectangle((0,14,13,63),outline="white",fill="white")
    draw.text((1, 0),"TopMenu pick SubMenu ", fill="black")
    draw.text((1,14),"Rr",fill="black")
    draw.text((17,14),"Core Operation",fill="white")
    draw.text((1,24),"Yw",fill="black")
    draw.text((1,34),"Gr",fill="black")
    draw.text((1,44),"Bu",fill="black")
    draw.text((1,54),"Bk",fill="black")

    #draw.text((0, 0),"123456789012345678901\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11", fill="black")
    #draw.rectangle((1,1,126,62),outline="black",fill="black")
    #draw.text((10,10),"White",fill="white")


with canvas(lcd_screen) as draw:
    draw.rectangle((0,0,0,0,),outline="white",fill="white")
    #draw.rectangle((127,63,127,63),outline="white",fill="white")
    draw.rectangle((128,64,128,64),outline="white",fill="white")
    draw.rectangle((10,10,20,20),outline="white",fill="white")
    draw.rectangle((20,20,30,30),outline="white",fill="white")
    
attempting to integrate
UEME 10.1" Portable DVD/CD Player With Car Headrest Holder, Personal DVD Players PD-1020
resolution panel; resolution 1024*600

edits to /boot/config.txt
# uncomment to force a console size. By default it will be display's size minus
# overscan.
framebuffer_width=1024
framebuffer_height=600

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1
hdmi_ignore_hotplug=1 #needed to disable hdmi

# uncomment to force a specific HDMI mode (this will force VGA)
hdmi_group=1
hdmi_mode=1

# uncomment for composite PAL
sdtv_mode=0   
sdtv_aspect=3


12345678902234567890323456789042345678905234567890623456789072345678908234567890
checking character on little screen


https://www.youtube.com/watch?v=4M-C9WHew9w
ideas on the day night clock

https://forums.raspberrypi.com/viewtopic.php?t=73120
displaying images to display



for sound get pygame
```
  731  apt-get update --allow-releaseinfo-change
  732  sudo apt-get update --allow-releaseinfo-change
  733  sudo apt-get install python3-pygame
  734  python
  735  sudo apt-get install libSDL2_mixer-2.0.so.0
  736  sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
```
from pygame import mixer
mixer.init()
sound = mixer.Sound('applause-1.wav')
#wget http://www.pacdv.com/sounds/people_sound_effects/applause-1.wav
sound.play()


cat /dev/urandom >/dev/fb0
fim -a fim_yoda_1.jpg 