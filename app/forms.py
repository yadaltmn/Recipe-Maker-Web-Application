from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=128)])
    submit =  SubmitField("Sign in")
    remember_me = BooleanField("Remember Me")    

class PostForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    body = StringField('Body of Post', validators=[validators.Length(min=4, max=35)])
    submit =  SubmitField("Post")

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=128)])
    submit =  SubmitField("Create account")

# Form for creating a new recipe
class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()])  # Input for recipe title
    description = StringField('Description', validators=[validators.DataRequired()])  # Short description
    ingredients = StringField('Ingredients', validators=[validators.DataRequired()])  # List of ingredients
    instructions = StringField('Instructions', validators=[validators.DataRequired()])  # Steps to prepare
    submit = SubmitField("Create Recipe")  # Button to submit the form

