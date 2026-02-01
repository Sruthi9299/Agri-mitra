from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///agri_mithra.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

db = SQLAlchemy(app)

# ==================== FEATURE FLAGS ====================
class FeatureFlag(db.Model):
    __tablename__ = 'feature_flags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    enabled = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'enabled': self.enabled,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


# Feature Flag Helper Functions
def is_feature_enabled(feature_name):
    """Check if a feature flag is enabled"""
    flag = FeatureFlag.query.filter_by(name=feature_name).first()
    return flag.enabled if flag else False


def initialize_default_flags():
    """Initialize default feature flags"""
    default_flags = [
        {'name': 'weather_api', 'description': 'Enable weather API integration', 'enabled': True},
        {'name': 'crop_recommendations', 'description': 'Enable AI crop recommendations', 'enabled': True},
        {'name': 'market_prices', 'description': 'Enable market price tracking', 'enabled': True},
        {'name': 'soil_analysis', 'description': 'Enable soil analysis feature', 'enabled': False},
        {'name': 'pest_detection', 'description': 'Enable pest detection AI', 'enabled': False},
        {'name': 'irrigation_scheduler', 'description': 'Enable irrigation scheduling', 'enabled': True},
        {'name': 'community_forum', 'description': 'Enable farmer community forum', 'enabled': False},
        {'name': 'government_schemes', 'description': 'Enable government schemes info', 'enabled': True},
    ]
    
    for flag_data in default_flags:
        existing_flag = FeatureFlag.query.filter_by(name=flag_data['name']).first()
        if not existing_flag:
            flag = FeatureFlag(**flag_data)
            db.session.add(flag)
    
    db.session.commit()


# ==================== MODELS ====================
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    location = db.Column(db.String(200))
    farm_size = db.Column(db.Float)  # in acres
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    crops = db.relationship('Crop', backref='farmer', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'location': self.location,
            'farm_size': self.farm_size,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Crop(db.Model):
    __tablename__ = 'crops'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    crop_name = db.Column(db.String(100), nullable=False)
    variety = db.Column(db.String(100))
    planting_date = db.Column(db.Date)
    expected_harvest = db.Column(db.Date)
    area = db.Column(db.Float)  # in acres
    status = db.Column(db.String(50), default='growing')  # growing, harvested, failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'crop_name': self.crop_name,
            'variety': self.variety,
            'planting_date': self.planting_date.isoformat() if self.planting_date else None,
            'expected_harvest': self.expected_harvest.isoformat() if self.expected_harvest else None,
            'area': self.area,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class WeatherData(db.Model):
    __tablename__ = 'weather_data'
    
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    weather_condition = db.Column(db.String(100))
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'rainfall': self.rainfall,
            'wind_speed': self.wind_speed,
            'weather_condition': self.weather_condition,
            'recorded_at': self.recorded_at.isoformat() if self.recorded_at else None
        }


class MarketPrice(db.Model):
    __tablename__ = 'market_prices'
    
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)  # price per quintal
    market_name = db.Column(db.String(200))
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'crop_name': self.crop_name,
            'location': self.location,
            'price': self.price,
            'market_name': self.market_name,
            'recorded_at': self.recorded_at.isoformat() if self.recorded_at else None
        }


# ==================== FEATURE FLAG ROUTES ====================
@app.route('/api/feature-flags', methods=['GET'])
def get_feature_flags():
    """Get all feature flags"""
    flags = FeatureFlag.query.all()
    return jsonify([flag.to_dict() for flag in flags]), 200


@app.route('/api/feature-flags/<flag_name>', methods=['GET'])
def get_feature_flag(flag_name):
    """Get specific feature flag status"""
    flag = FeatureFlag.query.filter_by(name=flag_name).first()
    if flag:
        return jsonify(flag.to_dict()), 200
    return jsonify({'error': 'Feature flag not found'}), 404


