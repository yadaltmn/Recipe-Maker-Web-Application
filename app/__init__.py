from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import os
from flask_migrate import Migrate
from flask_socketio import SocketIO

myapp_obj = Flask(__name__, static_folder='../static')
basedir = os.path.abspath(os.path.dirname(__file__))

# Config setup
myapp_obj.config.from_mapping(
    SECRET_KEY='you-will-never-guess',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
)

# Initialize extensions
db = SQLAlchemy(myapp_obj)
csrf = CSRFProtect(myapp_obj)
migrate = Migrate(myapp_obj, db)
socketio = SocketIO(myapp_obj, cors_allowed_origins="*")  # Initialize SocketIO first
login_manager = LoginManager()

# Configure login manager
login_manager.init_app(myapp_obj)
login_manager.login_view = 'login'

# Import models AFTER extensions but BEFORE routes
from app.models import User

# User loader must come after User model import
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes
