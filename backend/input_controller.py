import pydirectinput
import time

class InputController:
    def __init__(self):
        pydirectinput.PAUSE = 0.1
        pydirectinput.FAILSAFE = True

    def press_key(self, key):
        pydirectinput.press(key.lower())

    def click(self, button):
        if button == "LClick":
            pydirectinput.click(button='left')
        elif button == "RClick":
            pydirectinput.click(button='right')

    def move_mouse(self, dx, dy):
        pydirectinput.moveRel(dx, dy, relative=True)

    def move_to(self, x, y):
        pydirectinput.moveTo(x, y)