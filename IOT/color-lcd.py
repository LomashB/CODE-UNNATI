from grove_rgb_lcd import *

import time

import random

while True:

  p1=random.randint(0,255)

  p2=random.randint(0,255)

  p3=random.randint(0,255)

  time.sleep(0.1)

  setRGB(p1,p2,p3) # (Green) RGB Pattern

#   ip=input()

  setText("Hi,\nHello World.")



