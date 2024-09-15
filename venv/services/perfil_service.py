from venv.db.models.perfiles import Perfil
from venv.db.models import db

def obtener_perfiles():
    """Obtiene todos los perfiles."""
    return Perfil.query.all()

def crear_perfil(data):
    """Crea un nuevo perfil."""
    nuevo_perfil = Perfil(
        DNI=data.get('DNI'),
        informacion=data.get('informacion'),
        status=data.get('status', True)  # Usa True por defecto si no se proporciona
    )
    db.session.add(nuevo_perfil)
    db.session.commit()
    return nuevo_perfil

def obtener_perfil_por_id(id):
    """Obtiene un perfil por ID."""
    return Perfil.query.get(id)

def actualizar_perfil(id, data):
    """Actualiza un perfil existente."""
    perfil = Perfil.query.get(id)
    if perfil:
        perfil.DNI = data.get('DNI', perfil.DNI)
        perfil.informacion = data.get('informacion', perfil.informacion)
        perfil.status = data.get('status', perfil.status)
        db.session.commit()
        return perfil
    return None
