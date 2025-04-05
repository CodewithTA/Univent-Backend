from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    college_email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=True)
    year = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
