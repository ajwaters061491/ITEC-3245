#values
from sense_emu import SenseHat
import time

sense = SenseHat()
temperature = str(sense.get_temperature() * 9/5 + 32) + " degrees Fahrenheit"
humidity = str(sense.get_humidity()) + " %"
pressure = str(sense.get_pressure()) + " Millibars"
accelerometer = str(sense.get_accelerometer_raw()) + " Gs"

 
print("It is currently " + temperature +
      ", the humidity is currently at " + humidity + 
      ", the pressure is reading " + pressure +
      ", and the accelerometer shows " + accelerometer)


#scroll
from sense_emu import SenseHat
import time

sense = SenseHat()

green = (0,255,0)
white = (255,255,255)

text_string = "Hello World!"

while True: 
    sense.show_message(text_string, scroll_speed=0.1, text_colour=[255,255,255], back_colour=[0,0,0])

    time.sleep(3) #just to cut down on output amounts


#the letter A
from sense_emu import SenseHat
import time

sense = SenseHat()
g = (0,255,0) #green
w = (255,255,255) #white
b = (0,0,0) #blank

LetterA = [
    b, b, b, w, w, b, b, b,
    b, b, w, g, g, w, b, b,
    b, b, w, g, g, w, b, b,
    b, w, g, g, g, g, w, b,
    b, w, g, w, w, g, w, b,
    w, g, g, g, g, g, g, w,
    w, g, g, w, w, g, g, w,
    w, g, g, w, w, g, g, w, 
    ]
sense.set_pixels(LetterA)






 
