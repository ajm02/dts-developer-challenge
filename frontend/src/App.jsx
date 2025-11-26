import React from "react";
import TaskForm from "./components/TaskForm";

const App = () => {
  return (
    <div style={{ padding: 24 }}>
      <h1>HMCTS Task Creator</h1>
      <TaskForm />
    </div>
  );
};

export default App;