@app.route('/api/feature-flags/<flag_name>/toggle', methods=['POST'])
def toggle_feature_flag(flag_name):
    """Toggle a feature flag on/off"""
    flag = FeatureFlag.query.filter_by(name=flag_name).first()
    if not flag:
        return jsonify({'error': 'Feature flag not found'}), 404
    
    flag.enabled = not flag.enabled
    flag.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify(flag.to_dict()), 200


@app.route('/api/feature-flags', methods=['POST'])
def create_feature_flag():
    """Create a new feature flag"""
    data = request.json
    
    if not data.get('name'):
        return jsonify({'error': 'Feature flag name is required'}), 400
    
    existing_flag = FeatureFlag.query.filter_by(name=data['name']).first()
    if existing_flag:
        return jsonify({'error': 'Feature flag already exists'}), 400
    
    flag = FeatureFlag(
        name=data['name'],
        enabled=data.get('enabled', False),
        description=data.get('description', '')
    )
    
    db.session.add(flag)
    db.session.commit()
    
    return jsonify(flag.to_dict()), 201


# ==================== USER ROUTES ====================
@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get specific user"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and email are required'}), 400
    
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'error': 'Email already registered'}), 400
    
    user = User(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone'),
        location=data.get('location'),
        farm_size=data.get('farm_size')
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user.to_dict()), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user details"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    
    if data.get('name'):
        user.name = data['name']
    if data.get('phone'):
        user.phone = data['phone']
    if data.get('location'):
        user.location = data['location']
    if data.get('farm_size') is not None:
        user.farm_size = data['farm_size']
    
    db.session.commit()
    
    return jsonify(user.to_dict()), 200


# ==================== CROP ROUTES ====================
@app.route('/api/crops', methods=['GET'])
def get_crops():
    """Get all crops or filter by user_id"""
    user_id = request.args.get('user_id', type=int)
    
    if user_id:
        crops = Crop.query.filter_by(user_id=user_id).all()
    else:
        crops = Crop.query.all()
    
    return jsonify([crop.to_dict() for crop in crops]), 200


@app.route('/api/crops/<int:crop_id>', methods=['GET'])
def get_crop(crop_id):
    """Get specific crop"""
    crop = Crop.query.get(crop_id)
    if not crop:
        return jsonify({'error': 'Crop not found'}), 404
    return jsonify(crop.to_dict()), 200


@app.route('/api/crops', methods=['POST'])
def create_crop():
    """Create a new crop record"""
    if not is_feature_enabled('crop_recommendations'):
        return jsonify({'error': 'Crop management feature is disabled'}), 403
    
    data = request.json
    
    if not data.get('user_id') or not data.get('crop_name'):
        return jsonify({'error': 'User ID and crop name are required'}), 400
    
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    crop = Crop(
        user_id=data['user_id'],
        crop_name=data['crop_name'],
        variety=data.get('variety'),
        planting_date=datetime.fromisoformat(data['planting_date']) if data.get('planting_date') else None,
        expected_harvest=datetime.fromisoformat(data['expected_harvest']) if data.get('expected_harvest') else None,
        area=data.get('area'),
        status=data.get('status', 'growing')
    )
    
    db.session.add(crop)
    db.session.commit()
    
    return jsonify(crop.to_dict()), 201


@app.route('/api/crops/<int:crop_id>', methods=['PUT'])
def update_crop(crop_id):
    """Update crop details"""
    crop = Crop.query.get(crop_id)
    if not crop:
        return jsonify({'error': 'Crop not found'}), 404
    
    data = request.json
    
    if data.get('crop_name'):
        crop.crop_name = data['crop_name']
    if data.get('variety'):
        crop.variety = data['variety']
    if data.get('status'):
        crop.status = data['status']
    if data.get('area') is not None:
        crop.area = data['area']
    
    db.session.commit()
    
    return jsonify(crop.to_dict()), 200


# ==================== WEATHER ROUTES ====================
@app.route('/api/weather', methods=['GET'])
def get_weather():
    """Get weather data"""
    if not is_feature_enabled('weather_api'):
        return jsonify({'error': 'Weather feature is disabled'}), 403
    
    location = request.args.get('location')
    
    if location:
        weather = WeatherData.query.filter_by(location=location).order_by(WeatherData.recorded_at.desc()).first()
        if weather:
            return jsonify(weather.to_dict()), 200
        return jsonify({'error': 'No weather data found for this location'}), 404
    
    recent_weather = WeatherData.query.order_by(WeatherData.recorded_at.desc()).limit(10).all()
    return jsonify([w.to_dict() for w in recent_weather]), 200


