
USERNAME_CRITERIA = "The username must be alphanumeric"
PASSWORD_CRITERIA = "The password must have at least 6 characters"

# Checks username criteria
def validateUsername(username) -> bool:
    # Length Check
    if (len(username) <= 0 or len(username) >= 128): 
        return False
    
    # Char Check
    if (not username.isalnum()):
        return False
    
    return True

# Checks password criteria
def validatePassword(password) -> bool:
    # Length Check
    if (len(password) < 6 or len(password) >= 256): 
        return False
    
    return True
    
