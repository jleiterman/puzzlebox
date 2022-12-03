import threading
from luma.core.render import canvas
from importlib import reload
from time import sleep
import random

class plant_component:
    def __init__(self, name):
        self.name = name
        self.attributes = ['None']
        
    def add_attribute(self, new_attribute):
        self.attributes.append(new_attribute)
    
    def attribute_count(self):
        return len(self.attributes)

class component_select_list_attribute:
    def __init__(self, name, values):
        self.attribute_type = 'selectable list'
        self.name = name
        self.values = values
        self.selected_value = 0
    def value(self):
        return self.values[self.selected_value]
    def update_value(self):
        if self.selected_value == len(self.values) - 1:
            self.selected_value = 0
        else:
            self.selected_value = self.selected_value + 1
        #self.selected_value = puzzle_functions.rotate_lcd_multiselect(lcd_screen_2,[b_right,b_left,blue_button],self.values,self.values,'pickone')

class component_numeric_attribute:
    def __init__(self, name, value_mean, units, sd = "5pct" ):
        self.attribute_type = 'view only numeric'
        self.name = name
        self.value_mean = value_mean
        self.units = units
        if sd == "5pct":
            self.sd = value*.05
        else:
            self.sd = sd
    def value(self):
        return str(random.gauss(self.value_mean,self.sd))
        


def lcd_text(text):
    with canvas(lcd_screen_2) as draw:
        draw.rectangle(lcd_screen_2.bounding_box, outline="white", fill="black")
        draw.text((10, 10), text, fill="white")

def lcd_max_text(text):
    with canvas(lcd_screen_2) as draw:
        draw.text((0, 0), text, fill="white")

def update_component_attribute_display():
    global component
    global attribute
    global componentlist
    global components
    global wh
    global black_button
    if black_button.is_pressed == False:
        red_led_2.show(str(component).zfill(3)+str(attribute))
    if component == 0:
        lcd_screen_2.display(wh) 
    else:
        if attribute == 0:
            with canvas(lcd_screen_2) as draw:
                draw.rectangle(lcd_screen_2.bounding_box, outline="black", fill="black")
                draw.rectangle((0,0,127,11),outline="white",fill="white")
                draw.text((1,0), componentlist[component], fill="black")
                draw.rectangle((17,14,111,57), outline="white", fill="black")
                draw.text((19,14), " use attribute ", fill="white")
                draw.text((19,22), "  selector to  ", fill="white")
                draw.text((19,30), "  select from  ", fill="white")
                draw.text((19,38), "   available   ", fill="white")
                draw.text((19,46), "   attributes  ", fill="white")
        else:
            if components[component] == None: 
                with canvas(lcd_screen_2) as draw:
                    draw.rectangle(lcd_screen_2.bounding_box, outline="black", fill="black")
                    draw.rectangle((0,0,127,11),outline="white",fill="white")
                    draw.text((1,0), componentlist[component], fill="black")
                    draw.rectangle((17,14,111,57), outline="white", fill="white")
                    draw.text((19,22), "      NO       ", fill="black")
                    draw.text((19,30), "  attributes   ", fill="black")
                    draw.text((19,38), "  available!   ", fill="black")     
            else:
                with canvas(lcd_screen_2) as draw:
                    draw.rectangle(lcd_screen_2.bounding_box, outline="black", fill="black")
                    draw.rectangle((0,0,127,11),outline="white",fill="white")
                    draw.text((1,0), componentlist[component], fill="black")
                    draw.text((1,22), components[component].attributes[attribute].name, fill="white")
                    draw.text((1,32), components[component].attributes[attribute].value(), fill="white")
                    if components[component].attributes[attribute].attribute_type == 'view only numeric':
                        draw.text((1,42), components[component].attributes[attribute].units, fill="white")


def update_component(lcd_screen_2):
    global component
    global attribute
    attribute = 0
    if a_left.value == 0:
        if component == 122:
            component = 0
        else:
            component = component + 1
    elif a_left.value == 1:
        if component == 0:
            component = 122
        else:
            component = component - 1
    else:
        print("we should not see this")
    update_component_attribute_display()


def update_component_wrapper():
    update_component(lcd_screen_2)




