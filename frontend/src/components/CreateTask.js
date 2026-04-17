import React, { useState } from "react";
import API from "../api/api";

function CreateTask() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    assigned_to: ""
  });

  const submit = async (e) => {
    e.preventDefault();

    await API.post("tasks/create/", {
      ...form,
      role: "admin",
      created_by: 1
    });

    alert("Task Created");
  };

  return (
    <form onSubmit={submit}>
      <input placeholder="Title"
        onChange={e => setForm({ ...form, title: e.target.value })} />

      <input placeholder="Description"
        onChange={e => setForm({ ...form, description: e.target.value })} />

      <input placeholder="Assign User ID"
        onChange={e => setForm({ ...form, assigned_to: e.target.value })} />

      <button type="submit">Create Task</button>
    </form>
  );
}

export default CreateTask;