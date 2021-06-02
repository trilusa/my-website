from blog import app
from flask import render_template, flash, redirect, url_for, request
from blog.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from blog.models import User
from werkzeug.urls import url_parse

posts = [
        {
            'meta': {'title': 'Analogy Time'},
            'content': 'Analogies are cool!'
        },
        {
            'meta': {'title': 'Category Time'},
            'content': 'Categories are cool!'
        },
        {
            'meta': {'title': 'Concept Time'},
            'content': 'Concepts are cool!'
        }
        ]

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))