def update_attribute_selection(lcd_screen_2):
    global attribute
    global component
    if component == 0:
        attribute = 0
    elif components[component] == None:
        if b_left.value == 0:
            if attribute == 1:
                attribute = 0
            else:
                attribute = attribute + 1
        elif b_left.value == 1:
            if attribute == 0:
                attribute = 1
            else:
                attribute = attribute - 1
        else:
            print("we should not see this")
    else:
        if b_left.value == 0:
            if attribute == len(components[component].attributes)-1:
                attribute = 0
            else:
                attribute = attribute + 1
        elif b_left.value == 1:
            if attribute == 0:
                attribute = len(components[component].attributes)-1
            else:
                attribute = attribute - 1
        else:
            print("we should not see this")        
    update_component_attribute_display()


def update_attribute_selection_wrapper():
    update_attribute_selection(lcd_screen_2)

    
def update_attribute_value():
    if components[component].attributes[attribute].attribute_type == 'selectable list':
        components[component].attributes[attribute].update_value()
        update_component_attribute_display()
    else:
        lcd_text("That attribute\ncannot be updated\nby this interface")
        sleep(3)
        update_component_attribute_display()





def countdown():
    global time_to_meltdown
    global puzzle_solved
    while True:
        sleep(1)
        if not(puzzle_solved):
            time_to_meltdown = time_to_meltdown - 1



def display_countdown():
    global black_button
    global red_led_2
    global time_to_meltdown
    mins, secs = divmod(time_to_meltdown, 60)
    red_led_2.numbers(mins, secs, True)
    while black_button.is_pressed:
        mins, secs = divmod(time_to_meltdown, 60)
        red_led_2.numbers(mins, secs, True)
        sleep(1)



def sleepmode():
    global component
    global attribute
    lcd_screen_2.hide()
    red_led_2.write([0, 0, 0, 0])
    while not switch_1.is_pressed:
        red_led_2.write([0, 0, 0, 0])
    lcd_screen_2.show()
    component = 0
    attribute = 0
    update_component_attribute_display()



def lcd_screen_2_bright():
    global lcd_screen_2
    lcd_screen_2.contrast(255)

def lcd_screen_2_dim():
    global lcd_screen_2
    lcd_screen_2.contrast(64)

def red_led_2_bright():
    global red_led_2
    red_led_2.brightness(val=7)

def red_led_2_dim():
    global red_led_2
    red_led_2.brightness(val=1)



   
