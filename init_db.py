from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    print("🔍 DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])  # Debug print
    db.create_all()
    print("✅ Database tables created successfully!")
