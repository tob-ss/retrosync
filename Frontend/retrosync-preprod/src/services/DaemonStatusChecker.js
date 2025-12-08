const checkStatus = (DeviceID) => {
    const get_url = "http://37.27.217.84/daemon/status/"
    const params = new URLSearchParams();
    params.append("DeviceID", DeviceID);
    const response = fetch(`http://37.27.217.84/daemon/status?${params}`);
    if (response === "1") {
        return 1
    }
    else {
        return 0
    }
}

export default checkStatus;