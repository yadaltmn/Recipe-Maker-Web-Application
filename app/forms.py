from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')  # matches form.remember_me
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    body = StringField('Body of Post', validators=[Length(min=4, max=35)])
    submit = SubmitField("Post")

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=4, max=35)])
    submit = SubmitField("Create account")

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    instructions = StringField('Instructions', validators=[DataRequired()])
    submit = SubmitField("Create Recipe")

class CommentForm(FlaskForm):
    content = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    #email = StringField('Email', validators=[Optional(), Email()])
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=255)]) 
    password = PasswordField('New Password', validators=[Optional(), Length(min=6)])
    submit = SubmitField('Update Profile')