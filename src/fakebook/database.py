from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

mysql = SQLAlchemy()

class User(mysql.Model):
    __tablename__ = 'users'

    id = mysql.Column(mysql.Integer, primary_key=True)
    nickname = mysql.Column(mysql.String(128), unique=True, nullable=False)
    password_hash = mysql.Column(mysql.String(256), nullable=False)

    def set_password(self, password) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'<User {self.nickname}>'
    
class Token(mysql.Model):
    __tablename__ = 'tokens'

    id = mysql.Column(mysql.Integer, mysql.ForeignKey('users.id'),  primary_key=True)
    raw_form = mysql.Column(mysql.String(256), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'<Token {self.raw_form}>'