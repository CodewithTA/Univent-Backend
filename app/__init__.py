from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app, origins="*", supports_credentials=True)  # Allows requests from frontend

    # Register blueprints
    from .auth_routes import auth
    from .routes import main
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(main)

    return app