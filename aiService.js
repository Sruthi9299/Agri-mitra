const axios = require('axios');

async function getResponse(text, language) {
  try {
    const response = await axios.post(
      'https://openrouter.ai/api/v1/chat/completions',
      {
        model: 'deepseek/deepseek-r1-0528:free',
        messages: [
          {
            role: 'user',
            content: text
          }
        ]
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.VITE_OPENROUTER_API_KEY}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': process.env.SITE_URL || 'http://localhost:5000',
          'X-Title': 'Farmer App'
        }
      }
    );

    // Extract the AI response text
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('AI Service Error:', error.message);
    throw new Error(`AI Service failed: ${error.message}`);
  }
}

module.exports = { getResponse };