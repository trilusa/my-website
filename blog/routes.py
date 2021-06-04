from blog import app, db
from flask import render_template, flash, redirect, url_for, request
from blog.forms import LoginForm, EditPostForm
from flask_login import current_user, login_user, logout_user, login_required
from blog.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime



@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
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


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_post/<post_title>', methods=['GET', 'POST'])
@login_required
def edit_post(post_title):
    form = EditPostForm()
    post = Post.query.filter_by(post_title=post_title).first()
    form.post_title.data = post.post_title
    form.body.data = post.body
    
        

    if form.validate_on_submit():
        post.post_title = form.post_title.data
        post.body = form.body.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('home'))

    return render_template('edit_post.html', title='Edit Post', form=form)


@app.route('/blog/<post_title>')
def post(post_title):
    post = Post.query.filter_by(post_title=post_title).first_or_404()
   
    return render_template('post.html', post=post)

