from app import app, db
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.login import LoginForm
from app.forms.registration import RegistrationForm
from app.models import User
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
    name = 'Guest'
    if current_user.is_authenticated:
        name = current_user.username

    user = {'name': name}
    posts = [
        {
            'title': 'Article1',
            'body': 'Hello, world'
        },
        {
            'title': 'Article2',
            'body': 'We run a new site'
        },
                {
            'title': 'Article3',
            'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
        },
        {
            'title': 'Article4',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        }
    ]
    return render_template('index.html', title='Home page', user=user, posts=posts)

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


