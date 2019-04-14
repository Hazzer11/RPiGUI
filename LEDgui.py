from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

red= LED(12)
green = LED(20)
blue= LED(16)

window = Tk()
window.title("RGB LEDS")
myFont= tkinter.font.Font(family = 'Helvetica', size = 12)
#the first 
def toggleRed():
    if red.is_lit:
        red.off()
        redLEDbutton["text"]="Red off"
    else:
        red.on()
        redLEDbutton["text"]="Red's on"

redLEDbutton = Button(window, text = "Red on",bg='Red', font = myFont,height=2, width =6, command = toggleRed)
redLEDbutton.grid(row=0 , column = 0)

## the second
def toggleGreen():
    if green.is_lit:
        green.off()
        greenLEDbutton["text"]="Green's off"
    else:
        green.on()
        greenLEDbutton["text"]="Green's on"

greenLEDbutton = Button(window, text = "Green's on",bg='Green', font = myFont,height=2, width =6, command = toggleGreen)
greenLEDbutton.grid(row=0 , column = 1)

## the third
def toggleBlue():
    if blue.is_lit:
        blue.off()
        blueLEDbutton["text"]="Blue's off"
    else:
       blue.on()
       blueLEDbutton["text"]="Blue's on"

blueLEDbutton = Button(window, text = "Blue's on",bg='Blue', font = myFont,height=2, width =6, command = toggleBlue)
blueLEDbutton.grid(row=0 , column= 2)

##final button

def quitLEDS():
    RPi.GPIO.cleanup()
    window.destroy()

exitbutton = Button(window, text = "QUIT",bg='White', font = myFont,height=2, width =6, command = quitLEDS)
exitbutton.grid(row=0 , column = 3)

window.protocol("Delete Window", quitLEDS)
