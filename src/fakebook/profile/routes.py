from fakebook.authz.tokens import get_user_id, validate_cookies
from fakebook.database import User
from fakebook.profile.handler import get_bio, get_enemies
from flask import Blueprint, jsonify, url_for, send_from_directory, redirect, render_template, request

profile_bp = Blueprint('profile_bp', __name__)

# Displays profiles
@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def fetch_profile(user_id):
    # Validate cookies
    if (not validate_cookies()):
        return redirect('/authz/login')
    
    # Check if user exists
    user = User.query.filter_by(id=user_id).first()
    if (user):
        # Load avatar url
        avatar_url = url_for('serve_avatar', filename=user.avatar_filename) if user.avatar_filename else url_for('static', filename='img/avatar.jpg')

        return render_template('profile.html', avatar_url=avatar_url, username=user.nickname,  
                               bio=get_bio(user.id), enemies=get_enemies(user.id))
    else:
        return jsonify({'message': 'User not found'}), 404

# Displays logged profile
@profile_bp.route('/profile/me', methods=['GET'])
def fetch_my_profile():
    # Validate cookies
    if (not validate_cookies()):
        return redirect('/authz/login')
    
    # Check if user exists
    jwt = request.cookies.get('jwt')
    user = User.query.filter_by(id=get_user_id(jwt)).first()
    if (user):
        return redirect(f'/profile/{user.id}')
    else:
        return jsonify({'message': 'User not found'}), 404

# Serves avatar images
@profile_bp.route('/avatars/<filename>')
def serve_avatar(filename):
    return send_from_directory('avatars', filename)