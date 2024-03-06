import time
from grovepi import *
from grove_rgb_lcd import *

setRGB(255,255,255)

def float_text(text, speed=0.5):
    while True:
        text_length = len(text)

        if text_length < 16:
            text += ' ' * (16 - text_length)

        for i in range(text_length):
            lcd_text = text[i:16+i]
            setText_norefresh(lcd_text)
            time.sleep(speed)

float_text("In LSD L stands for Lomash, S for Sneh and D for Dev.", speed=0.1)
