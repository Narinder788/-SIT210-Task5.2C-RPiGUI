from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

win = Tk()
win.title("TASK 5.2C-LED-TOGGLE");
fontstyle = tkinter.font.Font(family = "Arial", size = 20, weight = "bold")

RedLight = LED(16)
YellowLight = LED(11)
GreenLight = LED(10)
value = IntVar()

def led_function():
    Temp = value.get()
    if Temp == 1:
       RedLight.on()
       YellowLight.off()
       GreenLight.off()
        
    elif Temp == 2:
        RedLight.off()
        YellowLight.on()
        GreenLight.off()

    elif Temp == 3:
        RedLight.off()
        YellowLight.off()
        GreenLight.on()
    else:
        RedLight.off()
        YellowLight.off()
        GreenLight.off()

    
red_button = Radiobutton( win, text = "RED-LED", font = fontstyle, variable = value, value = 1, command = led_function, height = 8, width = 8)
red_button.grid( row = 1, column = 1)

green_button = Radiobutton( win, text = "GREEN-LED", font = fontstyle, variable = value, value = 2, command = led_function, height = 10, width = 10)
green_button.grid( row = 2, column = 2)

yellow_button = Radiobutton( win, text = "YELLOW-LED", font = fontstyle, variable = value, value= 3, command = led_function, height = 10, width = 10)
yellow_button.grid( row = 3, column = 3)

win.mainloop()