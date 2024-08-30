from fakebook.database import Enemy, User, mysql
import os, random, string, pathlib

# Retrieves a user id
def get_id(username):
    # Check user 
    user = User.query.filter_by(nickname=username).first()
    if (user): 
        return user.id
    else:
        return None

# Retrieves a user bio
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

# Changes avatar image
def update_avatar(avatar, user_id):
    # Generate a new filename
    extension = pathlib.Path(avatar.filename).suffix
    hash_filename = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    hash_filename = hash_filename + extension

    # Update user object
    user = User.query.filter_by(id=user_id).first()
    if (not user): return False
    
    # Change user data
    prev_filename = user.avatar_filename
    user.avatar_filename = hash_filename
    try:
        # Update user
        mysql.session.add(user)
        mysql.session.commit()

        avatar.save(os.path.join('avatars', hash_filename))

        # Delete previous avatar image
        if (os.path.exists(f'avatars/{prev_filename}')):
            os.remove(os.path.join('avatars', prev_filename))
    except:
        return False
    return True