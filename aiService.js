const axios = require('axios');

const OPENROUTER_API_KEY = process.env.VITE_OPENROUTER_API_KEY;

if (!OPENROUTER_API_KEY) {
  console.error('❌ VITE_OPENROUTER_API_KEY not set in .env');
}

module.exports.getResponse = async (userText, language = 'en') => {
  try {
    const systemPrompt = `You are an agricultural assistant for Indian farmers. Provide helpful, practical advice about farming, crops, and agriculture. If the user asks in Telugu, reply in Telugu. If in English, reply in English. Keep responses concise and actionable.`;

    const messages = [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: userText }
    ];

    const resp = await axios.post(
      'https://openrouter.ai/api/v1/chat/completions',
      {
        model: 'deepseek/deepseek-r1-0528:free',
        messages,
        temperature: 0.7,
        max_tokens: 500
      },
      {
        headers: {
          'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
          'HTTP-Referer': 'http://localhost:5000',
          'X-Title': 'Farmer AI Assistant',
          'Content-Type': 'application/json'
        },
        timeout: 30000
      }
    );

    const content =
      resp?.data?.choices?.[0]?.message?.content ||
      resp?.data?.choices?.[0]?.message?.text ||
      'Sorry, I could not generate an answer.';

    return content.toString().trim();
  } catch (err) {
    console.error('AI Service Error:', err.message);
    throw new Error(`AI Error: ${err.message}`);
  }
};