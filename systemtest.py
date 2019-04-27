#!/usr/bin/python

# test file to run system test.

# first test is to ensure that needed libraries load

# test switches

# test displayes

# test buttons

# test other

import sys
import Adafruit_DHT
import time
import os

os.environ['TZ'] = 'US/Central'
time.tzset()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    f = open("/home/pi/templog.txt","a+")
    f.write(time.strftime('%Y-%m-%d %H:%M:%S')+'     {:.1f} F'.format(temperature*9/5+32)+'\n')
    f.close()
    time.sleep(10)
