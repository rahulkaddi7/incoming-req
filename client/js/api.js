const API_BASE = "http://127.0.0.1:8000";

async function processRequest(request) {
  const response = await fetch(`${API_BASE}/requests/process`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      request: request,
    }),
  });

  if (!response.ok) throw new Error("Failed to process request.");

  return await response.json();
}

async function getDashboard(type) {
  const response = await fetch(`${API_BASE}/dashboard/${type}`);

  if (!response.ok) throw new Error("Unable to load dashboard.");

  return await response.json();
}
