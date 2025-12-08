async function getDaemonStatus(deviceID) {
    try {
        const params = new URLSearchParams();
        params.append("DeviceID", deviceID)
        let daemonStatus = await new Promise(
            fetch(`http://37.27.217.84/daemon/status?${params}`)
        );
        console.log(`The Current Status of the Daemon is: ${daemonStatus}`)
    } catch (error) {
        console.log("Error:", error)
    }
}

export default getDaemonStatus;