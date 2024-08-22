from flask import Blueprint, render_template

fb_endpoints = Blueprint('fb_endpoints', __name__)

@fb_endpoints.route('/')
def home():
    return render_template('index.html')

@fb_endpoints.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)