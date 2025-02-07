#!/bin/python
import puzzle_functions
import threading
from time import time, sleep, localtime
from gpiozero import Button
import tm1637
red_led = tm1637.TM1637(clk=17,dio=4)



def commission_test_repair_button(button_name,pin_number):
    sleep(.5)
    button = Button(pin_number)
    def button_pressed():
        print(button_name+' pressed')
    button.when_pressed = button_pressed
    print('press ' +button_name)
    while not button.wait_for_press(3):
        del button
        button = Button(pin_number)
        button.when_pressed = button_pressed
        print(button_name+' repaired')
    return button

yellow_button = commission_test_repair_button('yellow button',19)
red_button = commission_test_repair_button('red button',26)

def commission_test_repair_switch(switch_name,pin_number):
    sleep(.5)
    button = Button(pin_number)
    def switch_up():
        print(switch_name+' up')
    button.when_pressed = switch_up
    def switch_down():
        print(switch_name+' down')
    button.when_released = switch_down
    print('test ' +switch_name)
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

# clock mode
def clock_mode():
    from time import time, sleep, localtime
    red_led.brightness(val=1) #0 through 7
    showColon = True
    def displayTM(disp,tim,hrs,colondsp):
        hour = tim.tm_hour
        minute = tim.tm_min
        if hrs == '12':
            hour = (tim.tm_hour % 12) or 12
        disp.show("%02d%02d" %(hour, minute),colon=colondsp)
    while switch_1.is_pressed:
        cur = time()
        ct  = localtime(cur)
        displayTM(red_led,ct,'12',showColon)
        sleep(0.5)
        showColon = not showColon
    red_led.write([0, 0, 0, 0])
    red_led.brightness(val=7) #0 through 7

def wall_time_clock_mode():
    global walltime
    from time import time, sleep, localtime
    red_led.brightness(val=1) #0 through 7
    showColon = True
    def displayTM(disp,tim,hrs,colondsp):
        hour = tim.tm_hour
        minute = tim.tm_min
        if hrs == '12':
            hour = (tim.tm_hour % 12) or 12
        disp.show("%02d%02d" %(hour, minute),colon=colondsp)
    while switch_2.is_pressed:
        ct  = localtime(walltime)
        displayTM(red_led,ct,'12',showColon)
        sleep(0.5)
        showColon = not showColon
    red_led.write([0, 0, 0, 0])
    red_led.brightness(val=7) #0 through 7


global walltime
walltime = time()

def wall_voltage_falling():
    def tmp():
        global walltime
        walltime = walltime + 1/60
    yellow_button.when_pressed = tmp

wall_voltage_falling_thread = threading.Thread(target=wall_voltage_falling)
wall_voltage_falling_thread.start()


def fibonacci_countdown_mode():
    from time import sleep
    red_led.brightness(val=1) #0 through 7
    showColon = True
    def countdown(red_led,t):
        while t:
            mins, secs = divmod(t, 60)
            red_led.numbers(mins, secs, True)
            sleep(1)
            t = t - 1
        red_led.numbers(0, 0, True)
    fibs = [1,5,8,13,21,34,55,89]
    options =          ["         1         ","         5         ","         8       ","        13        ","        21        ","        34        ","        55        ","        89        "]
    option_responces = ["    you have\n    Selected\n      1","    you have\n    Selected\n      5","    you have\n    Selected\n    8","    you have\n    Selected\n      13","    you have\n    Selected\n      21","    you have\n    Selected\n      34","    you have\n    Selected\n      55","    you have\n    Selected\n      89"]
    title_rows = [" Select focus time ","  duration   ","(use left nob & push)"]
    while switch_2.is_pressed:
        print("got here")
        #fails because a_combo is not visible in rotate multiselected
        rotate_lcd_multiselect = puzzle_functions.rotate_lcd_multiselect
        fibselected = rotate_lcd_multiselect(lcd_screen,a_combo,options,option_responces,title_rows)
        print("got here too")
        countdown(red_led,60*fibs[fibselected])
    red_led.write([0, 0, 0, 0])
    red_led.brightness(val=7) #0 through 7


def main(yellow_button_local,red_button_local,switch_1_local,switch_2_local,red_led_local):
    from luma.core.render import canvas
    from time import time, sleep, localtime
    global red_led
    red_led = red_led_local
    global yellow_button
    yellow_button = yellow_button_local
    global red_button
    red_button = red_button_local
    global switch_1
    switch_1 = switch_1_local
    global switch_2
    switch_2 = switch_2_local
    
    switch_1.when_pressed = clock_mode
    switch_2.when_pressed = wall_time_clock_mode
    red_button.wait_for_press()
    
if __name__ == "__main__":
    #from systemtest import red_led,lcd_screen,switches,buttons,a_combo,b_combo
    main(yellow_button,red_button,switch_1,switch_2,red_led)   
    
    