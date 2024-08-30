from fakebook.profile.userservice import get_id, get_suggestions 
from flask import Blueprint, jsonify, redirect, render_template, request

search_bp = Blueprint('search_bp', __name__)

# Returns search page
@search_bp.route('/search', methods=['GET'])
def fetch_startpage():
    return render_template('search.html')

# Suggests profiles
@search_bp.route('/search/suggestions', methods=['GET'])
def find_suggestions():
    # Check query
    query = request.args.get('query', '')
    if (query):
        # Fetch suggested profiles
        profiles = get_suggestions(query)
        data = [{'id': profile.id, 'username': profile.nickname} for profile in profiles]

        return jsonify(data), 200
    else:
        return jsonify([]), 404

# Fetches profile page
@search_bp.route('/search/profiles', methods=['GET'])
def load_profile():
    # Check query
    query = request.args.get('query', '')
    if (query):

        # Check user_id
        user_id = get_id(query)
        if (user_id):
            return redirect(f'/profile/{user_id}')
        else: 
            return render_template('profile404.html')
    else:
        return render_template('profile404.html')