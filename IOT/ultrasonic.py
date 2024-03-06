from grovepi import *
from grove_rgb_lcd import *
import time

ultrasonic_ranger = 7

while True :
    distant = ultrasonicRead(ultrasonic_ranger)
    print(distant,'cm')
    setText_norefresh('     '+str(distant)+'cm')
    time.sleep(0.025)