import time
from grovepi import *

ledg = 6
ledr = 7
ledb = 8

pinMode(ledg,"OUTPUT")
pinMode(ledr,"OUTPUT")
pinMode(ledb,"OUTPUT")

digitalWrite(ledr,0)
digitalWrite(ledb,0)
digitalWrite(ledg,0)

clr = input("Enter color name : ")

digitalWrite(ledr,0)
digitalWrite(ledb,0)
digitalWrite(ledg,0)

if clr == "r" :
    digitalWrite(ledr,1)
    time.sleep(1)
    digitalWrite(ledr,0)
elif clr == "g" :
    digitalWrite(ledg,1)
    time.sleep(1)
    digitalWrite(ledg,0)
else :
    digitalWrite(ledb,1)
    time.sleep(1)
    digitalWrite(ledb,0)