def main(red_led,lcd_screen,switches,buttons,a_combo,b_combo):
    from luma.core.render import canvas
    from time import time, sleep, localtime

    global componentlist
    with open('/home/pi/puzzlebox/componentlist21.txt') as my_file:
        componentlist = my_file.readlines()
    global lcd_screen_2
    lcd_screen_2 = lcd_screen
    lcd_screen_2.clear()
    global red_led_2
    red_led_2 = red_led
    componentlist.insert(0, 'componentlist')
    global components
    components = [None] * 123
    global component
    component = 0
    global attribute
    attribute = 0
    global puzzle_solved
    puzzle_solved = False
    global time_to_meltdown
    time_to_meltdown = 3600

    from PIL import Image
    global wh
    wh = Image.open('/home/pi/puzzlebox/64x128westinghouse.png').convert(lcd_screen_2.mode)

    global switch_1
    global switch_2
    global switch_3
    global a_left
    global a_right
    global b_left
    global b_right
    switch_1 = switches[0]
    switch_2 = switches[1]
    switch_3 = switches[2]
    switch_4 = switches[3]
    switch_5 = switches[4]
    switch_6 = switches[5]
    switch_7 = switches[6]
    switch_8 = switches[7]
    switch_9 = switches[8]
    global black_button
    global white_button
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
    
    components[1]  = plant_component('turbinebuilding')
    components[1].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[1].add_attribute(component_select_list_attribute("doors",["locked","unlocked"]))
    components[1].add_attribute(component_numeric_attribute("temperature",72,"degF",.05))
    components[2]  = plant_component("Turbine bridge crane")
    components[2].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[2].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[2].add_attribute(component_numeric_attribute("bridge position",82,"feet",0))
    components[2].add_attribute(component_numeric_attribute("trolly position",23,"feet",0))
    components[2].add_attribute(component_numeric_attribute("block hook position",28,"feet",0))
    components[3]  = plant_component("High-pressure turbine")
    components[3].add_attribute(component_numeric_attribute("Inlet steam temp",900,"degf",6))
    components[3].add_attribute(component_numeric_attribute("Inlet steam pressure",1450,"psi",6))
    components[4]  = plant_component("Low-pressure turbines")
    components[4].add_attribute(component_numeric_attribute("Inlet steam temp",720,"degf",5))
    components[4].add_attribute(component_numeric_attribute("Inlet steam pressure",1220,"psi",6))
    components[5]  = plant_component("Generator")
    components[5].add_attribute(component_numeric_attribute("Output Power",380,"megawatts",3))    
    components[5].add_attribute(component_numeric_attribute("bearing vibration",7.4,"percent of max allowable",.02)) 
    components[6]  = plant_component("Condenser")   
    components[6].add_attribute(component_select_list_attribute("operation state",["on","off"])) 
    components[7]  = plant_component("Low pressure heaters") 
    components[7].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[8]  = plant_component("De-aerator heater")
    components[8].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[9]  = plant_component("Storage tank")
    components[9].add_attribute(component_numeric_attribute("percent filled",2.2,"percent of max allowable",.02)) 
    components[10] = plant_component("Surge tank")
    components[10].add_attribute(component_numeric_attribute("percent filled",18,"percent of max allowable",6)) 
    components[11] = plant_component("High-p fdwater heater")
    components[11].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[11].add_attribute(component_select_list_attribute("setpoint temperature",["400degF","425degF","450degF"]))
    components[12] = plant_component("Low-p fdwater heaters")
    components[12].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[12].add_attribute(component_select_list_attribute("setpoint temperature",["400degF","425degF","450degF"]))
    components[13] = plant_component("Condensate pumps")
    components[13].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[14] = plant_component("Steam gen feed pumps")
    components[14].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[15] = plant_component("Vacuum pumps")
    components[15].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[16] = plant_component("HVAC equipment")
    components[16].add_attribute(component_select_list_attribute("operation state",["on","off"]))
    components[25]  = plant_component('Warehouse & shop bldg')
    components[25].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[25].add_attribute(component_select_list_attribute("doors",["locked","unlocked"]))
    components[25].add_attribute(component_numeric_attribute("temperature",72,"degF",.05))
    components[26]  = plant_component('Steam generator bldg')
    components[26].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[26].add_attribute(component_select_list_attribute("doors",["locked","unlocked"]))
    components[26].add_attribute(component_numeric_attribute("temperature",72,"degF",.05))
    components[26].add_attribute(component_numeric_attribute("relative humidity",90,"percent",.05))
    components[27]  = plant_component("Steamgen gantry crane")
    components[27].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[27].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[27].add_attribute(component_numeric_attribute("bridge position",82,"feet",0))
    components[27].add_attribute(component_numeric_attribute("trolly position",23,"feet",0))
    components[27].add_attribute(component_numeric_attribute("block hook position",28,"feet",0))
    components[37] = plant_component("Intermediate pump")
    components[37].add_attribute(component_numeric_attribute("speed",1006,"rpm",10))
    components[37].add_attribute(component_numeric_attribute("head pressure",612,"feet",4))
    components[45] = plant_component("ColdReturn heatexhngr")
    components[45].add_attribute(component_numeric_attribute("Sodium Temp",208,"degF",.2))
    components[45].add_attribute(component_select_list_attribute("lowtemp heater",["off","on"]))
    components[46] = plant_component("Feed from heat exhngr")
    components[46].add_attribute(component_numeric_attribute("Sodium Temp",230,"degF",.2))
    components[46].add_attribute(component_select_list_attribute("lowtemp heater",["on","off"]))
    components[47] = plant_component("Flow meter")
    components[47].add_attribute(component_numeric_attribute("Sodium flow",20,"lb/hr",5))
    components[48]  = plant_component('Diesel Generator Bldg')
    components[48].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[48].add_attribute(component_select_list_attribute("doors",["locked","unlocked"]))
    components[48].add_attribute(component_numeric_attribute("temperature",72,"degF",.05))    
    components[48]  = plant_component('Control room')
    components[48].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[48].add_attribute(component_select_list_attribute("doors",["unlocked","locked"]))
    components[48].add_attribute(component_numeric_attribute("temperature",72,"degF",.05))    
    components[57] = plant_component("Reactor polar crane")
    components[57].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[57].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[57].add_attribute(component_numeric_attribute("bridge position",10,"degreesr",0))
    components[57].add_attribute(component_numeric_attribute("trolly position",23,"feet",0))
    components[57].add_attribute(component_numeric_attribute("block hook position",28,"feet",0))
    components[83] = plant_component("Interm heat exchanger")
    components[83].add_attribute(component_numeric_attribute("SodiumTemp prime IN",1150,"degF",10))
    components[83].add_attribute(component_numeric_attribute("SodiumTemp prime OUT",1100,"degF",10))
    components[83].add_attribute(component_numeric_attribute("SodiumTemp second IN",260,"degF",10))
    components[83].add_attribute(component_numeric_attribute("SodiumTemp second OUT",260,"degF",10))
    components[95]  = plant_component('Reactor service bldng')
    components[95].add_attribute(component_select_list_attribute("lights",["on","off"]))
    components[95].add_attribute(component_select_list_attribute("doors",["locked","unlocked"]))
    components[95].add_attribute(component_numeric_attribute("temperature",72,"degF",.05)) 
    components[96] = plant_component("Reactor service crane")
    components[96].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[96].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[96].add_attribute(component_numeric_attribute("bridge position",10,"feet",0))
    components[96].add_attribute(component_numeric_attribute("trolly position",22,"feet",0))
    components[96].add_attribute(component_numeric_attribute("block hook position",16,"feet",0))
    components[108] = plant_component("New component crane")
    components[108].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[108].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[108].add_attribute(component_numeric_attribute("bridge position",7,"feet",0))
    components[108].add_attribute(component_numeric_attribute("trolly position",8,"feet",0))
    components[108].add_attribute(component_numeric_attribute("block hook position",8,"feet",0))
    components[118]  = plant_component('Decontamination area')
    components[118].add_attribute(component_select_list_attribute("status",["contaminated","decontaminated"]))
    components[119] = plant_component("Decon area crane")
    components[119].add_attribute(component_select_list_attribute("Motion Warning Lights",["off","on"]))
    components[119].add_attribute(component_select_list_attribute("Motion Warning Siren",["off","on"]))
    components[119].add_attribute(component_numeric_attribute("bridge position",66,"feet",0))
    components[119].add_attribute(component_numeric_attribute("trolly position",18,"feet",0))
    components[119].add_attribute(component_numeric_attribute("block hook position",12,"feet",0))
    components[122]  = plant_component('Plant service bldng')
    components[122].add_attribute(component_select_list_attribute("lights",["off","on"]))
    components[122].add_attribute(component_select_list_attribute("overhead door",["open","closed"]))
    components[122].add_attribute(component_numeric_attribute("temperature",92,"degF",.05))    
    
    a_right.when_pressed = update_component_wrapper
    white_button.when_pressed = update_attribute_value
    b_right.when_pressed = update_attribute_selection_wrapper
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()
    black_button.when_pressed = display_countdown
    black_button.when_released = update_component_attribute_display
    switch_1.when_released = sleepmode
    switch_2.when_pressed = lcd_screen_2_bright
    switch_2.when_released = lcd_screen_2_dim
    switch_3.when_pressed = red_led_2_bright
    switch_3.when_released = red_led_2_dim

    lcd_screen_2_dim()
    red_led_2_dim()
    switch_1.wait_for_press()
    # display splash screen
    lcd_screen_2.display(wh)
    red_led_2.scroll('ON      ON     ON')


    while not(puzzle_solved):
        if  components[45].attributes[2].value() == 'on':
            puzzle_solved = True
            print("puzzle_solved")
            print(puzzle_solved)
            display_countdown()
        else:
            sleep(2)
            update_component_attribute_display()
            print("puzzle_solved")
            print(puzzle_solved)
    
    
    # cleaning up button functions
    def donothing():
        do = "nothing"
    
    for a in a_combo:
        a.when_pressed = donothing
    
    for b in b_combo:
        b.when_pressed = donothing
    
    for button in buttons:
        button.when_pressed = donothing
    
    for switch in switches:
        switch.when_pressed = donothing
        switch.when_released = donothing
    
    lcd_text('\nYou WIN')
    
 
    sleep(10)



if __name__ == "__main__":
    from systemtest import red_led,lcd_screen,switches,buttons,a_combo,b_combo
    main(red_led,lcd_screen,switches,buttons,a_combo,b_combo)
