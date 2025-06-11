from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import uvicorn
from ai_engine import AIEngine
from input_controller import InputController
from game_profiles import GameProfile, EscapeFromTarkov, ForzaHorizon5, Fortnite, Warzone, ArmaReforger, DCS
from gui_backend import create_gui
import threading
import psutil
import asyncio

app = FastAPI(title="CoresModTrainer API")

# Hardcoded game profiles
GAME_PROFILES = {
    "EscapeFromTarkov": EscapeFromTarkov(),
    "ForzaHorizon5": ForzaHorizon5(),
    "Fortnite": Fortnite(),
    "Warzone": Warzone(),
    "ArmaReforger": ArmaReforger(),
    "DCS": DCS()
}
ACTIVE_PROFILE = None
AI_ENGINE = None
INPUT_CONTROLLER = InputController()

@app.get("/profiles")
async def get_profiles():
    running_games = detect_running_games()
    return {"profiles": list(GAME_PROFILES.keys()), "running": running_games}

@app.post("/select_profile")
async def select_profile(profile: str):
    global ACTIVE_PROFILE, AI_ENGINE
    if profile in GAME_PROFILES:
        ACTIVE_PROFILE = GAME_PROFILES[profile]
        AI_ENGINE = AIEngine(ACTIVE_PROFILE)
        return {"status": "Profile selected", "profile": profile}
    return JSONResponse(status_code=400, content={"error": "Invalid profile"})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            command = data.get("command")
            params = data.get("params", {})
            if command == "start_auto":
                AI_ENGINE.start_autonomous()
            elif command == "stop_auto":
                AI_ENGINE.stop_autonomous()
            elif command == "execute":
                AI_ENGINE.execute_command(params)
            await websocket.send_json({"status": "Command received", "command": command})
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

def detect_running_games():
    running = []
    for proc in psutil.process_iter(['name']):
        for game in GAME_PROFILES:
            if game.lower() in proc.info['name'].lower():
                running.append(game)
    return running

def run_gui():
    create_gui()

if __name__ == "__main__":
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)

