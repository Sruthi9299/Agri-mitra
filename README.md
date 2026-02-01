# Agri Mitra – Full Stack Application

Smart farming app with **user registration/login**, **profile**, and **AI agriculture voice assistant** (multilingual speech → text → AI → translation → text-to-speech + optional image).

## Project structure

```
frontend/                    # Project root (your UI + backend)
├── backend/                  # Python Flask backend
│   ├── app.py               # Flask app, CORS, routes
│   ├── config.py            # Env config (MySQL, API keys)
│   ├── database.py          # MySQL connection + init_db
│   ├── requirements.txt     # Python deps
│   ├── .env.example         # Copy to .env and fill
│   ├── routes/
│   │   ├── auth.py          # /api/send-otp, /api/register, /api/login
│   │   ├── profile.py       # /api/me, /api/profile
│   │   └── ai.py            # /api/ask (text/audio), /api/uploads/<path>
│   ├── services/
│   │   ├── speech_to_text.py # Whisper (OpenAI) or Google Speech
│   │   ├── gen_ai.py        # OpenAI or Gemini (agriculture prompt)
│   │   ├── translate.py     # Google Translation (optional)
│   │   ├── text_to_speech.py# Google TTS / Azure TTS (optional)
│   │   └── image_gen.py     # DALL-E (optional)
│   └── utils/
│       ├── auth.py          # Signed token (session)
│       └── otp.py           # OTP generate/verify
├── config.js                # API_BASE (same origin when deployed)
├── index.html               # Home
├── farmer.html / farmer.js  # Login / Register (wired to backend)
├── user.html                # Profile (wired to /api/profile)
├── ai.html                  # Voice assistant (wired to /api/ask)
├── home.js, home.css        # Nav + username from /api/me
├── .replit, replit.nix      # Replit run config
└── README.md                 # This file
```

## Backend APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/send-otp` | Body: `{ "phone": "10-digit" }` → sends OTP (demo: 1234) |
| POST | `/api/register` | Body: full_name, phone, otp, age, dob, preferred_language, location, soil_type |
| POST | `/api/login` | Body: phone, otp → returns token + full_name |
| GET | `/api/me` | Header: `Authorization: Bearer <token>` → { full_name, logged_in } |
| GET | `/api/profile` | Header: token → farmer details, crop, photos |
| POST | `/api/ask` | JSON: `{ "text", "language" }` or FormData: audio file + language → { text, audioUrl?, imageUrl? } |
| GET | `/api/uploads/<path>` | Serves TTS/Images |
| GET | `/api/health` | Health check |

## Local development

1. **MySQL**  
   Create database: `CREATE DATABASE agri_mitra;`  
   Set in `.env`: `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_PORT`.

2. **Backend**  
   ```bash
   cd backend
   cp .env.example .env   # edit .env with keys
   pip install -r requirements.txt
   python app.py
   ```  
   Backend runs at `http://localhost:5000`.

3. **Frontend**  
   Open `index.html` in browser (or use a static server from project root).  
   `config.js` sets `API_BASE = 'http://localhost:5000'` for localhost.

4. **Demo auth**  
   Set `OTP_DEMO=1234` in `.env`. Any 10-digit phone can login/register with OTP `1234`.

## Replit deployment

1. In Replit, open this repo (frontend folder as root).
2. Add **Secrets** (Environment variables):  
   `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`, `SECRET_KEY`, optionally `OPENAI_API_KEY`, `GEMINI_API_KEY`, etc. (see `.env.example`).
3. **Run**: `.replit` runs `cd backend && pip install -r requirements.txt && python app.py`.  
   Flask serves both API and static frontend (index.html, ai.html, etc.) from project root.
4. **Deploy**: Use Replit Deploy; deployment command runs gunicorn in `backend/`.  
   Set Replit’s public URL; `config.js` will use same origin for API.

## GitHub

- Push the whole project (including `backend/`, `.replit`, `replit.nix`, `config.js`, `README.md`) to a GitHub repo.
- Clone for local dev or import into Replit from GitHub.

## AI voice assistant flow

1. **User**: Clicks bot or types/speaks in ai.html.
2. **Input**: Text sent as JSON, or audio sent as FormData → backend.
3. **Speech-to-Text**: If audio → OpenAI Whisper (or Google Speech) → text.
4. **Translation (optional)**: If language ≠ English → user query translated to English for AI.
5. **Gen AI**: Agriculture-focused prompt + query → OpenAI or Gemini → response text.
6. **Translation (optional)**: Response translated to user’s selected language.
7. **Text-to-Speech**: Google TTS / Azure TTS (if configured) → audio file; else frontend uses browser TTS.
8. **Image (optional)**: DALL-E generates context image from response → `imageUrl` returned.
9. **Output**: Bot shows text + optional image; plays audio (or browser TTS).

## Env vars (backend `.env`)

- **Required for DB**: `MYSQL_*`, `SECRET_KEY`
- **Demo OTP**: `OTP_DEMO=1234`
- **AI**: `OPENAI_API_KEY` (chat + Whisper STT + DALL-E), or `GEMINI_API_KEY` with `AI_PROVIDER=gemini`
- **Translation**: `GOOGLE_TRANSLATE_API_KEY` or Google Cloud credentials
- **TTS**: `TTS_PROVIDER=google` or `azure` + `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION`

Your existing UI (design, layout, styles) is unchanged; only backend and API wiring (auth, profile, AI, config) were added.
