import React, { useState } from 'react';
import { useRef } from 'react';
import checkStatus  from '../services/DaemonStatusChecker';

const SubmitSync = () => {
  const [deviceID, setDeviceID] = useState("");
  const [operation, setOperation] = useState("");
  const [gameID, setGameID] = useState("");

  const buttonRef = useRef(null)

  const handleSubmit = (event) => {
    if (buttonRef.current && !buttonRef.current.disabled) {
      buttonRef.current.disabled = true;
      event.preventDefault();
      const syncRequest = {
        DeviceID: deviceID,
        Operation: operation,
        GameID: gameID,
        Completed: false,
        TimeStamp: Date.now() / 1000,
      };
      const status = checkStatus(deviceID)
      if (status === 1) {
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
      else {
        console.log("Could not connect to device")
      };
    }
    buttonRef.current.disabled = false;
    
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
              <button ref={buttonRef}>
                Submit
              </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default SubmitSync;