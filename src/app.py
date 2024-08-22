from flask import Flask
from fakebook.routes import fb_endpoints

def init_app():
    app = Flask(__name__)
    
    app.register_blueprint(fb_endpoints)

    return app

if (__name__ == '__main__'):
    app = init_app()
    app.run()