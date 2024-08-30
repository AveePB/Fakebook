from fakebook.authz.criteria import validateUsername, validatePassword, USERNAME_CRITERIA, PASSWORD_CRITERIA
from fakebook.authz.tokens import generate_token
from fakebook.database import User, mysql
from fakebook.config import Config
from flask import Blueprint, jsonify, make_response, render_template, request

authz_bp = Blueprint('authz_bp', __name__)

# Register new users
@authz_bp.route('/authz/signup', methods=['GET', 'POST'])
def signup_user():
    # GET method
    if (request.method == 'GET'):
        return render_template('signup.html')
    
    # POST method
    elif (request.method == 'POST'):
        data = request.get_json()
        
        # Check request body
        if ((not data) or (not data.get('username')) or (not data.get('password'))):
            return jsonify({'message': 'Username and password are required'}), 400
        
        # Check data consistency
        user = User.query.filter_by(nickname=data['username']).first()
        if (user):
            return jsonify({'message': 'User already exists'}), 409
        
        # Validate username & password
        if (not validateUsername(data['username'])):
            return jsonify({'message': USERNAME_CRITERIA}), 400
        
        if (not validatePassword(data['password'])):
            return jsonify({'message': PASSWORD_CRITERIA}), 400

        # Create new user
        new_user = User(nickname=data['username'])
        new_user.set_password(data['password'])
        mysql.session.add(new_user)
        mysql.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    
    # Other methods
    else:
        return jsonify({'message': 'Not Found 404'}), 404 

# Authenticates users
@authz_bp.route('/authz/login', methods=['GET', 'POST'])
def login_user():
    # GET method
    if (request.method == 'GET'):
        return render_template('login.html')
    
    # POST method
    elif (request.method == 'POST'):
        data = request.get_json()

        # Check request body
        if ((not data) or (not data.get('username')) or (not data.get('password'))):
            return jsonify({'message': 'Username and password are required'}), 400
        
        # Check data consistency
        user = User.query.filter_by(nickname=data['username']).first()
        if ((not user) or (not user.check_password(data['password']))):
            return jsonify({'message': 'Invalid credentials'}), 401
        token = generate_token(user)
        
        response = make_response(jsonify({'message': 'Logged in successfully'}))
        response.set_cookie('jwt', token, max_age=Config.TOKEN_LIFESPAN, httponly=True, secure=True, )
    
        return response
    
    # Other methods
    else:
        return jsonify({'message': 'Not Found 404'}), 404 
