// app.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const predictRoute = require('./routes/predict'); // your predict router

const app = express();

app.use(cors());
app.use(bodyParser.json());

// Simple test route
app.get('/', (req, res) => {
  res.send('Server is up and running!');
});

// Mount your predict route at /predict
app.use('/predict', predictRoute);

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
