from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.login import LoginForm
from app.forms.edit_profile import EditProfileForm
from app.forms.registration import RegistrationForm
from app.forms.article import ArticleForm
from app.models import User, Article
from datetime import datetime

counter = 0

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
def index():
    #print(current_user)
    #return 'Hello, world'
    
    if current_user.is_authenticated:
        name = current_user.username
        posts = current_user.followed_posts()
    else:
        name = 'Guest'
        posts = Article.query.order_by(Article.created_at.desc()).all()
    
    return render_template('index.html', title='Home page', user={'name':name}, posts=posts)

@login_required
@app.route('/info')
def info():
    global counter
    counter += 1
    #return 'Hello, times: {}'.format(counter)
    return render_template('info.html', tille='Info page', counter=counter)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested: Name - {}, remember me - {}'.format(form.username.data, form.remember_me.data))
        #return redirect(url_for('index'))
        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username of password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', tilte='Sign in', form=form)

@app.route('/logout')
def loglout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('user registered')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Registration', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'test_1'},
        {'author': user, 'body': 'test_2'},
    ]

    return render_template('user.html', title='user info', user=user, posts=posts)

@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Chenges saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@app.route('/create_article',methods=['GET','POST'])
@login_required
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, body=form.post.data, author=current_user)
        db.session.add(article)
        db.session.commit()
        flash('your post added')
        return redirect(url_for('index'))
    
    return render_template('create_article.html', title='Create article', form=form)

