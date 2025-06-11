import pydirectinput
import time
import random

class InputController:
    def init(self):
        pydirectinput.FAILSAFE = False
        self.key_map = {
            "W": "w", "A": "a", "S": "s", "D": "d",
            "Shift": "shift", "Space": "space",
            "LClick": "left", "RClick": "right",
            "Inventory": "tab", "Special": "e",
            "Escape": "esc", "Enter": "enter"
        }

    def press_key(self, key):
        duration = random.uniform(0.05, 0.15)
        pydirectinput.keyDown(self.key_map[key])
        time.sleep(duration)
        pydirectinput.keyUp(self.key_map[key])

    def click(self, button):
        if button == "LClick":
            pydirectinput.click()
        elif button == "RClick":
            pydirectinput.rightClick()

    def move_mouse(self, dx, dy):
        pydirectinput.moveRel(dx, dy, relative=True)

    def move_to(self, x, y):
        pydirectinput.moveTo(x, y)