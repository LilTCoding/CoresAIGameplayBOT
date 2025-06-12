import time
import random

class AIEngine:
    def __init__(self, profile):
        self.profile = profile
        self.running = False

    def start_autonomous(self):
        self.running = True
        while self.running:
            action = random.randint(0, len(self.profile.actions) - 1)
            self.profile.execute_action(action)
            time.sleep(0.05)

    def stop_autonomous(self):
        self.running = False

    def execute_command(self, params):
        self.profile.execute_command(params)