from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostEditor(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    body = CKEditorField('Body')
    description = TextAreaField('Description')
    post_url = StringField('Perma-link', validators=[DataRequired()])
    submit = SubmitField('Publish')
    delete = SubmitField('Delete')
    featured = BooleanField('Featured?')