import threading
#
import puzzle_functions
from importlib import reload
#from systemtest import *
    
def main(red_led,lcd_screen,switches,buttons,a_combo,b_combo):
    from luma.core.render import canvas
    from time import time, sleep, localtime
    
    switch_1 = switches[0]
    switch_2 = switches[1]
    switch_3 = switches[2]
    switch_4 = switches[3]
    switch_5 = switches[4]
    switch_6 = switches[5]
    switch_7 = switches[6]
    switch_8 = switches[7]
    switch_9 = switches[8]
    
    yellow_button = buttons[0]
    green_button  = buttons[1]
    blue_button   = buttons[2]
    black_button  = buttons[3]
    red_button    = buttons[4]
    white_button  = buttons[5]
    
    a_right  = a_combo[0]
    a_left   = a_combo[1]
    a_button = a_combo[2]
    b_right  = b_combo[0]
    b_left   = b_combo[1]
    b_button = b_combo[2]
    
    def lcd_text(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), text, fill="white")

    def lcd_text_4line(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 5), text, fill="white")

    # def system_on():
        # lcd_text('System Loading\n\n  please wait')
        # red_led.scroll('ON             ON            ON')
        # lcd_text_4line('WELCOME!\nauthenticate\nby entering toggle\nswitch sequence')

    # switch_1.when_pressed = system_on

    # dropping system off until we can get the whole script to start form beginning on restart
    # def system_off():
        # lcd_text('System Shutdown')
        # red_led.scroll('off')
        # lcd_screen.clear()

    # switch_1.when_released = system_off
    lcd_text('to win press\n\n  red_button')
    red_button.wait_for_press()
    lcd_text('\nYou WIN')
    
 
    sleep(10)



if __name__ == "__main__":
    from systemtest import *
    main(red_led,lcd_screen,switches,buttons,a_combo,b_combo)
