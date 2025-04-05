from flask import Blueprint, request, jsonify
from .models import User
from . import db, bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json

    full_name = data.get('full_name')
    college_email = data.get('college_email')
    password = data.get('password')
    university = data.get('university')
    department = data.get('department')
    year = data.get('year')
    phone = data.get('phone')

    # Check if user exists
    existing_user = User.query.filter_by(college_email=college_email).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 409

    # Hash password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(
        full_name=full_name,
        college_email=college_email,
        password=hashed_password,
        university=university,
        department=department,
        year=year,
        phone=phone
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Signup successful'}), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.json

    college_email = data.get('college_email')
    password = data.get('password')

    user = User.query.filter_by(college_email=college_email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if bcrypt.check_password_hash(user.password, password):
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'full_name': user.full_name,
                'college_email': user.college_email,
                'university': user.university
            }
        }), 200
    else:
        return jsonify({'message': 'Incorrect password'}), 401

