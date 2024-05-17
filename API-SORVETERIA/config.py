from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Configurações do aplicativo Flask
app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 8000
app.config["DEBUG"] = True

# Configurações do banco de dados SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa o SQLAlchemy com o aplicativo Flask
db = SQLAlchemy(app)
