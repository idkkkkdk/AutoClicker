
from pyautogui import click
import keyboard
from time import sleep

print("AutoClicker")
print("Click 'H' to turn on and 'G' to turn off")

while True:
    on = False
    if keyboard.is_pressed("H") and on == False:
        on = True
        while on == True:
            click(None,None,1,0.01)
            if keyboard.is_pressed("G") and on == True:
                print("Succesfully stopped!")
                on=False