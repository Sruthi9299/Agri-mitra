# 🌾 Agri Mitra - Smart Farming Platform

A Flask-based backend for agricultural management with frontend and backend fully integrated!

## 🚀 Quick Start

### Start the Application (2 minutes)

```bash
cd Agri/frontend/backend
python cli.py run
```

Then open your browser:
```
http://localhost:5000
```

## ✨ What's Integrated

✅ **Frontend** - HTML/CSS/JavaScript frontend  
✅ **Backend** - Flask API with MySQL database  
✅ **Integration** - Connected via RESTful APIs  
✅ **Authentication** - OTP-based user login  
✅ **Database** - MySQL for persistent data  
✅ **Configuration** - Environment-based setup  

## 📚 Documentation

### Start with these files:

1. **[README.md](README.md)** (this file) - Overview
2. **[INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)** - Integration details
3. **[QUICK_START.md](Agri/frontend/backend/QUICK_START.md)** - Quick reference
4. **[DEVELOPER_CHECKLIST.md](DEVELOPER_CHECKLIST.md)** - Checklists
5. **[ARCHITECTURE.md](Agri/ARCHITECTURE.md)** - System design

## 🎯 Features

### User Management
✅ OTP-based authentication  
✅ User registration and login  
✅ User profile management  
✅ Language preferences  

### Core Features
- 🌾 Crop information and recommendations
- 🏥 Disease detection and management
- 🌦️ Weather alerts and forecasts
- 💰 Market prices and trends
- 🏛️ Government schemes information
- 📞 Contact support system

### AI Services
- 🤖 AI-powered farmer assistant
- 🗣️ Speech-to-text support
- 🔊 Text-to-speech output
- 🌐 Multi-language support

## 📋 Installation

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- Node.js (optional, for Node services)

### Setup Steps

```bash
# 1. Navigate to backend
cd Agri/frontend/backend

# 2. Install dependencies
python cli.py install

# 3. Configure environment
# Edit .env file with your MySQL credentials

# 4. Initialize database
python cli.py init-db

# 5. Start the application
python cli.py run
```

## 🔌 API Endpoints

### Authentication
```
POST   /api/send-otp       Send OTP to phone number
POST   /api/register       Register new farmer
POST   /api/login          Login farmer
```

### Profile
```
GET    /api/me             Get current user info
PUT    /api/profile        Update user profile
```

### AI Services
```
POST   /api/ask            Ask AI question
POST   /api/suggestions    Get crop suggestions
```

### Health
```
GET    /api/health         Check backend status
```

## 🧪 Testing

### Test Connection
```bash
python test_connection.py
```

### Manual Testing
1. Open `http://localhost:5000`
2. Navigate to Login/Register
3. Enter phone number: `9876543210`
4. Send OTP
5. Enter demo OTP: `1234`
6. Submit

## 🔧 Development

### Using the CLI Tool
```bash
python cli.py run          # Start backend
python cli.py test         # Test connection
python cli.py install      # Install dependencies
python cli.py init-db      # Initialize database
python cli.py status       # Check backend status
```

### Development Mode
- Backend runs on `http://localhost:5000`
- Hot reload enabled with `FLASK_DEBUG=1`
- Demo OTP mode enabled for testing

## 📁 Project Structure

```
Agri/
├── frontend/
│   ├── config.js           ← API configuration
│   ├── index.html          ← Homepage
│   ├── farmer.html         ← Login/Register
│   ├── *.js                ← Frontend scripts
│   └── backend/            ← Flask backend
│       ├── app.py          ← Main application
│       ├── .env            ← Configuration
│       ├── cli.py          ← Development CLI
│       ├── test_connection.py
│       ├── routes/         ← API endpoints
│       ├── services/       ← Business logic
│       └── utils/          ← Helpers
```

## 🔐 Security Notes

### Development
- ⚠️ OTP_DEMO_MODE=1 enabled (for testing)
- ⚠️ FLASK_DEBUG=1 enabled
- ⚠️ Default credentials

### Before Production
- 🔒 Change SECRET_KEY to random string
- 🔒 Set FLASK_DEBUG=0
- 🔒 Disable OTP_DEMO_MODE
- 🔒 Update MySQL credentials
- 🔒 Use HTTPS
- 🔒 Restrict CORS origins

## ⚙️ Configuration

The `.env` file controls:

```ini
# Flask
FLASK_ENV=development
FLASK_DEBUG=1
PORT=5000

# MySQL
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=agri_mitra

# Authentication
OTP_DEMO_MODE=1
OTP_DEMO=1234

# Security
SECRET_KEY=change-this-in-production
```

## 🆘 Troubleshooting

### Backend won't start
```bash
# Check if MySQL is running
# Check if port 5000 is free
# Check .env file is configured
python test_connection.py
```

### Database connection failed
```bash
# Verify MySQL is running
# Check credentials in .env
# Initialize database
python cli.py init-db
```

### API returns 404
```bash
# Check backend is running
# Check endpoint is correct
# Verify config.js is loaded
# Check browser Network tab (F12)
```

## 📖 Additional Documentation

