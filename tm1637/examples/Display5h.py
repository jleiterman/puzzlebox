# Display5h.py
# scroll

from TM1637 import FourDigit
from time import sleep
        
d = FourDigit()
while True:
    d.scroll("ALL your bAse Are Belong to us")   
