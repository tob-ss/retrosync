const postSyncRequest = (syncRequest) => {
    fetch("http://37.27.217.84/sync/append/", {
    method: "POST",
    headers: {
        "Content-type": "application/json",
    },
    body: JSON.stringify(syncRequest),
    })
    .then((response) => response.json())
    .then((newRequest) => {
        setDeviceID("");
        setOperation("");
        setGameID("");
    })
    .catch((error) => {
        console.log(error)
    });
}

export default postSyncRequest;