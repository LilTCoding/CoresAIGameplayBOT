import cv2
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym
from gymnasium import spaces
import pyautogui
import time

class GameEnv(gym.Env):
    def __init__(self, profile):
        super().__init__()
        self.profile = profile
        self.action_space = spaces.Discrete(10)  # WASD, Shift, Space, LClick, RClick, Inventory, Special
        self.observation_space = spaces.Box(low=0, high=255, shape=(100, 100, 3), dtype=np.uint8)
        self.screen_size = (1920, 1080)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        pyautogui.moveTo(100, 100)
        return self._get_observation(), {}

    def step(self, action):
        self.profile.execute_action(action)
        obs = self._get_observation()
        reward = self.profile.calculate_reward(obs)
        done = False
        return obs, reward, done, False, {}

    def _get_observation(self):
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot)
        img = cv2.resize(img, (100, 100))
        return img

class AIEngine:
    def __init__(self, profile):
        self.profile = profile
        env_fn = lambda: GameEnv(profile)
        self.env = DummyVecEnv([env_fn])
        self.model = PPO("CnnPolicy", self.env, verbose=1)
        self.running = False

    def start_autonomous(self):
        self.running = True
        while self.running:
            obs = self.env.reset()[0]
            action, _ = self.model.predict(obs)
            self.env.step(action)
            time.sleep(0.05)

    def stop_autonomous(self):
        self.running = False

    def execute_command(self, params):
        self.profile.execute_command(params)