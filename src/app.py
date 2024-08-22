from fakebook.authz.routes import authz_bp
from fakebook.database import mysql
from fakebook.config import Config
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=None)

if (__name__ == '__main__'):
    # Update constants 
    app.config.from_object(Config)

    #Pin database & blueprints
    mysql.init_app(app)
    app.register_blueprint(authz_bp)
    
    # Create tables
    with app.app_context():
        mysql.create_all()
    
    app.run()