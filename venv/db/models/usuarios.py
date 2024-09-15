from venv.db.models import db
from sqlalchemy import func

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=func.now())
    
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'), nullable=True)
    
    perfil = db.relationship('Perfil', backref=db.backref('usuarios', lazy=True))

