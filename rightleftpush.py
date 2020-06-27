import sys

from gpiozero import Button
from signal import pause

#a rotating button
def a_right_pressed():
    if a_left.is_pressed:
        print('a left')

a_right = Button(27)
a_right.when_pressed = a_right_pressed

def a_left_pressed():
    if a_right.is_pressed:
        print('a right')

a_left = Button(22)
a_left.when_pressed = a_left_pressed

def a_button_pressed():
    print('a button push')

a_button = Button(10)
a_button.when_pressed = a_button_pressed

#b rotating button
def b_right_pressed():
    if b_left.is_pressed:
        print('b left')

b_right = Button(20)
b_right.when_pressed = b_right_pressed

def b_left_pressed():
    if b_right.is_pressed:
        print('b right')

b_left = Button(16)
b_left.when_pressed = b_left_pressed

def b_button_pressed():
    print('b button push')

b_button = Button(21)
b_button.when_pressed = b_button_pressed

pause()

# test other

