#!/usr/bin/python3

# test file to run system test.

# first test is to ensure that needed libraries load
import sys
import time
import os
import tm1637

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
serial = i2c(port=1, address=0x3C)
lcd_screen = sh1106(serial)
#buttons
red_button = Button(26)
yellow_button = Button(19)
green_button = Button(13)
blue_button = Button(6)
black_button = Button(5)
white_button = Button(11)
#switches
switch_1 = Button(14)
switch_2 = Button(15)
switch_3 = Button(18)
switch_4 = Button(23)
switch_5 = Button(24)
switch_6 = Button(25)
switch_7 = Button(8)
switch_8 = Button(7)
switch_9 = Button(12)
#rotating buttons
a_right = Button(27)
a_left = Button(22)
a_button = Button(10)
b_right = Button(20)
b_left = Button(16)
b_button = Button(21)




def lcd_text(text):
    with canvas(lcd_screen) as draw:
        draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
        draw.text((10, 10), text, fill="white")

lcd_text("System Test\nresults displayed\nhere")

### test buttons ###

def red_button_pressed():
    print('Red button was pressed.')
    lcd_text("Red button\nwas pressed")
red_button.when_pressed = red_button_pressed

def yellow_button_pressed():
    print('Yellow button was pressed.')
    lcd_text("Yellow button\nwas pressed")
yellow_button.when_pressed = yellow_button_pressed

def green_button_pressed():
    print('Green button was pressed.')
    lcd_text("Green button\nwas pressed")
green_button.when_pressed = green_button_pressed

def blue_button_pressed():
    print('Blue button was pressed.')
    lcd_text("Blue button\nwas pressed")
blue_button.when_pressed = blue_button_pressed

def black_button_pressed():
    print('Black button was pressed.')
    lcd_text("Black button\nwas pressed")
black_button.when_pressed = black_button_pressed

def white_button_pressed():
    print('White button was pressed.')
    lcd_text("White button\nwas pressed")
white_button.when_pressed = white_button_pressed



###  TEST SWITCHES ###

def switch_1_up():
   print('switch 1 up')
   lcd_text("Switch 1 up")
switch_1.when_pressed = switch_1_up

def switch_1_down():
   print('switch 1 down')
   lcd_text("Switch 1 down")
switch_1.when_released = switch_1_down

def switch_2_up():
   print('switch 2 up')
   lcd_text("Switch 2 up")
switch_2.when_pressed = switch_2_up

def switch_2_down():
   print('switch 2 down')
   lcd_text("Switch 2 down")
switch_2.when_released = switch_2_down

def switch_3_up():
   print('switch 3 up')
   lcd_text("Switch 3 up")
switch_3.when_pressed = switch_3_up

def switch_3_down():
   print('switch 3 down')
   lcd_text("Switch 3 down") 
switch_3.when_released = switch_3_down

def switch_4_up():
   print('switch 4 up')
   lcd_text("Switch 4 up")
switch_4.when_pressed = switch_4_up

def switch_4_down():
   print('switch 4 down')
   lcd_text("Switch 4 down")
switch_4.when_released = switch_4_down
def switch_5_up():
   print('switch 5 up')
   lcd_text("Switch 5 up")
switch_5.when_pressed = switch_5_up

def switch_5_down():
   print('switch 5 down')
   lcd_text("Switch 5 down")
switch_5.when_released = switch_5_down

def switch_6_up():
   print('switch 6 up')
   lcd_text("Switch 6 up")
switch_6.when_pressed = switch_6_up

def switch_6_down():
   print('switch 6 down')
   lcd_text("Switch 6 down")
switch_6.when_released = switch_6_down

def switch_7_up():
   print('switch 7 up')
   lcd_text("Switch 7 up")
switch_7.when_pressed = switch_7_up

def switch_7_down():
   print('switch 7 down')
   lcd_text("Switch 7 down")
switch_7.when_released = switch_7_down

def switch_8_up():
   print('switch 8 up')
   lcd_text("Switch 8 up")
switch_8.when_pressed = switch_8_up

def switch_8_down():
   print('switch 8 down')
   lcd_text("Switch 8 down")
switch_8.when_released = switch_8_down

def switch_9_up():
   print('switch 9 up')
   lcd_text("Switch 9 up")
switch_9.when_pressed = switch_9_up

def switch_9_down():
   print('switch 9 down')
   lcd_text("Switch 9 down")
switch_9.when_released = switch_9_down


## Test Rotating Buttons ###

#a rotating button
def a_right_pressed():
    if a_left.is_pressed:
        print('a left')
        lcd_text("A Left")
a_right.when_pressed = a_right_pressed

def a_left_pressed():
    if a_right.is_pressed:
        print('a right')
        lcd_text("A Right")
a_left.when_pressed = a_left_pressed

def a_button_pressed():
    print('a button push')
    lcd_text("A pushed")
a_button.when_pressed = a_button_pressed

#b rotating button
def b_right_pressed():
    if b_left.is_pressed:
        print('b left')
        lcd_text("B Left")
b_right.when_pressed = b_right_pressed

def b_left_pressed():
    if b_right.is_pressed:
        print('b right')
        lcd_text("B Right")
b_left.when_pressed = b_left_pressed

def b_button_pressed():
    print('b button push')
    lcd_text("B pushed")
b_button.when_pressed = b_button_pressed


# start the countdown timer

def countdown(red_led,t):
    while t:
        mins, secs = divmod(t, 60)
        red_led.numbers(mins, secs, True)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1
    print("System Test complete")
    lcd_text("System Test\nComplete")
    red_led.numbers(0, 0, True)

countdown(red_led,t=400)
