import React, { useEffect, useState } from "react";
import API from "../api/api";

function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    API.get("tasks/").then(res => setTasks(res.data));
  }, []);

  const updateStatus = async (id, status) => {
    await API.patch(`tasks/update/${id}/`, { status });
    window.location.reload();
  };

  return (
    <div>
      <h2>Tasks</h2>

      {tasks.map(task => (
        <div key={task.id}>
          <h4>{task.title}</h4>
          <p>{task.description}</p>
          <p>Status: {task.status}</p>

          <button onClick={() => updateStatus(task.id, "in_progress")}>
            In Progress
          </button>

          <button onClick={() => updateStatus(task.id, "completed")}>
            Complete
          </button>
        </div>
      ))}
    </div>
  );
}


export default TaskList;