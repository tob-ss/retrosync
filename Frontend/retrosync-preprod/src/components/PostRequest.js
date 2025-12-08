import React, { useState } from 'react';

const SubmitSync = () => {
  const [deviceID, setDeviceID] = useState("");
  const [operation, setOperation] = useState("");
  const [gameID, setGameID] = useState("");
  const [completed, setCompleted] = useState("");


  const handleSubmit = (event) => {
    event.preventDefault();
    const syncRequest = {
      DeviceID: deviceID,
      Operation: operation,
      GameID: gameID,
      Completed: completed,
      TimeStamp: Date.now(),
    };
    fetch("http://37.27.217.84/sync/append", {
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
        setCompleted("");
      })
      .catch((error) => {
        console.log(error)
      });
  };

  return (
    <div >
      <div >
        <h1 >
          Post a sync request
        </h1>
        <div >
          <form
            onSubmit={handleSubmit}
          >
            <textarea
              type="text"
              name="Device Name"
              rows="1"
              placeholder="Device Name"
              value={deviceID}
              onChange={(event) => setDeviceID(event.target.value)}
              />
              <textarea
              type="text"
              name="Operation"
              rows="1"
              placeholder="Operation"
              value={operation}
              onChange={(event) => setOperation(event.target.value)}
              />
              <textarea
              type="text"
              name="Game ID"
              rows="1"
              placeholder="Game ID"
              value={gameID}
              onChange={(event) => setGameID(event.target.value)}
              />
              <textarea
              type="text"
              name="Completed"
              rows="1"
              placeholder="Completed"
              value={completed}
              onChange={(event) => setCompleted(event.target.value)}
              />
              <button >
                Submit
              </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default SubmitSync;