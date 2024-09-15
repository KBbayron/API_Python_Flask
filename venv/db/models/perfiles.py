from venv.db.models import db
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Perfil(db.Model):
    __tablename__ = 'perfil'  # Asegúrate de que este sea el nombre correcto de la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DNI = db.Column(db.String(20), nullable=False)
    informacion = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    

