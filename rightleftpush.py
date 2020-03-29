import sys

from gpiozero import Button
from signal import pause

def red_button_pressed():
    print('red')
    if blue_button.is_pressed:
        print('Left')

red_button = Button(27)
red_button.when_pressed = red_button_pressed

def blue_button_pressed():
    print('blue')
    if red_button.is_pressed:
        print('Right')

blue_button = Button(22)
blue_button.when_pressed = blue_button_pressed

def a_button_pressed():
    print('push')

a_button = Button(10)
a_button.when_pressed = a_button_pressed

#b rotating button
def b_red_button_pressed():
    print('red')
    if b_blue_button.is_pressed:
        print('Left')

b_red_button = Button(20)
b_red_button.when_pressed = b_red_button_pressed

def b_blue_button_pressed():
    print('blue')
    if b_red_button.is_pressed:
        print('Right')

b_blue_button = Button(16)
b_blue_button.when_pressed = b_blue_button_pressed

def b_button_pressed():
    print('push')

b_button = Button(21)
b_button.when_pressed = b_button_pressed

pause()

# test other

