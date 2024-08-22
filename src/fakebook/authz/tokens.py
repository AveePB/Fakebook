from fakebook.database import Token, mysql
from fakebook.config import Config
from functools import wraps
from flask import redirect, request
from datetime import datetime, timedelta, timezone
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
            return redirect('/authz/login')

        try:
            # Decode the token
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])

            # Check for expiration time
            exp = data.get('exp')
            if (not exp):
                return redirect('/authz/login')

            # Convert expiration time to a timezone-aware datetime object
            exp_date = datetime.fromtimestamp(exp, tz=timezone.utc)

            # Compare expiration time with the current UTC time
            if (exp_date < datetime.now(tz=timezone.utc)):
                return redirect('/authz/login')


        except jwt.ExpiredSignatureError:
            return redirect('/authz/login')
        except jwt.InvalidTokenError:
            return redirect('/authz/login')
        except Exception as e:
            return redirect('/authz/login')
        
        # Verify if token exists
        token_record = Token.query.filter_by(raw_form=token).first()
        if (not token_record):
            return redirect('/authz/login')

        return f(*args, **kwargs)

    return decorated

# Creates tokens
def generate_token(user):
    # Generate the JWT token
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=Config.TOKEN_LIFESPAN)
    }, Config.SECRET_KEY, algorithm='HS256')

    # Check if a token already exists for the user
    token_record = Token.query.filter_by(id=user.id).first()

    if (token_record):
        # Update the existing token record
        token_record.raw_form = token
    else:
        # Create a new token record
        mysql.session.add(Token(id=user.id, raw_form=token))

    # Commit the changes to the database
    mysql.session.commit()
    
    return token