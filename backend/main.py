from flask import Flask, request, jsonify
from ai_engine import AIEngine
from game_profiles import EscapeFromTarkov, ForzaHorizon5, Warzone

app = Flask(__name__)
ai_engine = None

@app.route('/start', methods=['POST'])
def start():
    global ai_engine
    data = request.json
    game = data.get('game')
    profile = None
    
    if game == 'EscapeFromTarkov':
        profile = EscapeFromTarkov()
    elif game == 'ForzaHorizon5':
        profile = ForzaHorizon5()
    elif game == 'Warzone':
        profile = Warzone()
    
    if profile:
        ai_engine = AIEngine(profile)
        ai_engine.start_autonomous()
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Invalid game"})

@app.route('/stop', methods=['POST'])
def stop():
    global ai_engine
    if ai_engine:
        ai_engine.stop_autonomous()
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "AI not running"})

@app.route('/command', methods=['POST'])
def command():
    global ai_engine
    if ai_engine:
        data = request.json
        ai_engine.execute_command(data)
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "AI not running"})

def run_gui():
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    run_gui()

