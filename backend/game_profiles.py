import cv2
import numpy as np
from input_controller import InputController
import time
import random

class GameProfile:
    def execute_action(self, action):
        pass

    def calculate_reward(self, observation):
        return 0.0

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

    def calculate_reward(self, observation):
        hsv = cv2.cvtColor(observation, cv2.COLOR_RGB2HSV)
        return 1.0 if np.mean(hsv[:, :, 0]) > 50 else -1.0

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
            "MPG_180": {"suspension": 0.65, "gearing": 0.75, "brakes": 0.55},
            "Drift_Hoonicorn": {"suspension": 0.5, "gearing": 0.6, "brakes": 0.4, "drift_angle": 0.9},
            "Drift_VinDiesel": {"suspension": 0.55, "gearing": 0.65, "brakes": 0.45, "drift_angle": 0.85},
            "Drift_BrianOConnor": {"suspension": 0.6, "gearing": 0.7, "brakes": 0.5, "drift_angle": 0.8},
            "Drift_Han": {"suspension": 0.58, "gearing": 0.68, "brakes": 0.48, "drift_angle": 0.87},
            "Drift_DK": {"suspension": 0.52, "gearing": 0.62, "brakes": 0.42, "drift_angle": 0.88},
            "Speed_BrianOConnor": {"suspension": 0.9, "gearing": 0.95, "brakes": 0.8, "top_speed": 0.9},
            "Speed_1": {"suspension": 0.88, "gearing": 0.93, "brakes": 0.78, "top_speed": 0.91},
            "Speed_2": {"suspension": 0.87, "gearing": 0.92, "brakes": 0.77, "top_speed": 0.92},
            "Speed_3": {"suspension": 0.86, "gearing": 0.91, "brakes": 0.76, "top_speed": 0.93},
            "Speed_4": {"suspension": 0.85, "gearing": 0.9, "brakes": 0.75, "top_speed": 0.94},
            "Speed_5": {"suspension": 0.84, "gearing": 0.89, "brakes": 0.74, "top_speed": 0.95},
            "Speed_6": {"suspension": 0.83, "gearing": 0.88, "brakes": 0.73, "top_speed": 0.96},
            "Speed_7": {"suspension": 0.82, "gearing": 0.87, "brakes": 0.72, "top_speed": 0.97},
            "Speed_8": {"suspension": 0.81, "gearing": 0.86, "brakes": 0.71, "top_speed": 0.98},
            "Speed_9": {"suspension": 0.8, "gearing": 0.85, "brakes": 0.7, "top_speed": 0.99},
            "Speed_10": {"suspension": 0.79, "gearing": 0.84, "brakes": 0.69, "top_speed": 1.0}
        }

    def execute_action(self, action):
        action_str = self.actions[action]
        if action_str in ["LClick", "RClick"]:
            self.controller.click(action_str)
        else:
            self.controller.press_key(action_str)
        if action_str == "RClick":
            self.controller.move_mouse(random.randint(-20, 20), 0)

    def calculate_reward(self, observation):
        gray = cv2.cvtColor(observation, cv2.COLOR_RGB2GRAY)
        return 1.0 if np.mean(gray) > 100 else -1.0

    def execute_command(self, params):
        task = params.get("task")
        if task == "Goliath":
            laps = params.get("laps", 50)
            print(f"Starting Goliath race, {laps} laps")
            self.controller.press_key("W")
            time.sleep(0.5)
            self.controller.press_key("Space")
            for _ in range(laps):
                self.controller.press_key("W")
                self.controller.move_mouse(random.randint(-20, 20), 0)
                time.sleep(60)
        elif task == "earn_millions":
            for _ in range(10):
                self.controller.press_key("W")
                self.controller.press_key("Space")
                time.sleep(120)
                self.controller.click("LClick")
        elif task == "upgrade_car":
            self._upgrade_car()
        elif task == "tune_car":
            preset = params.get("preset")
            if preset in self.tune_presets:
                self._tune_car(preset)

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

class Fortnite(GameProfile):
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

    def calculate_reward(self, observation):
        hsv = cv2.cvtColor(observation, cv2.COLOR_RGB2HSV)
        return 2.0 if np.mean(hsv[:, :, 2]) > 150 else -1.0

    def execute_command(self, params):
        if params.get("task") == "build_and_fight":
            self.controller.click("RClick")
            self.controller.press_key("Special")
            for _ in range(3):
                self.controller.click("LClick")
                self.controller.move_mouse(0, -50)
                self.controller.click("LClick")

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

    def calculate_reward(self, observation):
        hsv = cv2.cvtColor(observation, cv2.COLOR_RGB2HSV)
        return 2.0 if np.mean(hsv[:, :, 2]) > 150 else -1.0

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

class ArmaReforger(GameProfile):
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

    def calculate_reward(self, observation):
        return 1.0 if np.mean(observation) > 100 else -1.0

    def execute_command(self, params):
        if params.get("task") == "tactical_move":
            self.controller.press_key("W")
            self.controller.press_key("Shift")
            time.sleep(2)

class DCS(GameProfile):
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

    def calculate_reward(self, observation):
        return 1.0 if np.mean(observation) > 100 else -1.0

    def execute_command(self, params):
        if params.get("task") == "start_engine":
            self.controller.press_key("Space")
            time.sleep(1)
            self.controller.press_key("Special")
            time.sleep(0.5)
            self.controller.click("LClick")
