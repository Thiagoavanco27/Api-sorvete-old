from flask import Blueprint
from config import app, db

# Definindo o blueprint para posts
posts = Blueprint('posts', __name__)

# Rota principal para o blueprint de posts
@posts.route('/', methods=['GET'])
def main():
    return 'Posts routes'

# Definindo o modelo User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
