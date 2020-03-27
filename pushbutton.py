import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_pressed(channel):
    print("Button was pushed!")
def button_released(channel):
    print("Button was released!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(36,GPIO.RISING,callback=button_pressed, bouncetime=100) # Setup event on pin 10 rising edge
#GPIO.add_event_detect(36,GPIO.FALLING,callback=button_released, bouncetime=100)
#gpio can only detect rizing or falling events, not both
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
