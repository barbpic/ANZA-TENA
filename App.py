from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///refuge_connect.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class EmergencyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # e.g., food, water, clothing
    quantity = db.Column(db.Integer, nullable=False)

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class HealthcareService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    appointment_required = db.Column(db.Boolean, default=False)

class LegalAid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to render the home page
@app.route('/')
def home():
    return render_template('home.html')

# User registration
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    user_name = data['name']
    user_role = data['role']

    new_user = User(name=user_name, role=user_role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'role': user.role} for user in users])

# Emergency response coordination
@app.route('/api/emergency', methods=['POST'])
def create_emergency():
    data = request.json
    title = data['title']
    description = data['description']
    location = data['location']
    contact_info = data['contact_info']
    
    emergency = EmergencyResponse(title=title, description=description, location=location, contact_info=contact_info)
    db.session.add(emergency)
    db.session.commit()
    
    return jsonify({'message': 'Emergency created successfully!'}), 201

@app.route('/api/emergencies', methods=['GET'])
def get_emergencies():
    emergencies = EmergencyResponse.query.all()
    return jsonify([{'id': e.id, 'title': e.title, 'description': e.description} for e in emergencies])

# Resource distribution
@app.route('/api/resources', methods=['POST'])
def add_resource():
    data = request.json
    resource_type = data['type']
    quantity = data['quantity']
    
    resource = Resource(type=resource_type, quantity=quantity)
    db.session.add(resource)
    db.session.commit()
    
    return jsonify({'message': 'Resource added successfully!'}), 201

@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{'id': r.id, 'type': r.type, 'quantity': r.quantity} for r in resources])

# Volunteer management
@app.route('/api/volunteers', methods=['POST'])
def add_volunteer():
    data = request.json
    name = data['name']
    role = data['role']
    
    volunteer = Volunteer(name=name, role=role)
    db.session.add(volunteer)
    db.session.commit()
    
    return jsonify({'message': 'Volunteer added successfully!'}), 201

@app.route('/api/volunteers', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([{'id': v.id, 'name': v.name, 'role': v.role} for v in volunteers])

# Healthcare services
@app.route('/api/healthcare', methods=['POST'])
def add_healthcare_service():
    data = request.json
    service_name = data['service_name']
    appointment_required = data.get('appointment_required', False)

    healthcare = HealthcareService(service_name=service_name, appointment_required=appointment_required)
    db.session.add(healthcare)
    db.session.commit()

    return jsonify({'message': 'Healthcare service added successfully!'}), 201

@app.route('/api/healthcare', methods=['GET'])
def get_healthcare_services():
    services = HealthcareService.query.all()
    return jsonify([{'id': s.id, 'service_name': s.service_name, 'appointment_required': s.appointment_required} for s in services])

# Legal Aid services
@app.route('/api/legal-aid', methods=['POST'])
def add_legal_aid():
    data = request.json
    service_name = data['service_name']
    description = data['description']

    legal_aid = LegalAid(service_name=service_name, description=description)
    db.session.add(legal_aid)
    db.session.commit()

    return jsonify({'message': 'Legal aid service added successfully!'}), 201

@app.route('/api/legal-aid', methods=['GET'])
def get_legal_aids():
    legal_aids = LegalAid.query.all()
    return jsonify([{'id': a.id, 'service_name': a.service_name, 'description': a.description} for a in legal_aids])

if __name__ == '__main__':
    app.run(debug=True)
