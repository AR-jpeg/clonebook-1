from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

login_manager = LoginManager()

db = SQLAlchemy(app)

def create_app():
    from src import models

    from src.routes.main import main

    app.register_blueprint(main)

    return app
