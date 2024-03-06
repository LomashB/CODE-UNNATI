
from grovepi import *
from grove_rgb_lcd import *
import time
import smtplib
import ssl

ctx = ssl.create_default_context()
password = "edwxysadmtdjfodd"    # Your app password goes here
sender = "devdhorajiya@gmail.com"    # Your e-mail address
receiver = "lomashbhuva@gmail.com" # Recipient's address
dht_sensor_port = 6
dht_sensor_type = 0 # 0 for DHT11 and 1 for DHT22

setRGB(0,255,0)

while True:
    [ t,h ] = dht(dht_sensor_port,dht_sensor_type)
    print(f"Temp:{t} C Humidity:{h}%")
    setText_norefresh(f"Temp:{t} C\nHumidity:{h}%")
    a=["Current DHT profile of this room","Temperature "+str(t)+" C","Humidity "+str(h)+"%"]
    message = " ".join(a)
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        time.sleep(1)