- **[INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)** - Full integration guide
- **[CONNECTION_SETUP.md](Agri/frontend/backend/CONNECTION_SETUP.md)** - Technical details
- **[ARCHITECTURE.md](Agri/ARCHITECTURE.md)** - System architecture
- **[DEVELOPER_CHECKLIST.md](DEVELOPER_CHECKLIST.md)** - Checklists & guidelines

## 🎯 Next Steps

1. ✅ Read [INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md)
2. ✅ Run `python cli.py run` to start backend
3. ✅ Open `http://localhost:5000` in browser
4. ✅ Test login/register flow
5. ✅ Start developing!

## 📝 Feature Flags

Feature flags allow toggling features without code changes:

```bash
# Get all feature flags
curl http://localhost:5000/api/feature-flags

# Toggle a feature flag
curl -X POST http://localhost:5000/api/feature-flags/weather_api/enable
```

## 🔗 API Integration

### Frontend to Backend Flow

```
Browser Request
    ↓
Frontend (HTML/JS) sends to http://localhost:5000/api/*
    ↓
Flask backend receives & processes
    ↓
Query MySQL database if needed
    ↓
Return JSON response
    ↓
Frontend updates page
```

## 📞 Support

- Check documentation files
- Review browser console (F12)
- Check Network tab in DevTools
- Review backend logs (`FLASK_DEBUG=1`)
- Read error messages carefully

## 🚀 Deployment

See [CONNECTION_SETUP.md](Agri/frontend/backend/CONNECTION_SETUP.md) for production deployment instructions.

## 📄 Feature Flags

```bash
GET /api/feature-flags
```

**Check specific flag:**
```bash
GET /api/feature-flags/weather_api
```

**Toggle a flag:**
```bash
POST /api/feature-flags/weather_api/toggle
```

**Create new flag:**
```bash
POST /api/feature-flags
Content-Type: application/json

{
  "name": "new_feature",
  "enabled": false,
  "description": "Description of the feature"
}
```

## API Endpoints

### Users
- `GET /api/users` - List all users
- `GET /api/users/:id` - Get user details
- `POST /api/users` - Create new user
- `PUT /api/users/:id` - Update user

**Example - Create User:**
```json
POST /api/users
{
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "phone": "+91-9876543210",
  "location": "Guntur, AP",
  "farm_size": 5.5
}
```

### Crops
- `GET /api/crops` - List all crops
- `GET /api/crops?user_id=1` - Get crops for specific user
- `GET /api/crops/:id` - Get crop details
- `POST /api/crops` - Create crop record
- `PUT /api/crops/:id` - Update crop

**Example - Create Crop:**
```json
POST /api/crops
{
  "user_id": 1,
  "crop_name": "Rice",
  "variety": "IR64",
  "planting_date": "2026-01-15",
  "expected_harvest": "2026-05-15",
  "area": 2.5,
  "status": "growing"
}
```

### Weather
- `GET /api/weather?location=Guntur` - Get weather data
- `POST /api/weather` - Add weather data

**Example - Add Weather Data:**
```json
POST /api/weather
{
  "location": "Guntur, AP",
  "temperature": 32.5,
  "humidity": 65,
  "rainfall": 0,
  "wind_speed": 12.5,
  "weather_condition": "Partly Cloudy"
}
```

### Market Prices
- `GET /api/market-prices?crop_name=Rice` - Get prices
- `GET /api/market-prices?crop_name=Rice&location=Guntur` - Filter by location
- `POST /api/market-prices` - Add price data

**Example - Add Market Price:**
```json
POST /api/market-prices
{
  "crop_name": "Rice",
  "location": "Guntur",
  "price": 1850.00,
  "market_name": "Guntur Agricultural Market"
}
```

### Recommendations
- `POST /api/recommendations/crops` - Get crop recommendations

**Example:**
```json
POST /api/recommendations/crops
{
  "location": "Guntur, AP",
  "soil_type": "loamy"
}
```

## Database Schema

### Users Table
- id, name, email, phone, location, farm_size, created_at

### Crops Table
- id, user_id, crop_name, variety, planting_date, expected_harvest, area, status, created_at

### Weather Data Table
- id, location, temperature, humidity, rainfall, wind_speed, weather_condition, recorded_at

### Market Prices Table
- id, crop_name, location, price, market_name, recorded_at

### Feature Flags Table
- id, name, enabled, description, created_at, updated_at

## Using with Frontend

Make sure your frontend points to the backend URL:

```javascript
const API_URL = 'http://localhost:5000/api';

// Example: Fetch crops
fetch(`${API_URL}/crops?user_id=1`)
  .then(res => res.json())
  .then(data => console.log(data));

// Example: Check feature flag before showing UI
fetch(`${API_URL}/feature-flags/weather_api`)
  .then(res => res.json())
  .then(flag => {
    if (flag.enabled) {
      // Show weather widget
    }
  });
```

## Production Deployment

1. **Use PostgreSQL:**
```bash
DATABASE_URL=postgresql://user:pass@localhost/agri_mithra
```

2. **Set SECRET_KEY:**
```bash
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
```

3. **Use Production Server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Feature Flag Best Practices

1. **Gradual Rollouts** - Enable features for testing before full deployment
2. **A/B Testing** - Toggle features for different user groups
3. **Emergency Switches** - Quickly disable problematic features
4. **Dark Launches** - Deploy code with features disabled, enable when ready

## Support

For issues or questions, check the code comments or raise an issue.
