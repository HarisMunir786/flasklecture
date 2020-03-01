from flask import render_template, url_for
from application import app
from application.models import Post

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all() 
    return render_template('home.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')
