from fakebook.database import Enemy, User

# Constructs a user bio
def get_bio(user_id):
    # Check user id
    user = User.query.filter_by(id=user_id).first()
    if (user == None or user.bio == None): 
        return "..."
    
    else:
        return user.bio

# Retrieves enemies list
def get_enemies(user_id):
    # Check user id
    user = User.query.filter_by(id=user_id).first()
    if (user == None):
        return []
    else:
        # Fetch all relations
        e1 = Enemy.query.filter_by(user1_id=user_id).all()
        e2 = Enemy.query.filter_by(user2_id=user_id).all()

        # Get enemies ids
        ids_set = set()

        for e in e1:
            ids_set.add(e.user1_id); ids_set.add(e.user2_id)
        
        for e in e2:
            ids_set.add(e.user1_id); ids_set.add(e.user2_id)

        # Remove current user's id
        if (user_id in ids_set):
            ids_set.remove(user_id) 

        # Fetch user objects
        enemies = []
        for e_id in ids_set:
            # Get enemy's user object
            enemy = User.query.filter_by(id=e_id).first()
            enemies.append(enemy)

    return enemies

# Returns all profiles that contain the pattern
def get_suggestions(pattern):
    return User.query.filter(User.nickname.ilike(f'%{pattern}%')).all()