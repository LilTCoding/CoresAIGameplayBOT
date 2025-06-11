CoresModTrainer
An AI-powered PC gaming bot for pro-level gameplay with an iOS-styled GUI.

Setup
Backend (Python):
Install dependencies: pip install fastapi uvicorn opencv-python numpy stable-baselines3 gymnasium pydirectinput pyautogui psutil
Run: python backend/main.py

Frontend (TypeScript):
Install Node.js and dependencies: npm install
Compile: npx tsc
Serve: npx serve dist
Create an index.html in dist/ to load the frontend:
<!DOCTYPE html>
<html>
<head>
    <title>CoresModTrainer</title>
</head>
<body>
    <div id="app"></div>
    <script src="app.js"></script>
</body>
</html>

Usage:
Launch the GUI (Python Tkinter or TypeScript HTML).
Toggle games on/off with iOS-style switches (auto-detects running games).
For Forza Horizon 5, select tune presets (e.g., MPG_300, Drift_Hoonicorn) or upgrade cars.
For Warzone, input waypoint coordinates (x, y).
Start/Stop autonomous mode or use JSON commands.

Supported Games
Escape from Tarkov: Inventory management, SCAV/PMC detection.
Forza Horizon 5: Goliath races, earn millions, car upgrades, custom tunes (MPG, drift, speed).
Fortnite: Ninja-style building, precise aiming.
Warzone: Top-tier aim, waypoint navigation.
Arma Reforger: Tactical movement.
DCS: Expert plane control.

Example Commands
Forza: {"task": "tune_car", "preset": "Drift_Hoonicorn"}, {"task": "upgrade_car"}
Warzone: {"task": "navigate_to_waypoint", "x": 500, "y": 300}
Tarkov: {"task": "manage_inventory"}

Notes
For offline, private use (Steam-compatible for Forza).
Extend game_profiles.py for more games.
Requires screen capture permissions and game window focus.
Tune presets in Forza are placeholders; customize with real values.