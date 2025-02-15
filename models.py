from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., refugee, volunteer, healthcare

# Emergency Response
class EmergencyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

# Resource model for resource distribution
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # e.g., food, water, clothing
    quantity = db.Column(db.Integer, nullable=False)

# Volunteer Support
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., educator, shelter support
    available = db.Column(db.Boolean, default=True)

# Healthcare model
class HealthcareService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    appointment_required = db.Column(db.Boolean, default=False)

# Legal Aid model
class LegalAid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
