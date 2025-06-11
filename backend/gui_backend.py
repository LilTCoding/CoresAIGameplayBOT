import tkinter as tk
from tkinter import ttk
import requests
import json
import psutil

def create_gui():
    root = tk.Tk()
    root.title("CoresModTrainer")
    root.geometry("800x600")
    root.configure(bg="#f2f2f2")

    style = ttk.Style()
    style.configure("TCheckbutton", background="#f2f2f2", font=("Helvetica", 12))

    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(pady=20)

    tk.Label(frame, text="Select Game", font=("Helvetica", 16, "bold"), bg="#f2f2f2").pack(pady=10)
    toggle_vars = {}
    running_games = requests.get("http://localhost:8000/profiles").json()["running"]

    for profile in requests.get("http://localhost:8000/profiles").json()["profiles"]:
        var = tk.BooleanVar(value=profile in running_games)
        toggle = ttk.Checkbutton(
            frame,
            text=profile,
            variable=var,
            command=lambda p=profile, v=var: toggle_profile(p, v.get()),
            style="TCheckbutton"
        )
        toggle.pack(anchor="w", padx=20, pady=5)
        toggle_vars[profile] = var

forza_frame = tk.Frame(root, bg="#f2f2f2")
    forza_frame.pack(pady=10)
    tk.Label(forza_frame, text="Forza Horizon 5 Presets", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=5)

    tune_var = tk.StringVar()
    tune_options = [
        "MPG_300", "MPG_290", "MPG_250", "MPG_180",
        "Drift_Hoonicorn", "Drift_VinDiesel", "Drift_BrianOConnor", "Drift_Han", "Drift_DK",
        "Speed_BrianOConnor", "Speed_1", "Speed_2", "Speed_3", "Speed_4", "Speed_5",
        "Speed_6", "Speed_7", "Speed_8", "Speed_9", "Speed_10", "Speed_11", "Speed_12",
        "Speed_13", "Speed_14", "Speed_15"
    ]
    tk.Label(forza_frame, text="Select Tune Preset:", bg="#f2f2f2").pack()
    tune_menu = ttk.Combobox(forza_frame, textvariable=tune_var, values=tune_options)
    tune_menu.pack(pady=5)
    tk.Button(forza_frame, text="Apply Tune", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "tune_car", "preset": tune_var.get()})).pack(pady=5)

    tk.Button(forza_frame, text="Upgrade Car", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "upgrade_car"})).pack(pady=5)

