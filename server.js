const apiKey = process.env.VITE_OPENROUTER_API_KEY;

if (!apiKey) {
  throw new Error("VITE_OPENROUTER_API_KEY is missing");
}
const express = require('express');
const multer = require('multer');
const cors = require('cors');
require('dotenv').config();

const sttService = require('./sttService');
const aiService = require('./aiService');
const ttsService = require('./ttsService');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());
app.use(express.json());

// Receive audio, language, and process
app.post('/api/ask', upload.single('audio'), async (req, res) => {
  try {
    const { language } = req.body;
    const audioPath = req.file.path;

    // 1. Speech to Text
    const text = await sttService.transcribe(audioPath, language);

    // 2. GenAI
    const aiResponse = await aiService.getResponse(text, language);

    // 3. Text to Speech
    const ttsAudioPath = await ttsService.synthesize(aiResponse, language);

    // Send back the AI text and audio file path (or audio as base64)
    res.json({ text: aiResponse, audioUrl: `/audio/${ttsAudioPath}` });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Serve generated audio files
app.use('/audio', express.static('audio'));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));