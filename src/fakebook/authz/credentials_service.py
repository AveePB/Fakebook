from authz.models import UserCredentials

# Exceptions
class CriteriaError(Exception): pass
class FieldRequired(Exception): pass
class UsernameTakenError(Exception): pass

# Criteria
def validateUsername(username: str):
    # Null
    if (not username):
        raise FieldRequired()
        
    # Length
    if (not(5 <= len(username) and len(username) <= 32)):
        raise CriteriaError()
        
    # Alpha-numeric
    if (not username.isalnum()):
        raise CriteriaError()

    # Unique
    if (UserCredentials.objects.filter(username=username).exists()):
        raise UsernameTakenError()

def validatePassword(password: str):
    # Null
    if (not password):
        raise FieldRequired()
        
    # Length
    if (not(6 <= len(password) and len(password) <= 32)):
        raise CriteriaError()
        
def checkCredentials(username: str, password: str):
    usercredentials = UserCredentials.objects.filter(username=username).first()
    if (not usercredentials): return False

    return usercredentials.check_password(password)