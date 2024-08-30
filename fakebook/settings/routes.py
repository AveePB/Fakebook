from fakebook.authz.tokens import token_required, get_user_id
from fakebook.database import User, mysql
from fakebook.profile.userservice import get_enemies, update_avatar
from flask import Blueprint, jsonify, render_template, request

settings_bp = Blueprint('settings_bp', __name__)

@settings_bp.route('/settings', methods=['GET'])
@token_required
def fetch_settings():
    # Get user id
    token = request.cookies.get('jwt')
    user_id = get_user_id(token)

    return render_template('settings.html', enemies=get_enemies(user_id))

@settings_bp.route('/settings/avatar', methods=['POST'])
def change_avatar():
    # Get user id
    token = request.cookies.get('jwt')
    user_id = get_user_id(token)

    # Fetch avatar    
    img = request.files['avatar']
    if ('.' in img.filename):
        if (update_avatar(img, user_id)):
            return jsonify({'message': 'Successfully updated the avatar'}), 204
    
    return jsonify({'message', 'Failed to update the profile image'}), 400