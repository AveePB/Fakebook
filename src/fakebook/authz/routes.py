from fakebook.authz.tokens import generate_token
from fakebook.database import User, mysql
from flask import Blueprint, jsonify, render_template, request

authz_bp = Blueprint('authz_bp', __name__)

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
        
        # Create new user
        new_user = User(nickname=data['username'])
        new_user.set_password(data['password'])
        mysql.session.add(new_user)
        mysql.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    
    # Other methods
    else:
        return jsonify({'message': 'Not Found 404'}), 404 


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
        
        return jsonify({'token': generate_token(user)})

    # Other methods
    else:
        return jsonify({'error': 'Not Found 404'}), 404 
