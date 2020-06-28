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

def binary_toggle(target_number,clue_number):
    
    global puzzle_solved
    puzzle_solved = False
    
    def display_solution():
        red_led.scroll('solution {:03d}'.format(clue_number))
        red_led.scroll('solution {:03d}'.format(clue_number))
        red_led.scroll('solution {:03d}'.format(clue_number))
    
    def switch_change():
        global puzzle_solved
        display_number = 0
        if switch_1.is_pressed:
            display_number = display_number + 256
        if switch_2.is_pressed:
            display_number = display_number + 128
        if switch_3.is_pressed:
            display_number = display_number + 64
        if switch_4.is_pressed:
            display_number = display_number + 32
        if switch_5.is_pressed:
            display_number = display_number + 16
        if switch_6.is_pressed:
            display_number = display_number + 8
        if switch_7.is_pressed:
            display_number = display_number + 4
        if switch_8.is_pressed:
            display_number = display_number + 2
        if switch_9.is_pressed:
            display_number = display_number + 1
        red_led.number(display_number)
        if display_number == target_number:
            puzzle_solved = True
            display_solution()
    
    switch_1.when_pressed = switch_change
    switch_2.when_pressed = switch_change
    switch_3.when_pressed = switch_change
    switch_4.when_pressed = switch_change
    switch_5.when_pressed = switch_change
    switch_6.when_pressed = switch_change
    switch_7.when_pressed = switch_change
    switch_8.when_pressed = switch_change
    switch_9.when_pressed = switch_change
    switch_1.when_released = switch_change
    switch_2.when_released = switch_change
    switch_3.when_released = switch_change
    switch_4.when_released = switch_change
    switch_5.when_released = switch_change
    switch_6.when_released = switch_change
    switch_7.when_released = switch_change
    switch_8.when_released = switch_change
    switch_9.when_released = switch_change

    while puzzle_solved == False:
        sleep(1)
    
binary_toggle(210,159)