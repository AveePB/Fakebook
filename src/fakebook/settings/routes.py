from fakebook.authz.tokens import token_required, get_user_id
from fakebook.profile.userservice import get_enemies
from flask import Blueprint, render_template, request

settings_bp = Blueprint('settings_bp', __name__)

@settings_bp.route('/settings')
@token_required
def fetch_settings():
    # Get user id
    token = request.cookies.get('jwt')
    user_id = get_user_id(token)

    return render_template('settings.html', enemies=get_enemies(user_id))

