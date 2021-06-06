from blog import app, db
from flask import render_template, flash, redirect, url_for, request
from blog.forms import LoginForm, PostEditor
from flask_login import current_user, login_user, logout_user, login_required
from blog.models import User, Post
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', title='Home', posts=reversed(posts))


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

@app.route("/blog/<post_url>")
def post(post_url):
    post = Post.query.filter_by(post_url=post_url).first_or_404()
    return render_template('post.html', title='Blog Post', post=post)

@app.route('/edit/<post_url>',  methods=['GET', 'POST'])
@login_required
def edit(post_url):
    editor = PostEditor()

    if post_url != 'new':
        p = Post.query.filter_by(post_url=post_url).first_or_404()
    else:
        p = Post()
        
    if editor.validate_on_submit():
        if editor.delete.data:
            if post_url == 'new':
                return redirect(url_for('home'))
            else:
                db.session.delete(p)
        else:
            p.post_title = editor.post_title.data
            p.description = editor.description.data
            p.body = editor.body.data
            p.post_url = editor.post_url.data
            db.session.add(p)
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        editor.post_title.data = p.post_title
        editor.description.data = p.description
        editor.body.data = p.body
        editor.post_url.data = p.post_url
    return render_template('edit.html', title="Post Editor", post=p, editor=editor)

@app.route('/new')
@app.route('/editor')
@app.route('/edit')
def new_post():
    return redirect(url_for('edit', post_url='new'))