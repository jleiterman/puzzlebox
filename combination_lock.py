#!/usr/bin/python3

# test file to run system test.

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


def combination_lock_a(*lock_combination):

    global combination_state_a 
    combination_state_a = []
    global lock_solved_a
    lock_solved_a = False
    global lock_combination_a
    lock_combination_a = list(lock_combination)

    def lcd_combination_state_a():
        with canvas(lcd_screen) as draw:
            combination_state_a_string = ''.join([('R' if i%2 == 0 else 'L') + str(combination_state_a[i]) + ' ' for i in range(len(combination_state_a))])
            combination_state_a_string = combination_state_a_string + '\npush to enter'
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((20, 20), combination_state_a_string, fill="white")
    
    def lcd_combination_success():
        with canvas(lcd_screen) as draw:
            combination_success_string = 'Correct A\nThis is the next\nhint!' 
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), combination_success_string, fill="white")
            
    def a_left_test():
        if a_left.is_pressed:
            print('a left')
            update_lock('left')
    a_right.when_pressed = a_left_test
    
    def a_right_test():
        if a_right.is_pressed:
            print('a right')
            update_lock('right')
    a_left.when_pressed = a_right_test
    
    def a_button_pressed():
        print('a button push')
        update_lock('enter')
    a_button.when_pressed = a_button_pressed
    
    def update_lock(input):
        global combination_state_a
        global lock_solved_a
        if input == 'enter':
            if combination_state_a == list(lock_combination_a):
                print('congratulaitons')
                lock_solved_a = True
                lcd_combination_success()
            else:
                combination_state_a = []
                lcd_combination_state_a()
        if len(combination_state_a) == 0 and input == 'left':
            combination_state_a = []
        else:
            if (len(combination_state_a) % 2) == 1:
                if input == 'right':
                    combination_state_a[len(combination_state_a)-1] = combination_state_a[len(combination_state_a)-1]+1
                    lcd_combination_state_a()
                elif input == 'left':
                    combination_state_a.append(1)
                    lcd_combination_state_a()
            else:
                if input == 'left':
                    combination_state_a[len(combination_state_a)-1] = combination_state_a[len(combination_state_a)-1]+1
                    lcd_combination_state_a()
                    if combination_state_a[len(combination_state_a)-1] > 60:
                        combination_state_a = []
                        lcd_combination_state_a()
                elif input == 'right':
                    combination_state_a.append(1)
                    lcd_combination_state_a()
        print(combination_state_a)

    while lock_solved_a != True:
        sleep(1)

combination_lock_a_thread = threading.Thread(target=combination_lock_a,args=([10,4,4]))
combination_lock_a_thread.start()



def combination_lock_b(*lock_combination):

    global combination_state_b 
    combination_state_b = []
    global lock_solved_b
    lock_solved_b = False
    global lock_combination_b
    lock_combination_b = list(lock_combination)

    def lcd_combination_state_b():
        with canvas(lcd_screen) as draw:
            combination_state_b_string = ''.join([('R' if i%2 == 0 else 'L') + str(combination_state_b[i]) + ' ' for i in range(len(combination_state_b))])
            combination_state_b_string = combination_state_b_string + '\npush to enter'
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((20, 20), combination_state_b_string, fill="white")
    
    def lcd_combination_success():
        with canvas(lcd_screen) as draw:
            combination_success_string = 'Correct B\nThis is the next\nhint!' 
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), combination_success_string, fill="white")
            
    def b_left_test():
        if b_left.is_pressed:
            print('a left')
            update_lock('left')
    b_right.when_pressed = b_left_test
    
    def b_right_test():
        if b_right.is_pressed:
            print('a right')
            update_lock('right')
    b_left.when_pressed = b_right_test
    
    def b_button_pressed():
        print('a button push')
        update_lock('enter')
    b_button.when_pressed = b_button_pressed
    
    def update_lock(input):
        global combination_state_b
        global lock_solved_b
        if input == 'enter':
            if combination_state_b == list(lock_combination_b):
                print('congratulaitons')
                lock_solved_b = True
                lcd_combination_success()
            else:
                combination_state_b = []
                lcd_combination_state_b()
        if len(combination_state_b) == 0 and input == 'left':
            combination_state_b = []
        else:
            if (len(combination_state_b) % 2) == 1:
                if input == 'right':
                    combination_state_b[len(combination_state_b)-1] = combination_state_b[len(combination_state_b)-1]+1
                    lcd_combination_state_b()
                elif input == 'left':
                    combination_state_b.append(1)
                    lcd_combination_state_b()
            else:
                if input == 'left':
                    combination_state_b[len(combination_state_b)-1] = combination_state_b[len(combination_state_b)-1]+1
                    lcd_combination_state_b()
                    if combination_state_b[len(combination_state_b)-1] > 60:
                        combination_state_b = []
                        lcd_combination_state_b()
                elif input == 'right':
                    combination_state_b.append(1)
                    lcd_combination_state_b()
        print(combination_state_b)

    while lock_solved_b != True:
        sleep(1)

combination_lock_b_thread = threading.Thread(target=combination_lock_b,args=([1,4,4]))
combination_lock_b_thread.start()