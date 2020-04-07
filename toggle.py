import sys

from gpiozero import Button
from signal import pause

def switch_1_up():
   print('switch 1 up')

def switch_1_down():
   print('switch 1 down')

switch_1 = Button(14)
switch_1.when_pressed = switch_1_up
switch_1.when_released = switch_1_down

def switch_2_up():
   print('switch 2 up')

def switch_2_down():
   print('switch 2 down')

switch_2 = Button(15)
switch_2.when_pressed = switch_2_up
switch_2.when_released = switch_2_down

def switch_3_up():
   print('switch 3 up')

def switch_3_down():
   print('switch 3 down')

switch_3 = Button(18)
switch_3.when_pressed = switch_3_up
switch_3.when_released = switch_3_down

def switch_4_up():
   print('switch 4 up')

def switch_4_down():
   print('switch 4 down')

switch_4 = Button(23)
switch_4.when_pressed = switch_4_up
switch_4.when_released = switch_4_down

def switch_5_up():
   print('switch 5 up')

def switch_5_down():
   print('switch 5 down')

switch_5 = Button(24)
switch_5.when_pressed = switch_5_up
switch_5.when_released = switch_5_down

def switch_6_up():
   print('switch 6 up')

def switch_6_down():
   print('switch 6 down')

switch_6 = Button(25)
switch_6.when_pressed = switch_6_up
switch_6.when_released = switch_6_down

def switch_7_up():
   print('switch 7 up')

def switch_7_down():
   print('switch 7 down')

switch_7 = Button(8)
switch_7.when_pressed = switch_7_up
switch_7.when_released = switch_7_down

def switch_8_up():
   print('switch 8 up')

def switch_8_down():
   print('switch 8 down')

switch_8 = Button(7)
switch_8.when_pressed = switch_8_up
switch_8.when_released = switch_8_down

def switch_9_up():
   print('switch 9 up')

def switch_9_down():
   print('switch 9 down')

switch_9 = Button(12)
switch_9.when_pressed = switch_9_up
switch_9.when_released = switch_9_down

pause()

# test other

