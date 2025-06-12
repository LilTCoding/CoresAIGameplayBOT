from input_controller import InputController
import time
import random

class GameProfile:
    def execute_action(self, action):
        pass

    def execute_command(self, params):
        pass

class EscapeFromTarkov(GameProfile):
    def __init__(self):
        self.controller = InputController()
        self.actions = ["W", "A", "S", "D", "Shift", "Space", "LClick", "RClick", "Inventory", "Special"]

    def execute_action(self, action):
        action_str = self.actions[action]
        if action_str in ["LClick", "RClick"]:
            self.controller.click(action_str)
        else:
            self.controller.press_key(action_str)
        if action_str == "RClick":
            self.controller.move_mouse(random.randint(-10, 10), 0)

    def execute_command(self, params):
        if params.get("task") == "manage_inventory":
            self.controller.press_key("Inventory")
            time.sleep(0.5)
            for _ in range(3):
                self.controller.click("LClick")
                self.controller.move_mouse(50, 50)
                time.sleep(0.2)
            self.controller.press_key("Inventory")

class ForzaHorizon5(GameProfile):
    def __init__(self):
        self.controller = InputController()
        self.actions = ["W", "A", "S", "D", "Shift", "Space", "LClick", "RClick", "Escape", "Enter"]
        self.tune_presets = {
            "MPG_300": {"suspension": 0.8, "gearing": 0.9, "brakes": 0.7},
            "MPG_290": {"suspension": 0.75, "gearing": 0.85, "brakes": 0.65},
            "MPG_250": {"suspension": 0.7, "gearing": 0.8, "brakes": 0.6},
            "MPG_180": {"suspension": 0.65, "gearing": 0.75, "brakes": 0.55}
        }

    def execute_action(self, action):
        action_str = self.actions[action]
        if action_str in ["LClick", "RClick"]:
            self.controller.click(action_str)
        else:
            self.controller.press_key(action_str)
        if action_str == "RClick":
            self.controller.move_mouse(random.randint(-20, 20), 0)

    def execute_command(self, params):
        task = params.get("task")
        if task == "tune_car":
            preset = params.get("preset")
            if preset in self.tune_presets:
                self._tune_car(preset)
        elif task == "upgrade_car":
            self._upgrade_car()

    def _upgrade_car(self):
        self.controller.press_key("Escape")
        time.sleep(0.5)
        self.controller.press_key("S")
        self.controller.press_key("Enter")
        time.sleep(0.5)
        self.controller.press_key("S")
        self.controller.press_key("Enter")
        time.sleep(1)
        for _ in range(5):
            self.controller.press_key("D")
            self.controller.press_key("Enter")
            self.controller.click("LClick")
            time.sleep(0.3)
        self.controller.press_key("Escape")

    def _tune_car(self, preset):
        self.controller.press_key("Escape")
        time.sleep(0.5)
        self.controller.press_key("S")
        self.controller.press_key("Enter")
        time.sleep(0.5)
        self.controller.press_key("S")
        self.controller.press_key("Enter")
        time.sleep(1)
        tune = self.tune_presets[preset]
        for _ in range(3):
            self.controller.move_mouse(50, 0)
            self.controller.click("LClick")
            time.sleep(0.2)
        self.controller.press_key("Escape")

class Warzone(GameProfile):
    def __init__(self):
        self.controller = InputController()
        self.actions = ["W", "A", "S", "D", "Shift", "Space", "LClick", "RClick", "Inventory", "Special"]

    def execute_action(self, action):
        action_str = self.actions[action]
        if action_str in ["LClick", "RClick"]:
            self.controller.click(action_str)
        else:
            self.controller.press_key(action_str)
        if action_str == "RClick":
            self.controller.move_mouse(random.randint(-15, 15), random.randint(-10, 10))

    def execute_command(self, params):
        task = params.get("task")
        if task == "engage_enemies":
            self.controller.click("RClick")
            self.controller.click("LClick")
            self.controller.move_mouse(random.randint(-10, 10), 0)
        elif task == "navigate_to_waypoint":
            x, y = params.get("x"), params.get("y")
            self._navigate_to_waypoint(x, y)

    def _navigate_to_waypoint(self, x, y):
        self.controller.press_key("Inventory")
        time.sleep(0.5)
        self.controller.move_to(x, y)
        self.controller.click("LClick")
        self.controller.press_key("Inventory")
        time.sleep(0.5)
        self.controller.press_key("Space")
        time.sleep(2)
        self.controller.press_key("W")
        for _ in range(10):
            self.controller.move_mouse(random.randint(-5, 5), 0)
            time.sleep(1)
