#!/bin/python
# RaspiDigiClock using TM1637 modules
# Designed to run up to 4 modules
#
# Requires Python2.7
#
# Use the raspidigiclock.ini file to set number of 
# modules, Timezone, 12/24 hr clock
#
# When running, you should see the colon blinking once per second
#
import tm1637
import os
import time

#disp = []
#for x in range(0,NUM_MODS):
#    disp.append(FourDigit(dio=d[x],clk=c[x],lum=l))

red_led = tm1637.TM1637(clk=17,dio=4)
red_led.brightness(val=1) #0 through 7 
showColon = True

# DISPLAY TIME ON ONE MODULE
def displayTM(disp,tim,hrs,colondsp):
    hour = tim.tm_hour
    minute = tim.tm_min
    if hrs == '12':
        hour = (tim.tm_hour % 12) or 12
    disp.show("%02d%02d" %(hour, minute),colon=colondsp)
    #disp.setColon(colon)


# MAIN LOOP
while True:
    cur=time.time()
    #os.environ["TZ"]=tmz[x]
    #time.tzset()
    ct = time.localtime(cur)
    displayTM(red_led,ct,'12',showColon)
    time.sleep(0.5)
    showColon = not showColon
