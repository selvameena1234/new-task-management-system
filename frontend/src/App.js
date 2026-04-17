import React from "react";
import TaskList from "./components/TaskList";
import CreateTask from "./components/CreateTask";

function App() {
  return (
    <div>
      <h1>Task Management System</h1>
      <CreateTask />
      <TaskList />
    </div>
  );
}

export default App;