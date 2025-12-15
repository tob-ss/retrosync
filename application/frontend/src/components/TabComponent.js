import React, { useState } from "react";
import styled from "styled-components";
import cloudDashboard from "./CloudDashboard";

const Tab = styled.button`
  font-size: 20px;
  padding: 10px 60px;
  cursor: pointer;
  opacity: 0.6;
  background: white;
  border: 0;
  outline: 0;
  ${({ active }) =>
    active &&
    `
    border-bottom: 2px solid black;
    opacity: 1;
  `}
`;
const ButtonGroup = styled.div`
  display: flex;
`;
const types = ["Cloud", "Local"];
function TabGroup() {
  const [active, setActive] = useState(types[0]);
  return (
    <>
      <ButtonGroup>
        {types.map((type) => (
          <Tab
            key={type}
            active={active === type}
            onClick={() => setActive(type)}
          >
            {type}
          </Tab>
          /* remove the paragraph below, and replace with some logic that does two things
          firstly, checks the active type; if its cloud, should then show the cloud dashboard component,
          if its local, show the local dashboard component*/
        ))}
      </ButtonGroup>
      {cloudDashboard()}
    </>
  );
}

export default TabGroup;
