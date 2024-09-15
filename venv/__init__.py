from flask import Flask
from venv.db.config import Config
from venv.db.models import db
from venv.routes import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    init_app(app)

    return app


