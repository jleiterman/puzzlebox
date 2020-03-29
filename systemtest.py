#!/usr/bin/python3

# test file to run system test.
import sys
import time
import os
import tm1637

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import Button
from signal import pause

# first test is to ensure that needed libraries load

# test switches

# test displayes
#Red LED display
tm = tm1637.TM1637(clk=17,dio=4)
tm.scroll('all your base are belong to us')

#White LCD screen
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 10), "All Your Base are\nbelong to us!", fill="white")
time.sleep(10)

# test buttons

def red_button_pressed():
    print('Red button was pressed.')
    tm.scroll('Red')

red_button = Button(26)
red_button.when_pressed = red_button_pressed

def yellow_button_pressed():
    print('Yellow button was pressed.')
    tm.scroll('Yellow')

yellow_button = Button(19)
yellow_button.when_pressed = yellow_button_pressed

def green_button_pressed():
    print('Green button was pressed.')
    tm.scroll('Green')

green_button = Button(13)
green_button.when_pressed = green_button_pressed

def blue_button_pressed():
    print('Blue button was pressed.')
    tm.scroll('Blue')

blue_button = Button(6)
blue_button.when_pressed = blue_button_pressed

def black_button_pressed():
    print('Black button was pressed.')
    tm.scroll('Black')

black_button = Button(5)
black_button.when_pressed = black_button_pressed

def white_button_pressed():
    print('White button was pressed.')
    tm.scroll('White')

white_button = Button(11)
white_button.when_pressed = white_button_pressed

pause()

# test other

