import { Command, GameProfile } from "./types";

export function renderUI(profiles: GameProfile[], running: string[]) {
    const container = document.getElementById("app")!;
    container.innerHTML = `
        <style>
            .toggle-switch {
                position: relative;
                display: inline-block;
                width: 51px;
                height: 31px;
                margin-left: 10px;
            }
            .toggle-switch input {
                opacity: 0;
                width: 0;
                height: 0;
            }
            .slider {
                position: absolute;
                cursor: pointer;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-color: #ccc;
                transition: .4s;
                border-radius: 34px;
            }
            .slider:before {
                position: absolute;
                content: "";
                height: 25px;
                width: 25px;
                left: 3px;
                bottom: 3px;
                background-color: white;
                transition: .4s;
                border-radius: 50%;
            }
            input:checked + .slider {
                background-color: #007aff;
            }
            input:checked + .slider:before {
                transform: translateX(20px);
            }
            .profile-item {
                display: flex;
                align-items: center;
                margin: 10px 0;
                font-family: -apple-system, Helvetica, sans-serif;
            }
            button {
                padding: 10px 20px;
                margin: 10px;
                border: none;
                border-radius: 10px;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            select, input {
                padding: 10px;
                margin: 10px;
                border-radius: 10px;
                font-size: 16px;
            }
            #start-auto { background-color: #007aff; }
            #stop-auto { background-color: #ff3b30; }
            #execute-command, #apply-tune, #upgrade-car, #set-waypoint { background-color: #007aff; }
            textarea {
                width: 100%;
                height: 100px;
                margin: 10px 0;
                border-radius: 10px;
                padding: 10px;
            }
        </style>
        <h2>Select Game</h2>
        <div id="profiles"></div>
        <h3>Forza Horizon 5 Presets</h3>
        <select id="tune-preset">
            <option value="MPG_300">300 MPG</option>
            <option value="MPG_290">290 MPG</option>
            <option value="MPG_250">250 MPG</option>
            <option value="MPG_180">180 MPG</option>
            <option value="Drift_Hoonicorn">Drift: Hoonicorn</option>
            <option value="Drift_VinDiesel">Drift: Vin Diesel</option>
            <option value="Drift_BrianOConnor">Drift: Brian O'Connor</option>
            <option value="Drift_Han">Drift: Han</option>
            <option value="Drift_DK">Drift: DK</option>
            <option value="Speed_BrianOConnor">Speed: Brian O'Connor</option>
            <option value="Speed_1">Speed: 1</option>
            <option value="Speed_2">Speed: 2</option>
            <option value="Speed_3">Speed: 3</option>
            <option value="Speed_4">Speed: 4</option>
            <option value="Speed_5">Speed: 5</option>
            <option value="Speed_6">Speed: 6</option>
            <option value="Speed_7">Speed: 7</option>
            <option value="Speed_8">Speed: 8</option>
            <option value="Speed_9">Speed: 9</option>
            <option value="Speed_10">Speed: 10</option>
            <option value="Speed_11">Speed: 11</option>
            <option value="Speed_12">Speed: 12</option>
            <option value="Speed_13">Speed: 13</option>
            <option value="Speed_14">Speed: 14</option>
            <option value="Speed_15">Speed: 15</option>
        </select>
        <button id="apply-tune">Apply Tune</button>
        <button id="upgrade-car">Upgrade Car</button>
        <h3>Warzone Waypoint</h3>
        <input type="number" id="waypoint-x" placeholder="X Coordinate">
        <input type="number" id="waypoint-y" placeholder="Y Coordinate">
        <button id="set-waypoint">Set Waypoint</button>
        <button id="start-auto">Start Autonomous</button>
        <button id="stop-auto">Stop Autonomous</button>
        <h3>Custom Command (JSON)</h3>
        <textarea id="command-input"></textarea>
        <button id="execute-command">Execute Command</button>
    `;

    const profilesDiv = document.getElementById("profiles")!;
    profiles.forEach(profile => {
        const div = document.createElement("div");
        div.className = "profile-item";
        div.innerHTML = `
            <span>${profile.name}</span>
            <label class="toggle-switch">
                <input type="checkbox" ${running.includes(profile.name) ? "checked" : ""}>
                <span class="slider"></span>
            </label>
        `;
        profilesDiv.appendChild(div);
    });
}

export function connectWebSocket() {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onopen = () => console.log("WebSocket connected");
    ws.onmessage = (event) => console.log("Received:", JSON.parse(event.data));
    ws.onclose = () => console.log("WebSocket closed");

    document.getElementById("start-auto")?.addEventListener("click", () => sendCommand(ws, { command: "start_auto" }));
    document.getElementById("stop-auto")?.addEventListener("click", () => sendCommand(ws, { command: "stop_auto" }));
    document.getElementById("execute-command")?.addEventListener("click", () => {
        const input = (document.getElementById("command-input") as HTMLTextAreaElement).value;
        sendCommand(ws, { command: "execute", params: JSON.parse(input) });
    });
    document.getElementById("apply-tune")?.addEventListener("click", () => {
        const preset = (document.getElementById("tune-preset") as HTMLSelectElement).value;
        sendCommand(ws, { command: "execute", params: { task: "tune_car", preset } });
    });
    document.getElementById("upgrade-car")?.addEventListener("click", () => {
        sendCommand(ws, { command: "execute", params: { task: "upgrade_car" } });
    });
    document.getElementById("set-waypoint")?.addEventListener("click", () => {
        const x = parseInt((document.getElementById("waypoint-x") as HTMLInputElement).value);
        const y = parseInt((document.getElementById("waypoint-y") as HTMLInputElement).value);
        sendCommand(ws, { command: "execute", params: { task: "navigate_to_waypoint", x, y } });
    });

    document.querySelectorAll(".toggle-switch input").forEach(input => {
        input.addEventListener("change", (e) => {
            const profile = (e.target as HTMLElement).parentElement!.previousElementSibling!.textContent!;
            sendCommand(ws, {
                command: "execute",
                params: { task: "select_profile", profile, state: (e.target as HTMLInputElement).checked }
            });
        });
    });
}

function sendCommand(ws: WebSocket, command: Command) {
    if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(command));
    }
}
