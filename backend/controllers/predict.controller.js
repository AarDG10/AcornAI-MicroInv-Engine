const axios = require('axios');

exports.predict = async (req, res) => {
  console.log("💡 Hit /predict endpoint");
  const inputData = req.body;
  console.log("🧾 Received inputData:", inputData);

  try {
    const response = await axios.post('http://localhost:8000/predict', inputData);
    console.log("📬 FastAPI prediction:", response.data);
    res.json({ prediction: response.data.prediction });
  } catch (error) {
    console.error("❌ Error communicating with FastAPI:", error.message);
    res.status(500).json({ error: 'Prediction failed', details: error.message });
  }
};
