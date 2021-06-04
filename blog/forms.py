from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from blog.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EditPostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[Length(min=0, max=100000)])
    submit = SubmitField('Publish')


