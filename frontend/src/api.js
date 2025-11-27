const API_URL = "http://localhost:8000";

export async function sendForPrediction(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData
  });

  return res.json();
}

export async function retrainModel(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_URL}/retrain`, {
    method: "POST",
    body: formData
  });

  return res.json();
}