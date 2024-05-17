from flask import Flask
from config import app, db
from index import posts
from flask_sqlalchemy import SQLAlchemy


# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Importa os blueprints e registra-os no aplicativo
from index import posts
from ice_cream.ice_cream_routes import ice_creams_blueprint
from categories.categories_routes import categories_blueprint

app.register_blueprint(posts)
app.register_blueprint(ice_creams_blueprint)
app.register_blueprint(categories_blueprint)

# Cria todas as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
