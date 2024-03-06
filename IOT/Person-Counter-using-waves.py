from grovepi import *
import grovepi
from grove_rgb_lcd import *
import time

buzzer_pin = 2
ultrasonic_ranger = 7
lightr = 8
body_count = 0

while True :
    distant = ultrasonicRead(ultrasonic_ranger)
    
    print(distant,'cm')
    if int(distant) < 13:
       body_count = body_count + 1
       grovepi.digitalWrite(buzzer_pin,1)
       digitalWrite(lightr,1)
       time.sleep(0.5)
       grovepi.digitalWrite(buzzer_pin,0)
       digitalWrite(lightr,0)
    time.sleep(0.5)
    
    print(body_count)
    setText_norefresh('    '+str(body_count)+' person')