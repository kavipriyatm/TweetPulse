const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

app.use(cors());

app.get('/api/sentiment', (req, res) => {
  res.json({ sentiment: 'positive' });
});

app.get('/api/wordcloud', (req, res) => {
  res.json({
    words: [
      { text: 'AI', value: 50 },
      { text: 'Social', value: 30 },
      { text: 'Media', value: 20 },
      { text: 'Trend', value: 40 },
      { text: 'Prediction', value: 25 },
    ]
  });
});

app.listen(port, () => {
  console.log(`Backend server is running at http://localhost:${port}`);
});
