#!/usr/bin/env python3
"""
Quick setup and test script for Agri-Mithra Backend
Run this after installing requirements to set up your database with sample data
"""

from app import app, db, User, Crop, WeatherData, MarketPrice, FeatureFlag
from datetime import datetime, timedelta
import json

def setup_database():
    """Initialize database with sample data"""
    print("🌱 Setting up Agri-Mithra Database...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created")
        
        # Check if data already exists
        if User.query.first():
            print("⚠️  Database already has data. Skipping sample data creation.")
            return
        
        # Create sample users
        users = [
            User(
                name="Ravi Kumar",
                email="ravi@example.com",
                phone="+91-9876543210",
                location="Guntur, Andhra Pradesh",
                farm_size=5.5
            ),
            User(
                name="Lakshmi Devi",
                email="lakshmi@example.com",
                phone="+91-9876543211",
                location="Vijayawada, Andhra Pradesh",
                farm_size=3.2
            ),
            User(
                name="Suresh Reddy",
                email="suresh@example.com",
                phone="+91-9876543212",
                location="Kurnool, Andhra Pradesh",
                farm_size=8.0
            )
        ]
        
        for user in users:
            db.session.add(user)
        db.session.commit()
        print(f"✅ Created {len(users)} sample users")
        
        # Create sample crops
        crops = [
            Crop(
                user_id=1,
                crop_name="Rice",
                variety="IR64",
                planting_date=datetime.now() - timedelta(days=30),
                expected_harvest=datetime.now() + timedelta(days=90),
                area=2.5,
                status="growing"
            ),
            Crop(
                user_id=1,
                crop_name="Cotton",
                variety="Bt Cotton",
                planting_date=datetime.now() - timedelta(days=45),
                expected_harvest=datetime.now() + timedelta(days=105),
                area=3.0,
                status="growing"
            ),
            Crop(
                user_id=2,
                crop_name="Maize",
                variety="Hybrid",
                planting_date=datetime.now() - timedelta(days=20),
                expected_harvest=datetime.now() + timedelta(days=70),
                area=2.0,
                status="growing"
            ),
            Crop(
                user_id=3,
                crop_name="Groundnut",
                variety="TMV-2",
                planting_date=datetime.now() - timedelta(days=60),
                expected_harvest=datetime.now() + timedelta(days=30),
                area=4.0,
                status="growing"
            )
        ]
        
        for crop in crops:
            db.session.add(crop)
        db.session.commit()
        print(f"✅ Created {len(crops)} sample crops")
        
        # Create sample weather data
        weather_data = [
            WeatherData(
                location="Guntur, Andhra Pradesh",
                temperature=32.5,
                humidity=65,
                rainfall=0,
                wind_speed=12.5,
                weather_condition="Partly Cloudy"
            ),
            WeatherData(
                location="Vijayawada, Andhra Pradesh",
                temperature=34.0,
                humidity=70,
                rainfall=2.5,
                wind_speed=10.0,
                weather_condition="Light Rain"
            ),
            WeatherData(
                location="Kurnool, Andhra Pradesh",
                temperature=31.0,
                humidity=60,
                rainfall=0,
                wind_speed=15.0,
                weather_condition="Clear Sky"
            )
        ]
        
        for weather in weather_data:
            db.session.add(weather)
        db.session.commit()
        print(f"✅ Created {len(weather_data)} weather records")
        
        # Create sample market prices
        market_prices = [
            MarketPrice(
                crop_name="Rice",
                location="Guntur",
                price=1850.00,
                market_name="Guntur Agricultural Market"
            ),
            MarketPrice(
                crop_name="Cotton",
                location="Guntur",
                price=6200.00,
                market_name="Guntur Cotton Market"
            ),
            MarketPrice(
                crop_name="Maize",
                location="Vijayawada",
                price=1650.00,
                market_name="Vijayawada Grain Market"
            ),
            MarketPrice(
                crop_name="Groundnut",
                location="Kurnool",
                price=5800.00,
                market_name="Kurnool Agricultural Market"
            ),
            MarketPrice(
                crop_name="Rice",
                location="Vijayawada",
                price=1875.00,
                market_name="Vijayawada Agricultural Market"
            )
        ]
        
        for price in market_prices:
            db.session.add(price)
        db.session.commit()
        print(f"✅ Created {len(market_prices)} market price records")
        
        print("\n🎉 Database setup complete!")
        print("\n📊 Summary:")
        print(f"   Users: {User.query.count()}")
        print(f"   Crops: {Crop.query.count()}")
        print(f"   Weather Records: {WeatherData.query.count()}")
        print(f"   Market Prices: {MarketPrice.query.count()}")
        print(f"   Feature Flags: {FeatureFlag.query.count()}")


def test_api():
    """Test API endpoints"""
    print("\n🧪 Testing API Endpoints...")
    
    with app.test_client() as client:
        # Test health check
        response = client.get('/api/health')
        print(f"\n✓ Health Check: {response.status_code}")
        
        # Test feature flags
        response = client.get('/api/feature-flags')
        print(f"✓ Feature Flags: {response.status_code} - {len(response.json)} flags")
        
        # Test users
        response = client.get('/api/users')
        print(f"✓ Get Users: {response.status_code} - {len(response.json)} users")
        
        # Test crops
        response = client.get('/api/crops')
        print(f"✓ Get Crops: {response.status_code} - {len(response.json)} crops")
        
        # Test weather
        response = client.get('/api/weather?location=Guntur, Andhra Pradesh')
        print(f"✓ Get Weather: {response.status_code}")
        
        # Test market prices
        response = client.get('/api/market-prices?crop_name=Rice')
        print(f"✓ Get Market Prices: {response.status_code} - {len(response.json)} prices")
        
        # Test feature flag toggle
        response = client.post('/api/feature-flags/pest_detection/toggle')
        print(f"✓ Toggle Feature Flag: {response.status_code}")
        
        print("\n✅ All API tests passed!")


def show_feature_flags():
    """Display current feature flag status"""
    print("\n🚩 Feature Flags Status:")
    print("-" * 60)
    
    with app.app_context():
        flags = FeatureFlag.query.all()
        for flag in flags:
            status = "🟢 ENABLED" if flag.enabled else "🔴 DISABLED"
            print(f"{status:15} | {flag.name:25} | {flag.description}")
    
    print("-" * 60)


if __name__ == "__main__":
    print("=" * 60)
    print("🌾 Agri-Mithra Backend Setup")
    print("=" * 60)
    
    # Setup database
    setup_database()
    
    # Show feature flags
    show_feature_flags()
    
    # Test API
    test_api()
    
    print("\n" + "=" * 60)
    print("✨ Setup Complete! You can now run:")
    print("   python app.py")
    print("=" * 60)
