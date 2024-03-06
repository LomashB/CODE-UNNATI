from grovepi import *
from grove_rgb_lcd import *
import time


buzzer_pin = 2

dht_sensor_port = 6
dht_sensor_type = 0
setRGB(0,255,0)
while True:
    [t,h] = dht(dht_sensor_port,dht_sensor_type)
    time.sleep(0.5)
    print(f"Temp:{t} C Humidity:{h}%")
    setText_norefresh(f"Temp:{t} C \nHumidity:{h}%")
    time.sleep(2)
    if t < 24.0:
        digitalWrite(buzzer_pin,1)
        time.sleep(0.5)
        digitalWrite(buzzer_pin,0)
    else:
        digitalWrite(buzzer_pin,0)