#!/usr/bin/python

# test file to run system test.

import sys
import Adafruit_DHT
import time
import os
sys.path.append('./tm1637/lib')
from TM1637 import FourDigit

# first test is to ensure that needed libraries load

# test switches

# test displayes

d = FourDigit()
d.scroll("ALL your bAse Are Belong to us")   

# test buttons

# test other


#os.environ['TZ'] = 'US/Central'
#time.tzset()
        
#while True:
#    humidity, temperature = Adafruit_DHT.read_retry(11,4)
#    f = open("/home/pi/templog.txt","a+")
#    f.write(time.strftime('%Y-%m-%d %H:%M:%S')+'     {:.1f} F'.format(temperature*9/5+32)+'\n')
#    f.close()
#    time.sleep(10)
