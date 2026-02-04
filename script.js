const video = document.getElementById('webcam');
const logs = document.getElementById('security-logs');

// Start Webcam
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => { video.srcObject = stream; })
        .catch((err) => { console.log("System Error: ", err); });
}

// Function to add logs
function addLog(msg, type = "info") {
    const p = document.createElement('p');
    p.style.color = type === "alert" ? "#ff003c" : "#00f3ff";
    p.innerText = `[${new Date().toLocaleTimeString()}] > ${msg}`;
    logs.prepend(p);
}

// Simulate connection to Python backend
setInterval(() => {
    addLog("HEARTBEAT_CHECK: OK");
}, 5000);
