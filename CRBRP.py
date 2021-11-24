#!/usr/bin/python3

# CRBRP

# first test is to ensure that needed libraries load
import sys
import time
import os
import tm1637
import threading

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import Button
from signal import pause
from time import time, sleep, localtime

# setup input-output
#Red LED display
red_led = tm1637.TM1637(clk=17,dio=4)
#White LCD screen
#width 128 points
#heigh 64 points
serial = i2c(port=1, address=0x3C)
lcd_screen = sh1106(serial)


#buttons
red_button = Button(26)     #   Core Operation   #
#   Core Operation   #
#Core:Online         #  #Core:Shutdown       #
#Core Temp:   XXXXX F#
#Inlet Temp:  XXXXX F#
#Outlet Temp: XXXXX F#
#flow rate: XXXXXlb/m#


yellow_button = Button(19)  #Primary Heat Removal#
#Primary Heat Removal#
#Pump1: ON XXXXXX PSI#
#Pump2:OFF XXXXXX PSI#
#A:XXXXX F  B:XXXXX F#
#flow trgt: XXXXXlb/m#
#flow rate: XXXXXlb/m#

green_button = Button(13)   #  2nd Heat Removal  #
#  2nd Heat Removal  #
#Pump1: ON XXXXXX PSI#
#Pump2:OFF XXXXXX PSI#
#A:XXXXX F  B:XXXXX F#
#flow trgt: XXXXXlb/m#
#flow rate: XXXXXlb/m#

blue_button = Button(6)     #  Steam handeling   #
#  Steam Handeling   #
#Pump1: ON XXXXXX PSI#
#Pump2:OFF XXXXXX PSI#
#A:XXXXX F  B:XXXXX F#
#steam temp XXXXXXX F#
#  pressure XXXXX PSI#
#flow rate: XXXXXlb/m#

black_button = Button(5)    #  Power Generation  #
white_button = Button(11)   #   Backup Systems   #

#switches
switch_1 = Button(14)       # Power on for Remote Radio Controler 
switch_2 = Button(15)       # Manual Core Shutdown / Normal Operation
switch_3 = Button(18)       # 
switch_4 = Button(23)       # Primary heat removal Pump
switch_5 = Button(24)       # Primary heat removal pump2
switch_6 = Button(25)       # Primary loop coolent heater
switch_7 = Button(8)
switch_8 = Button(7)
switch_9 = Button(12)
#rotating buttons
a_right = Button(27)        # Field selector #
a_left = Button(22)         # Push to Cancel #
a_button = Button(10)
b_right = Button(20)        # Value adjustment #
b_left = Button(16)         # Push to Enter #
b_button = Button(21)



def lcd_text(text):
    with canvas(lcd_screen) as draw:
        draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
        draw.text((0, 0), text, fill="white")


#lcd_text("123456789012345678901\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11")
#sleep(10) 
with canvas(lcd_screen) as draw:
    draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
    draw.rectangle((0,0,127,9),outline="white",fill="white")
    draw.rectangle((14,12,127,13),outline="white",fill="white")
    draw.rectangle((0,14,13,63),outline="white",fill="white")
    draw.text((1, 0),"primary heat removeal", fill="black")
    draw.text((1,14),"Rr",fill="black")
    draw.text((1,24),"Yw",fill="black")
    draw.text((1,34),"Gr",fill="black")
    draw.text((1,44),"Bu",fill="black")
    draw.text((1,54),"Bk",fill="black")

    #draw.text((0, 0),"123456789012345678901\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11", fill="black")
    #draw.rectangle((1,1,126,62),outline="black",fill="black")
    #draw.text((10,10),"White",fill="white")
sleep(10)
