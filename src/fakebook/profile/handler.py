from fakebook.database import User

# Constructs a user bio
def get_bio(user_id):
    user = User.query.filter_by(id=user_id).first()
    
    if (user == None or user.bio == None): 
        return "Default bio..."
    
    else:
        return user.bio

# Retrieves enemies list
def get_enemies(user_id):
    user = User.query.filter_by(id=user_id).first()
    
    return ['Dangerous Enemy', 'Amazing Enemy', 'Weirdo Enemy']