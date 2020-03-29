import sys

import tm1637
from gpiozero import Button
from signal import pause
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import Button

#Red LED display
display_number = 0
tm = tm1637.TM1637(clk=17,dio=4)
tm.number(display_number)

#White LCD screen
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

def display_solution():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((5, 5), "How does Dad come\nup with this stuff?\nThe KEY is a good\ncup of expresso!!",fill="white")

def switch_change():
    display_number = 0
    if switch_1.is_pressed:
        display_number = display_number + 512
    if switch_2.is_pressed:
        display_number = display_number + 256
    if switch_3.is_pressed:
        display_number = display_number + 128
    if switch_4.is_pressed:
        display_number = display_number + 64
    if switch_5.is_pressed:
        display_number = display_number + 32
    if switch_6.is_pressed:
        display_number = display_number + 16
    if switch_7.is_pressed:
        display_number = display_number + 8
    if switch_8.is_pressed:
        display_number = display_number + 4
    if switch_9.is_pressed:
        display_number = display_number + 2
    if switch_10.is_pressed:
        display_number = display_number + 1
    tm.number(display_number)
    if display_number == 708:
        display_solution()

switch_1 = Button(24)
switch_2 = Button(23)
switch_3 = Button(18)
switch_4 = Button(15)
switch_5 = Button(14)
switch_6 = Button(25)
switch_7 = Button(8)
switch_8 = Button(7)
switch_9 = Button(12)
switch_10 = Button(9)
switch_1.when_pressed = switch_change
switch_2.when_pressed = switch_change
switch_3.when_pressed = switch_change
switch_4.when_pressed = switch_change
switch_5.when_pressed = switch_change
switch_6.when_pressed = switch_change
switch_7.when_pressed = switch_change
switch_8.when_pressed = switch_change
switch_9.when_pressed = switch_change
switch_10.when_pressed = switch_change
switch_1.when_released = switch_change
switch_2.when_released = switch_change
switch_3.when_released = switch_change
switch_4.when_released = switch_change
switch_5.when_released = switch_change
switch_6.when_released = switch_change
switch_7.when_released = switch_change
switch_8.when_released = switch_change
switch_9.when_released = switch_change
switch_10.when_released = switch_change

pause()




pause()


