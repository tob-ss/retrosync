const checkStatus = (DeviceID) => {
    const get_url = "http://37.27.217.84/daemon/status/"
    const x = {
        DeviceID: DeviceID
    }
    fetch(get_url, {
        method: "GET",
        headers: {
            "Content-type": "application/json",
        },
        body: JSON.stringify(x),
    })
        .then((response) => response.json())
        if (response == "1") {
            return 1
        }
        else {
            return 0
        }
}

export default checkStatus;