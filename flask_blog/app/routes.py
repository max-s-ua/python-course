from app import app, db
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, logout_user, current_user, login_required

from app.forms.login import LoginForm
from app.forms.edit_profile import EditProfileForm
from app.forms.registration import RegistrationForm
from app.forms.article import ArticleForm
from app.models import User, Article
from datetime import datetime

from math import ceil

@app.route('/post_page/<page>')
@login_required
def post_page(page):
    page_num = int(page)
    posts_count = int(Article.query.count())
    posts_per_page = 10
    total_pages = ceil(posts_count / posts_per_page)
    if page_num not in range(1, total_pages + 1):
        abort(404)

    if page_num*10 < posts_count:
        begin = (page_num - 1) * posts_per_page
        end = begin + posts_per_page - 1
    else:
        begin = (page_num - 1) * posts_per_page
        end = posts_count - 1

    posts = Article.query.order_by(Article.created_at.desc()).all()

    #return 'page {}, total posts: {}'.format(p, posts_count)

    if current_user.is_authenticated:
        name = current_user.username
    else:
        name = 'Guest'

    return render_template('posts.html', title='Posts, page {}'.format(page_num),
     user={'name':name}, posts=posts[begin:(end+1)], page_num=page_num, total_pages=total_pages)


@app.route('/post_page/like')
@login_required
def like():
    post_id = request.args.get('post_id')
    user = current_user
    
    post = Article.query.filter_by(id=post_id).first_or_404()
    if user not in post.likes:
        post.likes.append(user)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/post_page/dislike')
@login_required
def dislike():
    post_id = request.args.get('post_id')
    user = current_user
    
    post = Article.query.filter_by(id=post_id).first_or_404()
    if user in post.likes:
        post.likes.remove(user)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/edit_post',methods=['GET','POST'])
@login_required
def edit_post():
    post_id = request.args.get('post_id')
    post = Article.query.filter_by(id=post_id).first_or_404()
    user = current_user

    if user.id != post.user_id:
        return redirect(url_for('index'))

        
    form = ArticleForm()
    if form.validate_on_submit():
        post.title =  form.title.data
        post.body = form.post.data
        #post.created_at = datetime.utcnow
        db.session.commit()
        flash('Changes saved')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.post.data = post.body
    return render_template('create_article.html', title='Edit Post', form=form)


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

    return redirect('/post_page/1')
    
    '''if current_user.is_authenticated:
        name = current_user.username
        posts = current_user.followed_posts()
    else:
        name = 'Guest'
        posts = Article.query.order_by(Article.created_at.desc()).all()
    
    return render_template('index.html', title='Home page', user={'name':name}, posts=posts)
    '''

@app.route('/sign_in', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested: Name - {}, remember me - {}'.format(form.username.data, form.remember_me.data))
        #return redirect(url_for('index'))
        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username of password')
            return redirect(url_for('sign_in'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('sign_in.html', tilte='Sign in', form=form)

@app.route('/sign_out')
def loglout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/sign_up', methods=['GET','POST'])
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
        return redirect(url_for('sign_in'))
    
    return render_template('sign_up.html', title='Sign Up', form=form)

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

