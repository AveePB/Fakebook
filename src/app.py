from fakebook.authz.routes import authz_bp
from fakebook.authz.tokens import validate_cookies
from fakebook.database import mysql
from fakebook.config import Config
from fakebook.profile.routes import profile_bp
from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    if (not validate_cookies()):
        return redirect('/authz/login')
    return render_template('index.html', posts=None)

if (__name__ == '__main__'):
    # Update constants 
    app.config.from_object(Config)

    # Pin database & blueprints
    mysql.init_app(app)

    app.register_blueprint(authz_bp)
    app.register_blueprint(profile_bp)
    
    # Create tables
    with app.app_context():
        mysql.create_all()
    
    # Start application
    app.run()