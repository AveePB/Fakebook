import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://fakebook:f4k3_is@localhost/fakebook_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables a feature that unnecessarily uses more memory

    # Json Web Token configuration
    SECRET_KEY = 'f4ke_k3y'
    TOKEN_LIFESPAN = 3600