warzone_frame = tk.Frame(root, bg="#f2f2f2")
    warzone_frame.pack(pady=10)
    tk.Label(warzone_frame, text="Warzone Waypoint", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=5)
    x_var = tk.StringVar()
    y_var = tk.StringVar()
    tk.Label(warzone_frame, text="X Coordinate:", bg="#f2f2f2").pack()
    tk.Entry(warzone_frame, textvariable=x_var).pack(pady=5)
    tk.Label(warzone_frame, text="Y Coordinate:", bg="#f2f2f2").pack()
    tk.Entry(warzone_frame, textvariable=y_var).pack(pady=5)
    tk.Button(warzone_frame, text="Set Waypoint", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "navigate_to_waypoint", "x": int(x_var.get()), "y": int(y_var.get())})).pack(pady=5)

    tk.Button(root, text="Start Autonomous", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("start_auto")).pack(pady=10)
    tk.Button(root, text="Stop Autonomous", font=("Helvetica", 12), bg="#ff3b30", fg="white",
              command=lambda: send_command("stop_auto")).pack(pady=10)

    tk.Label(root, text="Custom Command (JSON):", font=("Helvetica", 12), bg="#f2f2f2").pack(pady=10)
    command_entry = tk.Text(root, height=5, width=60, font=("Helvetica", 12))
    command_entry.pack(pady=10)
    tk.Button(root, text="Execute Command", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", json.loads(command_entry.get("1.0", tk.END)))).pack(pady=10)

    def toggle_profile(profile, state):
        if state:
            requests.post("http://localhost:8000/select_profile", json={"profile": profile})
        else:
            send_command("stop_auto")

    def send_command(command, params=None):
        requests.post("http://localhost:8000/ws", json={"command": command, "params": params or {}})

    root.mainloop()import tkinter as tk
from tkinter import ttk
import requests
import json
import psutil

def create_gui():
    root = tk.Tk()
    root.title("CoresModTrainer")
    root.geometry("800x600")
    root.configure(bg="#f2f2f2")

    style = ttk.Style()
    style.configure("TCheckbutton", background="#f2f2f2", font=("Helvetica", 12))

    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(pady=20)

    tk.Label(frame, text="Select Game", font=("Helvetica", 16, "bold"), bg="#f2f2f2").pack(pady=10)
    toggle_vars = {}
    running_games = requests.get("http://localhost:8000/profiles").json()["running"]

    for profile in requests.get("http://localhost:8000/profiles").json()["profiles"]:
        var = tk.BooleanVar(value=profile in running_games)
        toggle = ttk.Checkbutton(
            frame,
            text=profile,
            variable=var,
            command=lambda p=profile, v=var: toggle_profile(p, v.get()),
            style="TCheckbutton"
        )
        toggle.pack(anchor="w", padx=20, pady=5)
        toggle_vars[profile] = var

forza_frame = tk.Frame(root, bg="#f2f2f2")
    forza_frame.pack(pady=10)
    tk.Label(forza_frame, text="Forza Horizon 5 Presets", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=5)

    tune_var = tk.StringVar()
    tune_options = [
        "MPG_300", "MPG_290", "MPG_250", "MPG_180",
        "Drift_Hoonicorn", "Drift_VinDiesel", "Drift_BrianOConnor", "Drift_Han", "Drift_DK",
        "Speed_BrianOConnor", "Speed_1", "Speed_2", "Speed_3", "Speed_4", "Speed_5",
        "Speed_6", "Speed_7", "Speed_8", "Speed_9", "Speed_10", "Speed_11", "Speed_12",
        "Speed_13", "Speed_14", "Speed_15"
    ]
    tk.Label(forza_frame, text="Select Tune Preset:", bg="#f2f2f2").pack()
    tune_menu = ttk.Combobox(forza_frame, textvariable=tune_var, values=tune_options)
    tune_menu.pack(pady=5)
    tk.Button(forza_frame, text="Apply Tune", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "tune_car", "preset": tune_var.get()})).pack(pady=5)

    tk.Button(forza_frame, text="Upgrade Car", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "upgrade_car"})).pack(pady=5)

warzone_frame = tk.Frame(root, bg="#f2f2f2")
    warzone_frame.pack(pady=10)
    tk.Label(warzone_frame, text="Warzone Waypoint", font=("Helvetica", 14), bg="#f2f2f2").pack(pady=5)
    x_var = tk.StringVar()
    y_var = tk.StringVar()
    tk.Label(warzone_frame, text="X Coordinate:", bg="#f2f2f2").pack()
    tk.Entry(warzone_frame, textvariable=x_var).pack(pady=5)
    tk.Label(warzone_frame, text="Y Coordinate:", bg="#f2f2f2").pack()
    tk.Entry(warzone_frame, textvariable=y_var).pack(pady=5)
    tk.Button(warzone_frame, text="Set Waypoint", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", {"task": "navigate_to_waypoint", "x": int(x_var.get()), "y": int(y_var.get())})).pack(pady=5)

    tk.Button(root, text="Start Autonomous", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("start_auto")).pack(pady=10)
    tk.Button(root, text="Stop Autonomous", font=("Helvetica", 12), bg="#ff3b30", fg="white",
              command=lambda: send_command("stop_auto")).pack(pady=10)

    tk.Label(root, text="Custom Command (JSON):", font=("Helvetica", 12), bg="#f2f2f2").pack(pady=10)
    command_entry = tk.Text(root, height=5, width=60, font=("Helvetica", 12))
    command_entry.pack(pady=10)
    tk.Button(root, text="Execute Command", font=("Helvetica", 12), bg="#007aff", fg="white",
              command=lambda: send_command("execute", json.loads(command_entry.get("1.0", tk.END)))).pack(pady=10)

    def toggle_profile(profile, state):
        if state:
            requests.post("http://localhost:8000/select_profile", json={"profile": profile})
        else:
            send_command("stop_auto")

    def send_command(command, params=None):
        requests.post("http://localhost:8000/ws", json={"command": command, "params": params or {}})

    root.mainloop()