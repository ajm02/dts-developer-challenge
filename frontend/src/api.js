export const API_BASE = "http://localhost:8000";

export async function createTask(payload) {
  const response = await fetch(`${API_BASE}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) throw new Error("API error");
  return response.json();
}
