from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import re

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.'),
        Length(min=3, max=80, message='Username must be between 3 and 80 characters.')
    ])
    
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Email(message='Please enter a valid email address.')
    ])
    
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.'),
        Length(min=8, message='Password must be at least 8 characters long.')
    ])
    
    password_confirm = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm your password.'),
        EqualTo('password', message='Passwords must match.')
    ])
    
    submit = SubmitField('Register')
    
    def validate_username(self, field):
        """Validate username contains only alphanumeric characters and underscores"""
        if not re.match(r'^[a-zA-Z0-9_]+$', field.data):
            raise ValidationError('Username can only contain letters, numbers, and underscores.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.')
    ])
    
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.')
    ])
    
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
