from app import app
from app.forms.login import LoginForm
from flask import render_template, flash, redirect, url_for

counter = 0

@app.route('/')
@app.route('/index')
def index():
    #return 'Hello, world'
    user = {'name': 'Max'}
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
        flash('Login requested: Name - {}, remember me - {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', tilte='Sign in', form=form)

