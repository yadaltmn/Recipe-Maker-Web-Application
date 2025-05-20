from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
import os
from flask_migrate import Migrate

# Create app
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

login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = 'login'

# Import AFTER defining login_manager
from app.models import User

# This is REQUIRED for Flask-Login to work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# This should come LAST
from app import routes, models

__all__ = [
    routes,
    models,
    myapp_obj
]