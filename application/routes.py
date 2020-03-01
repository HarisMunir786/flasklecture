from flask import render_template, url_for, redirect
from application import app, db
from application.models import Post
from application.forms import PostForm

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all() 
    return render_template('home.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/post/create', methods=['GET','POST'])
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post.html', form=form)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')
