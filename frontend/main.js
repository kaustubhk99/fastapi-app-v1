// API is on same origin, no CORS issues!
const API_BASE = "/api";

const pingBtn = document.getElementById("pingBtn");
const dataBtn = document.getElementById("dataBtn");
const resultEl = document.getElementById("result");

// Test basic API call
pingBtn.addEventListener("click", async () => {
  resultEl.textContent = "Loading...";
  try {
    const res = await fetch(API_BASE);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    resultEl.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    resultEl.textContent = `Error: ${err.message}`;
  }
});

// Test data endpoint
dataBtn.addEventListener("click", async () => {
  resultEl.textContent = "Loading...";
  try {
    const res = await fetch(`${API_BASE}/data`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    resultEl.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    resultEl.textContent = `Error: ${err.message}`;
  }
});

console.log("App initialized. API Base:", API_BASE);