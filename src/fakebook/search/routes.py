from fakebook.profile.userservice import get_suggestions
from flask import Blueprint, jsonify, render_template, request

search_bp = Blueprint('search_bp', __name__)

# Returns search page
@search_bp.route('/search', methods=['GET'])
def fetch_startpage():
    return render_template('search.html')

# Suggests profiles
@search_bp.route('/search/suggestions', methods=['GET'])
def find_suggestions():
    query = request.args.get('query', '')
    if (query):
        # Fetch suggested profiles
        profiles = get_suggestions(query)
        data = [{'id': profile.id, 'username': profile.nickname} for profile in profiles]

        return jsonify(data), 200
    else:
        return jsonify([]), 404

# Fetches profile page
