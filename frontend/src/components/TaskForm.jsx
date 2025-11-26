import React, { useState } from "react";
import { createTask } from "../api";

const TaskForm = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [status, setStatus] = useState("todo");
  const [dueDatetime, setDueDatetime] = useState("");
  const [created, setCreated] = useState(null);
  const [error, setError] = useState(null);

  async function onSubmit(e) {
    e.preventDefault();
    try {
      const payload = {
        title,
        description: description || null,
        status,
        due_datetime: new Date(dueDatetime).toISOString(),
      };
      const data = await createTask(payload);
      setCreated(data);
      setError(null);
    } catch (err) {
      setError(err.message);
      setCreated(null);
    }
  }

  return (
    <form
      onSubmit={onSubmit}
      style={{ display: "flex", flexDirection: "column", gap: 6 }}
    >
      <div>
        <label>Title</label>
        <br />
        <input
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label>Description</label>
        <br />
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div>
        <label>Status</label>
        <br />
        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="todo">To do</option>
          <option value="in_progress">In progress</option>
          <option value="done">Done</option>
        </select>
      </div>
      <div>
        <label>Due date/time</label>
        <br />
        <input
          type="datetime-local"
          required
          value={dueDatetime}
          onChange={(e) => setDueDatetime(e.target.value)}
        />
      </div>
      <button style={{ width: 64 }}>Create</button>

      {error && <p>Error: {error}</p>}
      {created && (
        <pre>
          Task Created Successfully <br /> {JSON.stringify(created, null, 2)}
        </pre>
      )}
    </form>
  );
};

export default TaskForm;
