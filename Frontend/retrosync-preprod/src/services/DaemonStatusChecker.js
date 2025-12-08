function makeGetRequest(path) {
    return new Promise(function (resolve, reject) {
        fetch(path).then(
            (response) => {
                var result = response.data;
                console.log('Processing REquest');
                resolve(result);
            },
                (error) => {
                    reject(error)
                }
        );
    });
}

async function checkStatus(DeviceID) {
    const params = new URLSearchParams();
    params.append("DeviceID", DeviceID);
    let result = await makeGetRequest(`http://37.27.217.84/daemon/status?${params}`);
    if (response === "1") {
        return 1
    }
    else {
        return 0
    }
}

export default checkStatus;