@app.route('/api/weather', methods=['POST'])
def add_weather_data():
    """Add weather data"""
    if not is_feature_enabled('weather_api'):
        return jsonify({'error': 'Weather feature is disabled'}), 403
    
    data = request.json
    
    if not data.get('location'):
        return jsonify({'error': 'Location is required'}), 400
    
    weather = WeatherData(
        location=data['location'],
        temperature=data.get('temperature'),
        humidity=data.get('humidity'),
        rainfall=data.get('rainfall'),
        wind_speed=data.get('wind_speed'),
        weather_condition=data.get('weather_condition')
    )
    
    db.session.add(weather)
    db.session.commit()
    
    return jsonify(weather.to_dict()), 201


# ==================== MARKET PRICE ROUTES ====================
@app.route('/api/market-prices', methods=['GET'])
def get_market_prices():
    """Get market prices"""
    if not is_feature_enabled('market_prices'):
        return jsonify({'error': 'Market prices feature is disabled'}), 403
    
    crop_name = request.args.get('crop_name')
    location = request.args.get('location')
    
    query = MarketPrice.query
    
    if crop_name:
        query = query.filter_by(crop_name=crop_name)
    if location:
        query = query.filter_by(location=location)
    
    prices = query.order_by(MarketPrice.recorded_at.desc()).limit(20).all()
    return jsonify([p.to_dict() for p in prices]), 200


@app.route('/api/market-prices', methods=['POST'])
def add_market_price():
    """Add market price data"""
    if not is_feature_enabled('market_prices'):
        return jsonify({'error': 'Market prices feature is disabled'}), 403
    
    data = request.json
    
    if not data.get('crop_name') or not data.get('location') or data.get('price') is None:
        return jsonify({'error': 'Crop name, location, and price are required'}), 400
    
    price = MarketPrice(
        crop_name=data['crop_name'],
        location=data['location'],
        price=data['price'],
        market_name=data.get('market_name')
    )
    
    db.session.add(price)
    db.session.commit()
    
    return jsonify(price.to_dict()), 201


# ==================== RECOMMENDATIONS (Feature Flag Protected) ====================
@app.route('/api/recommendations/crops', methods=['POST'])
def get_crop_recommendations():
    """Get AI-based crop recommendations"""
    if not is_feature_enabled('crop_recommendations'):
        return jsonify({'error': 'Crop recommendations feature is disabled'}), 403
    
    data = request.json
    location = data.get('location')
    soil_type = data.get('soil_type', 'loamy')
    
    # Sample recommendations (integrate with actual AI model)
    recommendations = [
        {
            'crop': 'Rice',
            'suitability': 'High',
            'expected_yield': '25-30 quintals/acre',
            'season': 'Kharif',
            'reason': 'Suitable soil type and weather conditions'
        },
        {
            'crop': 'Wheat',
            'suitability': 'Medium',
            'expected_yield': '18-22 quintals/acre',
            'season': 'Rabi',
            'reason': 'Good for this region in winter season'
        }
    ]
    
    return jsonify({'recommendations': recommendations}), 200


# ==================== HEALTH CHECK ====================
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'database': 'connected'
    }), 200


@app.route('/', methods=['GET'])
def home():
    """Root endpoint"""
    return jsonify({
        'message': 'Agri-Mithra API',
        'version': '1.0.0',
        'endpoints': {
            'feature_flags': '/api/feature-flags',
            'users': '/api/users',
            'crops': '/api/crops',
            'weather': '/api/weather',
            'market_prices': '/api/market-prices',
            'recommendations': '/api/recommendations/crops'
        }
    }), 200


# ==================== DATABASE INITIALIZATION ====================
with app.app_context():
    db.create_all()
    initialize_default_flags()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
