from fakebook.database import User
from fakebook.config import Config
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta, timezone, UTC
import jwt

# Authenticates tokens
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if the token is in the Authorization header
        if ('Authorization' in request.headers):
            token = request.headers['Authorization'].split(" ")[1]

        if (not token):
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            # Decode the token
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])

            # Check for expiration time
            exp = data.get('exp')
            if (not exp):
                return jsonify({'message': 'No expiration date in token!'}), 403

            # Convert expiration time to a timezone-aware datetime object
            exp_date = datetime.fromtimestamp(exp, tz=timezone.utc)

            # Compare expiration time with the current UTC time
            if (exp_date < datetime.now(tz=timezone.utc)):
                return jsonify({'message': 'Token has expired!'}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403
        except Exception as e:
            return jsonify({'message': str(e)}), 403

        return f(current_user, *args, **kwargs)

    return decorated

# Creates tokens
def generateToken(user):
    return jwt.encode({
            'user_id': user.id,
            'exp': datetime.now(UTC) + timedelta(minutes=Config.TOKEN_LIFESPAN)
        }, Config.SECRET_KEY, algorithm='HS256')

