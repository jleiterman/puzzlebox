#!/usr/bin/python3

# test file to run system test.

# first test is to ensure that needed libraries load
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

global countdown_nodisplay_time
countdown_nodisplay_time = 0

def binary_toggle(target_number,clue_number):
    
    global binary_toggle_puzzle_solved
    binary_toggle_puzzle_solved = False
    
    def display_solution():
        red_led.scroll('lock code {:03d}'.format(clue_number))
        red_led.scroll('lock code {:03d}'.format(clue_number))
        red_led.scroll('lock code {:03d}'.format(clue_number))
    
    def switch_change():
        global countdown_nodisplay_time
        global binary_toggle_puzzle_solved
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
        countdown_nodisplay_time = 17
        red_led.number(display_number)
        if display_number == target_number:
            binary_toggle_puzzle_solved = True
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

    while binary_toggle_puzzle_solved == False:
        sleep(1)

binary_toggle_thread = threading.Thread(target=binary_toggle,args=(237,104))
binary_toggle_thread.start()


def pushbutton_sequence(*input_sequence):

    global sequence
    global sequence_position
    global pushbutton_puzzle_solved
    sequence = input_sequence
    sequence_position = 0
    pushbutton_puzzle_solved = False

    def lcd_text(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((20, 10), text, fill="white")
    
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
        global pushbutton_puzzle_solved
        if sequence[sequence_position] == button_color:
            sequence_position = sequence_position + 1
        else:
            sequence_position = 0
        print('sequence position {:02d}'.format(sequence_position))
        if sequence_position == len(sequence):
            lcd_text("CONGRATUATIONS\n    YOU WIN!")
            pushbutton_puzzle_solved = True
            sequence_position = 0

    while sequence_position < len(sequence):
        sleep(1)


pushbutton_sequence_thread = threading.Thread(target=pushbutton_sequence,args=(['red','green','black','white','yellow','white','black','blue']))
pushbutton_sequence_thread.start()


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
            combination_success_string = '125 plus\nsomething else' 
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

combination_lock_a_thread = threading.Thread(target=combination_lock_a,args=([11,23,19]))
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
            combination_success_string = '643 plus\nsometing else' 
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

combination_lock_b_thread = threading.Thread(target=combination_lock_b,args=([2,11,20]))
combination_lock_b_thread.start()


def countdown(red_led,t):
    global countdown_nodisplay_time
    while t:
        mins, secs = divmod(t, 60)
        if countdown_nodisplay_time <= 0:
            red_led.numbers(mins, secs, True)
        #timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r")
        sleep(1)
        if not(binary_toggle_puzzle_solved & lock_solved_a & lock_solved_b & pushbutton_puzzle_solved):
            t = t - 1
        countdown_nodisplay_time = countdown_nodisplay_time - 1
    with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((30, 10), 'TIME IS UP\nYOU LOOSE!', fill="white")
    red_led.numbers(0, 0, True)

countdown_thread = threading.Thread(target=countdown,args=(red_led,3600))
countdown_thread.start()

def loguptime():
    while True:
        f = open('loguptime.txt', 'a')
        f.write(datetime.datetime.now().strftime("%Y %m %d %H:%M:%S"))
        f.write('\n')
        f.close()
        sleep(60)

loguptime_thread = threading.Thread(target=loguptime)
loguptime_thread.start()



