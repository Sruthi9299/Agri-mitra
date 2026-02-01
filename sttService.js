module.exports.transcribe = async (audioPath, language) => {
  // Integrate with Google Speech-to-Text, Azure, or any STT API
  // For now, return dummy text
  return language === 'te' ? 'మీరు ఏమి అడిగారు?' : 'What did you ask?';
};