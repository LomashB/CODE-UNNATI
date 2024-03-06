import time
from grovepi import *

ledg = 6
ledr = 7
ledb = 8

pinMode(ledg,"OUTPUT")
pinMode(ledr,"OUTPUT")
pinMode(ledb,"OUTPUT")

while True:
    digitalWrite(ledr,1)
    digitalWrite(ledb,0)
    digitalWrite(ledg,0)
    time.sleep(1)
    digitalWrite(ledr,0)
    digitalWrite(ledb,1)
    digitalWrite(ledg,0)
    time.sleep(1)
    digitalWrite(ledr,0)
    digitalWrite(ledb,0)
    digitalWrite(ledg,1)
    time.sleep(1)