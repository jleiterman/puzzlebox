import sys
import time
import os
import tm1637
import threading
import datetime

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import Button
from signal import pause
from time import time, sleep, localtime

from systemtest import *
import puzzle_functions
from importlib import reload
puzzle_functions = reload(puzzle_functions)
combination_lock = puzzle_functions.combination_lock

def system_on():
    lcd_text('System Loading\n\n  please wait')
    red_led.scroll('ON             ON            ON')
    lcd_text('Welcome authenticate\nby using toggle\nswitch sequence')

switch_1.when_pressed = system_on

def system_off():
    lcd_text('System Shutdown')
    red_led.scroll('off')
    with canvas(lcd_screen) as draw:
        draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")

switch_1.when_released = system_off

switch_up_text = ['power on','blitzen','comet','cupid','dancer','dasher','donner','prancer','vixen']
switch_down_text = ['power off',' ',' ',' ',' ',' ',' ',' ',' ']
switch_sequence = ['6 up','5 up','8 up','9 up','3 up','4 up','7 up','2 up']

#puzzle_functions = reload(puzzle_functions)
#switch_combo = puzzle_functions.switch_combo
sc = threading.Thread(target=switch_combo,args=(red_led,switches,switch_sequence,switch_up_text,switch_down_text,'it worked'))
sc.start()
switch_1.when_pressed = system_on
switch_1.when_released = system_off

