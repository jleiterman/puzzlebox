from gpiozero import Button
from signal import pause

def yellow_button_pressed():
    print("Yellow button was pressed.")

yellow_button = Button(19)

yellow_button.when_pressed = yellow_button_pressed

pause()
