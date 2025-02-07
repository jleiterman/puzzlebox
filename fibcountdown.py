from systemtest import red_led,lcd_screen,switches,buttons,a_combo,b_combo

def fibonacci_countdown_mode():
    from time import sleep
    from puzzle_functions import rotate_lcd_multiselect
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
    while True:
        print("got here")
        fibselected = rotate_lcd_multiselect(lcd_screen,a_combo,options,option_responces,title_rows)
        print("got here too")
        countdown(red_led,60*fibs[fibselected])
    red_led.write([0, 0, 0, 0])
    red_led.brightness(val=7) #0 through 7

fibonacci_countdown_mode()


