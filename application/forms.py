from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    content = StringField('Content',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post!')

class RegisterForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    password = StringField('Password',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    confirm_password = StringField('Confirm Password',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit = SubmitField('Register')
