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

global debug_on
debug_on = True

#note 2021-11-29 found that there is a random failure in buttons working related to software.
#to correct we can delete the button with `del button_[x]` and then recreate the button and 
#then re run the button action to function mapping `button_[x].when_pressed = function`
#can not find test to see that it is not working other than manual test of the physical switch
#Idea to correct is to build a button push to exit each of the mapping steps.


# setup input-output
#Red LED display
red_led = tm1637.TM1637(clk=17,dio=4)
#White LCD screen
serial = i2c(port=1, address=0x3C)
lcd_screen = sh1106(serial)

def lcd_text(text):
    with canvas(lcd_screen) as draw:
        draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
        draw.text((10, 10), text, fill="white")

lcd_text("System Test\nresults displayed\nhere")

### test buttons ###

def commission_test_repair_button(button_name,pin_number):
    sleep(.5)
    button = Button(pin_number)
    def button_pressed():
        print(button_name+' pressed')
        lcd_text(button_name+'\nwas pressed')
    button.when_pressed = button_pressed
    print('press ' +button_name)
    lcd_text('press ' +button_name)
    while not button.wait_for_press(3):
        del button
        button = Button(pin_number)
        button.when_pressed = button_pressed
        print(button_name+' repaired')
    return button

red_button = commission_test_repair_button('red button',26)
yellow_button = commission_test_repair_button('yellow button',19)
green_button = commission_test_repair_button('green button',13)
blue_button = commission_test_repair_button('blue button',6)
black_button = commission_test_repair_button('black button',5)
white_button = commission_test_repair_button('white button',11)

###  TEST SWITCHES ###

def commission_test_repair_switch(switch_name,pin_number):
    sleep(.5)
    button = Button(pin_number)
    def switch_up():
        print(switch_name+' up')
        lcd_text(switch_name+' up')
    button.when_pressed = switch_up
    def switch_down():
        print(switch_name+' down')
        lcd_text(switch_name+' down')
    button.when_released = switch_down
    print('test ' +switch_name)
    lcd_text('test ' +switch_name)
    if button.wait_for_press(3):
        if button.wait_for_release(3):
            print("it works")
            return button
        else:
            print("it failed release")
            del button
            return commission_test_repair_switch(switch_name,pin_number)
    else:
        print("it failed press")
        del button
        return commission_test_repair_switch(switch_name,pin_number)

switch_1 = commission_test_repair_switch('switch 1',14)
switch_2 = commission_test_repair_switch('switch 2',15)
switch_3 = commission_test_repair_switch('switch 3',18)
switch_4 = commission_test_repair_switch('switch 4',23)
switch_5 = commission_test_repair_switch('switch 5',24)
switch_6 = commission_test_repair_switch('switch 6',25)
switch_7 = commission_test_repair_switch('switch 7',8)
switch_8 = commission_test_repair_switch('switch 8',7)
switch_9 = commission_test_repair_switch('switch 9',12)

## Test Rotating Buttons ###


def commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number):
    sleep(.5)
    right = Button(right_pin_number)
    left = Button(left_pin_number)
    button = Button(button_pin_number)
    def left_test():
        if left.is_pressed:
            print(button_name+' left')
            lcd_text(button_name+' left')
    right.when_pressed = left_test
    def right_test():
        if right.is_pressed:
            print(button_name+' right')
            lcd_text(button_name+' right')
    left.when_pressed = right_test
    def button_pressed():
        print(button_name+' pushed')
        lcd_text(button_name+' pushed')
    button.when_pressed = button_pressed

    print('test ' +button_name+' right left press')
    lcd_text('test ' +button_name+'\nright left\n press')
    if left.wait_for_press(3):
        if right.is_pressed:
            if right.wait_for_press(3):
                if left.is_pressed:
                    if button.wait_for_press(3):
                        print("it works")
                        return right, left, button;
                    else:
                        del right, left, button;
                        return commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number) 
                else:
                    del right, left, button;
                    return commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number) 
            else:
                del right, left, button;
                return commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number) 
        else:
            del right, left, button;
            return commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number)             

    else:
        del right, left, button;
        return commission_test_repair_roating_button(button_name,right_pin_number,left_pin_number,button_pin_number) 

a_right, a_left, a_button = commission_test_repair_roating_button('a',27,22,10)
b_right, b_left, b_button = commission_test_repair_roating_button('b',20,16,21)



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

countdown(red_led,t=10)
