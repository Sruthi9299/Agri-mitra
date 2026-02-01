require("dotenv").config();
const express = require('express');
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

const aiService = require('./services/aiService');
const sttService = require('./services/sttService');
const ttsService = require('./services/ttsService');

const upload = multer({ dest: 'uploads/' });
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'frontend')));
app.use('/audio', express.static(path.join(__dirname, 'audio')));

// Ensure upload and audio directories exist
if (!fs.existsSync('uploads')) fs.mkdirSync('uploads');
if (!fs.existsSync('audio')) fs.mkdirSync('audio');

// Accept either audio upload or plain text
app.post('/api/ask', upload.single('audio'), async (req, res) => {
  try {
    const language = req.body.language || 'en';
    let userText = req.body.text || '';

    if (req.file) {
      userText = await sttService.transcribe(req.file.path, language);
      fs.unlink(req.file.path, () => {});
    }

    if (!userText) {
      return res.status(400).json({ error: 'No audio or text provided' });
    }

    const aiResponse = await aiService.getResponse(userText, language);
    const ttsResult = await ttsService.synthesize(aiResponse, language);

    res.json({
      text: aiResponse,
      audioUrl: ttsResult ? ttsResult.audioUrl : null
    });
  } catch (err) {
    console.error('Error:', err);
    res.status(500).json({ error: err.message || 'Server error' });
  }
});

// Serve index.html for SPA routing
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
  console.log(`📝 API Key configured: ${process.env.OPENROUTER_API_KEY ? 'Yes' : 'No'}`);
});