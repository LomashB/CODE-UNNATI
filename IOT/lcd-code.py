from grove_rgb_lcd import *

setRGB(204,194,255)
#setText("Hello, \nLomash Bhuva..")
total = input("Enter the upper bound : ")

for i in range(total) :
    setText(i)
else :
    setText("Count over")
