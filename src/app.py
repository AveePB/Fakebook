from fakebook.authz.routes import authz_bp
from fakebook.authz.tokens import token_required
from fakebook.database import mysql
from fakebook.config import Config
from fakebook.profile.routes import profile_bp
from fakebook.search.routes import search_bp
from fakebook.settings.routes import settings_bp
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
@token_required
def home():
    return redirect('/search')

if (__name__ == '__main__'):
    # Update constants 
    app.config.from_object(Config)

    # Pin database & blueprints
    mysql.init_app(app)

    app.register_blueprint(authz_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(settings_bp)

    # Create tables
    with app.app_context():
        mysql.create_all()
    
    # Start application
    app.run()