#!/usr/bin/python3

# This is a pushbutton sequence example

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


def pushbutton_sequence(input_sequence):

    global sequence
    global sequence_position
    sequence = input_sequence
    sequence_position = 0
    puzzle_unsolved = True

    def lcd_text(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), text, fill="white")
    
    def red_button_pressed(self):
        print('Red button was pressed.')
        update_sequence_position('red')
    red_button.when_pressed = red_button_pressed
    
    def yellow_button_pressed():
        print('Yellow button was pressed.')
        update_sequence_position('yellow')
    yellow_button.when_pressed = yellow_button_pressed
    
    def green_button_pressed():
        print('Green button was pressed.')
        update_sequence_position('green')
    green_button.when_pressed = green_button_pressed
    
    def blue_button_pressed():
        print('Blue button was pressed.')
        update_sequence_position('blue')
    blue_button.when_pressed = blue_button_pressed
    
    def black_button_pressed():
        print('Black button was pressed.')
        update_sequence_position('black')
    black_button.when_pressed = black_button_pressed

    def white_button_pressed():
        print('White button was pressed.')
        update_sequence_position('white')
    white_button.when_pressed = white_button_pressed
    
    def update_sequence_position(button_color):
        global sequence
        global sequence_position
        global puzzle_unsolved
        if sequence[sequence_position] == button_color:
            sequence_position = sequence_position + 1
        else:
            sequence_position = 0
        print('sequence position {:02d}'.format(sequence_position))
        if sequence_position == len(sequence):
            lcd_text("You Got It!\n'next clue'")
            puzzle_unsolved = False

    while sequence_position < len(sequence):
        sleep(1)

pushbutton_sequence(['red','blue','green','blue'])