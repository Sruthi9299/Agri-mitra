# 🎯 Quick Reference Card

## 🚀 Start in One Command
```bash
cd Agri/frontend/backend && python cli.py run
```

Then visit: **http://localhost:5000**

---

## 📋 Essential Commands

| Command | What It Does |
|---------|-------------|
| `python cli.py run` | Start backend |
| `python cli.py test` | Test connection |
| `python cli.py install` | Install dependencies |
| `python cli.py init-db` | Initialize database |
| `python cli.py status` | Check backend status |
| `python cli.py help` | Show all commands |

---

## 🌐 Important URLs

| URL | Purpose |
|-----|---------|
| http://localhost:5000 | Homepage |
| http://localhost:5000/farmer.html | Login/Register |
| http://localhost:5000/api/health | API Health Check |

---

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /api/send-otp | Send OTP |
| POST | /api/register | Register user |
| POST | /api/login | Login user |
| GET | /api/me | Get current user |
| PUT | /api/profile | Update profile |
| POST | /api/ask | Ask AI question |
| GET | /api/health | Health check |

---

## ⚙️ Configuration

**File:** `Agri/frontend/backend/.env`

```ini
# Important variables to configure:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=agri_mitra
PORT=5000
FLASK_DEBUG=1
OTP_DEMO=1234
```

---

## 🧪 Demo Login Credentials

| Field | Value |
|-------|-------|
| Phone | Any 10-digit number (e.g., 9876543210) |
| OTP | 1234 (in demo mode) |

---

## 📁 Key Files

| File | Location | Purpose |
|------|----------|---------|
| app.py | Agri/frontend/backend/ | Main backend |
| config.js | Agri/frontend/ | API configuration |
| .env | Agri/frontend/backend/ | Environment variables |
| test_connection.py | Agri/frontend/backend/ | Run tests |

---

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| "Address already in use" | Change PORT in .env |
| "Can't connect to MySQL" | Check MySQL is running |
| "404 on API calls" | Check backend is running |
| "CORS errors" | Already configured, refresh page |

---

## 📚 Documentation

| Document | Read For |
|----------|----------|
| 00_START_HERE.md | Quick overview |
| FINAL_SUMMARY.md | Complete summary |
| QUICK_START.md | Quick reference |
| ARCHITECTURE.md | System design |
| DEVELOPER_CHECKLIST.md | Checklists |

---

## ✅ Checklist Before Starting

- [ ] Navigate to `Agri/frontend/backend/`
- [ ] Check `.env` file exists
- [ ] MySQL running on localhost
- [ ] Port 5000 is free
- [ ] Python 3.8+ installed
- [ ] Required packages available

---

## 🎯 3-Step Setup

```
1. Navigate to backend
   cd Agri/frontend/backend

2. Install and start
   python cli.py run

3. Open browser
   http://localhost:5000
```

Done! 🎉

---

## 🔑 Key Concepts

| Term | Meaning |
|------|---------|
| API_BASE | Backend URL used by frontend |
| FLASK_DEBUG | Development auto-reload mode |
| OTP | One-Time Password for login |
| CORS | Cross-Origin Resource Sharing |
| Endpoint | API URL that handles requests |

---

## 📊 Architecture in 1 Minute

```
User Browser
    ↓
Flask Backend (localhost:5000)
    ├─ Serves HTML/CSS/JS
    ├─ Routes API calls to Python code
    └─ Manages database queries
    
Database (MySQL)
    └─ Stores user data
```

---

## 🚀 Next Steps

1. Start backend: `python cli.py run`
2. Open: `http://localhost:5000`
3. Test login with OTP: 1234
4. Explore features
5. Start developing!

---

## 💡 Pro Tips

- Use `F12` to open browser DevTools
- Check Network tab for API calls
- Check Console tab for errors
- Use `FLASK_DEBUG=1` for auto-reload
- Read error messages carefully
- Check `.env` for configuration

---

**That's all you need to know to get started!** ✨

For more details, see the documentation files.

---

**Created:** February 1, 2026  
**Status:** ✅ Ready to Use
