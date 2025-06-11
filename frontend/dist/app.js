import { renderUI, connectWebSocket } from "./ui";
const profiles = [];
async function init() {
    const response = await fetch("http://localhost:8000/profiles");
    const data = await response.json();
    profiles.push(...data.profiles);
    renderUI(profiles, data.running);
    connectWebSocket();
}
init();
