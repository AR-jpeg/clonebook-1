from src import login_manager
from src import db

@login_manager.user_loader
def LoadUser(id: int):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'