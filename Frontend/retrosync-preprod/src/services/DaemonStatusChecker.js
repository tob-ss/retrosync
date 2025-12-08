async function getDaemonStatus(deviceID) {
    try {
        const params = new URLSearchParams();
        params.append("DeviceID", deviceID)
        let daemonStatus = await fetch(`http://37.27.217.84/daemon/status?${params}`);
        let data = await daemonStatus.json();
        console.log(`The Current Status of the Daemon is: ${data}`)
    } catch (error) {
        console.log("Error:", error)
    }
}

export default getDaemonStatus;