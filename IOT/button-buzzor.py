import time
from grovepi import *
import math
from grove_rgb_lcd import *
setRGB(0,255,255) # (Green) RGB Pattern
buzzer_pin = 2		#Port for buzzer
button = 4
#Port for Button

pinMode(buzzer_pin,"OUTPUT")	# Assign mode for buzzer as output
pinMode(button,"INPUT")		# Assign mode for Button as input
while True:
	try:
		button_status= digitalRead(button)	#Read the Button status
		#print(button_status)
		if button_status:	#If the Button is in HIGH position, run the program
			digitalWrite(buzzer_pin,1)
			setText("AWAJ BAND KAR")
			time.sleep(0.5)
			digitalWrite(buzzer_pin,0)
                        
			# print "\tBuzzing"			
		else:		#If Button is in Off position, print "Off" on the screen
			setText("GATE CLOSED")
			time.sleep(0.5)
			# print "Off"			
	except KeyboardInterrupt:	# Stop the buzzer before stopping
		digitalWrite(buzzer_pin,0)
		break
	except (IOError,TypeError) as e:
		print("Error")


# Problem reported . Check button value



