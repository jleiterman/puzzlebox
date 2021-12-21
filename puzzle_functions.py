#!/usr/bin/python3
# binary toggle uses the nine toggle switches as binary inputs and displayes
# the corresponding number to the red led.  The code to input is target number
# the display on success is the second argument

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import Button
from signal import pause
from time import time, sleep, localtime

def binary_toggle(target_number,success_message):
    
    global binary_toggle_puzzle_solved
    binary_toggle_puzzle_solved = False
    
    def display_solution():
        red_led.scroll(success_message)
        red_led.scroll(success_message)
        red_led.scroll(success_message)
    
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

# example usage
#binary_toggle_thread = threading.Thread(target=binary_toggle,args=(237,"you successfully entered the binary toggle"))
#binary_toggle_thread.start()


def pushbutton_sequence(lcd_screen,buttons,input_sequence):
    yellow_button = buttons[0]
    green_button  = buttons[1]
    blue_button   = buttons[2]
    black_button  = buttons[3]
    red_button    = buttons[4]
    white_button  = buttons[5]
    
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
            lcd_text("Correct\n    sequence")
            pushbutton_puzzle_solved = True
            sequence_position = 0
    
    while not pushbutton_puzzle_solved:
        sleep(1)


#pushbutton_sequence_thread = threading.Thread(target=pushbutton_sequence,args=(lcd_screen,buttons,['red','green','red'])) 
#pushbutton_sequence_thread.start()

def combination_lock(lcd_screen,combo,lock_combination,success_string):
    print("combo version2")
    right  = combo[0]
    left   = combo[1]
    button = combo[2]
    global combination_state 
    combination_state = []
    global lock_solved
    lock_solved = False
    lock_combination = list(lock_combination)
    
    def lcd_combination_state():
        with canvas(lcd_screen) as draw:
            combination_state_string = ''.join([('R' if i%2 == 0 else 'L') + str(combination_state[i]) + ' ' for i in range(len(combination_state))])
            combination_state_string = combination_state_string + '\npush to enter'
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((20, 20), combination_state_string, fill="white")
    
    def lcd_combination_success():
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), success_string, fill="white")
            
    def left_test():
        if left.is_pressed:
            print('a left')
            update_lock('left')
    right.when_pressed = left_test
    
    def right_test():
        if right.is_pressed:
            print('a right')
            update_lock('right')
    left.when_pressed = right_test
    
    def button_pressed():
        print('a button push')
        update_lock('enter')
    button.when_pressed = button_pressed
    
    def update_lock(input):
        global combination_state
        global lock_solved
        if input == 'enter':
            if combination_state == list(lock_combination):
                print('congratulaitons')
                lock_solved = True
                lcd_combination_success()
            else:
                combination_state = []
                lcd_combination_state()
        if len(combination_state) == 0 and input == 'left':
            combination_state = []
        else:
            if (len(combination_state) % 2) == 1:
                if input == 'right':
                    combination_state[len(combination_state)-1] = combination_state[len(combination_state)-1]+1
                    lcd_combination_state()
                elif input == 'left':
                    combination_state.append(1)
                    lcd_combination_state()
            else:
                if input == 'left':
                    combination_state[len(combination_state)-1] = combination_state[len(combination_state)-1]+1
                    lcd_combination_state()
                    if combination_state[len(combination_state)-1] > 60:
                        combination_state = []
                        lcd_combination_state()
                elif input == 'right':
                    combination_state.append(1)
                    lcd_combination_state()
        print(combination_state)
    
    while lock_solved != True:
        sleep(1)

#combination_lock_thread = threading.Thread(target=combination_lock,args=(right, left, button, lcd_screen, [2,11,20],'you win'))
#combination_lock_thread.start()



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

##countdown_thread = threading.Thread(target=countdown,args=(red_led,3600))
##countdown_thread.start()


# log uptime was developed to test battery use time
def loguptime():
    while True:
        f = open('loguptime.txt', 'a')
        f.write(datetime.datetime.now().strftime("%Y %m %d %H:%M:%S"))
        f.write('\n')
        f.close()
        sleep(60)

#loguptime_thread = threading.Thread(target=loguptime)
#loguptime_thread.start()



