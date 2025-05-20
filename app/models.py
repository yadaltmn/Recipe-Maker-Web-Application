from app import db
from datetime import datetime
from flask_login import UserMixin

# Association table for favorites
favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(128), nullable=False)
    favorite_recipes = db.relationship('Recipe', secondary=favorites, backref='favorited_by')
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    body = db.Column(db.String(256))
    # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # def __repr__(self):
    #  return '<Posts {}>'.format(self.body)

# class Age(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     age = db.Column(db.String(32))

# Define the Recipe model/table for storing recipes
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for each recipe
    title = db.Column(db.String(100), nullable=False)  # Recipe title
    description = db.Column(db.String(255), nullable=False)  # Short description of the recipe
    ingredients = db.Column(db.Text, nullable=False)  # Ingredients required
    instructions = db.Column(db.Text, nullable=False)  # Instructions to prepare the recipe
    username = db.Column(db.String(32))  # Username of the creator (optional)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False)
