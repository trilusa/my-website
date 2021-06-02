from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EditPostForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    post_content = TextAreaField('Post Content', validators=[DataRequired()])
    submit = SubmitField('Publish')