def switch_combo(red_led,switches,switch_sequence,switch_up_text,switch_down_text,success_message):
    global switch_combo_puzzle_solved
    switch_combo_puzzle_solved = False
    switch_1 = switches[0]
    switch_2 = switches[1]
    switch_3 = switches[2]
    switch_4 = switches[3]
    switch_5 = switches[4]
    switch_6 = switches[5]
    switch_7 = switches[6]
    switch_8 = switches[7]
    switch_9 = switches[8]
    
    global sequence
    global sequence_position
    global switch_puzzle_solved
    sequence = switch_sequence
    sequence_position = 0
    switch_puzzle_solved = False
    print(sequence)
    
    def display_success():
        red_led.scroll(success_message)
        red_led.scroll(success_message)
        red_led.scroll(success_message)
    
    for i in range(len(switches)):
        def switchup(i):
            def switchupinner():
                print(str(i+1)+' up')
                if switch_up_text[i] != '':
                    red_led.scroll(switch_up_text[i])
                update_sequence_position(str(i+1)+' up')
            return switchupinner
        if not switch_up_text[i] == 'skip this switch':
            switches[i].when_pressed = switchup(i)
        def switchdown(i):
            def switchdowninner():
                print(str(i+1)+' down')
                if switch_down_text[i] != '':
                    red_led.scroll(switch_down_text[i])
                update_sequence_position(str(i+1)+' down')
            return switchdowninner
        if not switch_up_text[i] == 'skip this switch':
            switches[i].when_pressed = switchup(i)
    
    def update_sequence_position(switch_action):
        global sequence
        global sequence_position
        global pushbutton_puzzle_solved
        if sequence[sequence_position] == switch_action:
            sequence_position = sequence_position + 1
        else:
            sequence_position = 0
        print('sequence position {:02d}'.format(sequence_position))
        if sequence_position == len(sequence):
            pushbutton_puzzle_solved = True
            display_success()
    
    while sequence_position < len(sequence):
        sleep(1)

def rotate_lcd_multiselect(lcd_screen,button_combo,options,option_responces,title_rows):
    
    global switch_puzzle_solved
    switch_puzzle_solved = False
    
    print("rotate_lcd_multiselect")
    right  = button_combo[0]
    left   = button_combo[1]
    button = button_combo[2]
    global multiselected
    multiselected = 0
    
    def lcd_text(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((20, 10), text, fill="white")
    
    def draw_lcd_multiselect(lcd_screen,options):
        print("got to draw_lcd_multiselect")
        print("multiselected")
        print(multiselected)
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="black", fill="black")
            draw.rectangle((0,0,127,27),outline="white",fill="white")
            draw.text((1, 0),title_rows[0], fill="black")
            draw.text((1, 9),title_rows[1], fill="black")
            draw.text((1,18),title_rows[2], fill="black")
            draw.rectangle((0,34,127,43),outline="black",fill="black")
            draw.text((1,34),options[multiselected-1],fill="white")
            draw.rectangle((0,44,127,53),outline="white",fill="white")
            draw.text((1,44),options[multiselected],fill="black")
            draw.rectangle((0,54,127,63),outline="black",fill="black")
            if multiselected+1 == len(options):
                draw.text((1,54),options[0],fill="white")
            else:
                draw.text((1,54),options[multiselected+1],fill="white")

    def update_multiselect(lcd_screen,options):
        global multiselected
        print(multiselected)
        if left.value == 0:
            if multiselected+1 == len(options):
                multiselected = 0
            else:
                multiselected = multiselected + 1
        elif left.value == 1:
            if multiselected == 0:
                multiselected = len(options) -1
            else:
                multiselected = multiselected - 1
        else:
            print("it should not have come to this one_or_neg_one is not one or negative one")
        draw_lcd_multiselect(lcd_screen,options)
        print(multiselected)
    
    def update_multiselect_wrapper():
        update_multiselect(lcd_screen,options)
    
    right.when_pressed = update_multiselect_wrapper
    left.when_pressed  = update_multiselect_wrapper
    
    def multiselect_selected():
        global switch_puzzle_solved
        lcd_text(option_responces[multiselected])
        switch_puzzle_solved = True
    
    button.when_pressed = multiselect_selected
    
    draw_lcd_multiselect(lcd_screen,options)
    
    while not switch_puzzle_solved:
        print("tick")
        sleep(1)
    
    def donothing():
        do = "nothing"
    
    right.when_pressed  = donothing
    left.when_pressed   = donothing
    button.when_pressed = donothing
    
    print("ending")
    print(multiselected)
    return multiselected