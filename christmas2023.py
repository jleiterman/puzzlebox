def step_down():
    global pos
    global virtual
    global lcd_screen
    x, y = pos
    if virtual.height > lcd_screen.height:
        if y < virtual.height - lcd_screen.height - int(lcd_screen.height/3):
            y += int(lcd_screen.height/3)
            virtual.set_position((x, y))
    pos=(x,y)
    print(pos)


def step_right():
    global pos
    global virtual
    global lcd_screen
    x, y = pos
    if virtual.width > lcd_screen.width:
        if x < virtual.width - lcd_screen.width - int(lcd_screen.width/3):
            x += int(lcd_screen.width/3)
            virtual.set_position((x, y))
    pos=(x,y)
    print(pos)


def step_up():
    global pos
    global virtual
    global lcd_screen
    x, y = pos
    if y >= int(lcd_screen.height/3):
        y -= int(lcd_screen.height/3)
        virtual.set_position((x, y))
    pos=(x,y)
    print(pos)


def step_left():
    global pos
    global virtual
    global lcd_screen
    x,y = pos
    if x >= int(lcd_screen.width/3):
        x -= int(lcd_screen.width/3)
        virtual.set_position((x, y))
    pos = (x, y)
    print(pos)

from luma.core.render import canvas
def lcd_text_4line(text):
    global lcd_screen
    with canvas(lcd_screen) as draw:
        draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
        draw.text((5, 5), text, fill="white")



def main(displays,switches,buttons,a_combo,b_combo):
    global lcd_screen
    lcd_screen = displays[0]
    red_led = displays[1]
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
    pushed_buttons = ['gray','gray','gray']
    
    def yellow_button_pressed():
        pushed_buttons.append('yellow')
    yellow_button.when_pressed = yellow_button_pressed
    
    def green_button_pressed():
        pushed_buttons.append('green')
    green_button.when_pressed = green_button_pressed
    
    def blue_button_pressed():
        pushed_buttons.append('blue')
    blue_button.when_pressed = blue_button_pressed
    
    def black_button_pressed():
        pushed_buttons.append('black')
    black_button.when_pressed = black_button_pressed
    
    def red_button_pressed(self):
        pushed_buttons.append('red')
    red_button.when_pressed = red_button_pressed
    
    def white_button_pressed():
        pushed_buttons.append('white')
    white_button.when_pressed = white_button_pressed
    
    a_right  = a_combo[0]
    a_left   = a_combo[1]
    a_button = a_combo[2]
    b_right  = b_combo[0]
    b_left   = b_combo[1]
    b_button = b_combo[2]
    
    from importlib import reload
    from time import sleep
    from PIL import Image
    from luma.core.virtual import viewport
    from PIL import Image
    #global lcd_screen
    pixel_art = Image.open('/home/pi/puzzlebox/LittleOrphanAnnie.png').convert(lcd_screen.mode)
    w,h =pixel_art.size
    global virtual
    virtual = viewport(lcd_screen, width=w, height=h)
    virtual.display(pixel_art)
    global pos
    pos = (2528, 655)
    virtual.set_position(pos)
    a_right.when_pressed = step_right
    a_left.when_pressed = step_left
    b_right.when_pressed = step_up
    b_left.when_pressed = step_down
    
    solvecount = 0
    button_puzzle_solved = False
    switch_puzzle_solved = False
    nob_puzzle_solved    = False
    solvecount = button_puzzle_solved + switch_puzzle_solved + nob_puzzle_solved
    pushed_buttons = ['gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray','gray']
    while not solvecount == 3:
        #21 color sequence for all 4 wheels 8 color sequence for front wheels only
        #button_puzzle_solved = ['yellow','green','green','red','red','blue','white','black','red','black','black','green','yellow','blue','green','black','yellow','white','blue','white','red'] == pushed_buttons[-21:]
        button_puzzle_solved = ['yellow','red','red','white','black','green','green','black'] == pushed_buttons[-8:]
        switch_puzzle_solved = [1,0,0,0,1,1,0,1,0] == [switch_1.value,switch_2.value,switch_3.value,switch_4.value,switch_5.value,switch_6.value,switch_7.value,switch_8.value,switch_9.value]
        nob_puzzle_solved    = (pos == (1730,1390))
        # solve position
        solvecount = button_puzzle_solved + switch_puzzle_solved + nob_puzzle_solved
        lines = [0,1,65,73][solvecount]
        red_led.write([lines,lines,lines,lines])
        sleep(0.5)
    #red_led.scroll('prepair for transmission of special christmas message')
    lcd_text_4line('    Prepair for\n  transmission of\n special Christmas\n      message!')
    sleep(10)
    encoderring = {"a": 2, "b": 4, "c": 7, "d": 5, "e": 9, "f": 6, "g": 8, "h": 10, "i": 24, "j": 1, "k": 25, "l": 15, "m": 14, "n": 12, "o": 13, "p": 3, "q": 11, "r": 16, "s": 17, "t": 23, "u": 26, "v": 21, "w": 19, "x": 18, "y": 20, "z": 22,"A": 2, "B": 4, "C": 7, "D": 5, "E": 9, "F": 6, "G": 8, "H": 10, "I": 24, "J": 1, "K": 25, "L": 15, "M": 14, "N": 12, "O": 13, "P": 3, "Q": 11, "R": 16, "S": 17, "T": 23, "U": 26, "V": 21, "W": 19, "X": 18, "Y": 20, "Z": 22}
    message = [encoderring[char] for char in "BeSureToDrinkYourOvaltine"]
    message_with_linebreaks = ' 4  9 17 26 16  9 23 \n13  5 16 24 12 25 20 \n13 26 16 13 21  2 15 \n23 24 12  9'
    lcd_text_4line('\n   Transmitting\n     message!')
    for n in message:
        red_led.number(n)
        sleep(1)
    lcd_text_4line('\n   Transmission\n     complete')
    red_led.show('    ')
    sleep(5)
    lcd_text_4line(message_with_linebreaks)
    while not red_button.is_pressed:
        sleep(1)


if __name__ == "__main__":
    from systemtest import displays,switches,buttons,a_combo,b_combo
    main(displays,switches,buttons,a_combo,b_combo)
    


