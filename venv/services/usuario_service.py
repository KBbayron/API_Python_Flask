from venv.db.models import db
from venv.db.models.usuarios import Usuario  # Ajusta según tu estructura de modelos

def obtener_usuarios():
    """Obtiene todos los usuarios."""
    return Usuario.query.all()

def crear_usuario(data):
    """Crea un nuevo usuario."""
    nuevo_usuario = Usuario(
        nombre=data.get('nombre'),
        correo=data.get('correo'),
        contrasena=data.get('contrasena'),
        fecha=data.get('fecha_registro')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def obtener_usuario_por_id(id):
    """Obtiene un usuario por ID."""
    return Usuario.query.get(id)

def actualizar_usuario(id, data):
    """Actualiza un usuario existente."""
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.correo = data.get('correo', usuario.correo)
        usuario.contrasena = data.get('contrasena', usuario.contrasena)
        usuario.fecha = data.get('fecha_registro', usuario.fecha_registro)
        db.session.commit()
        return usuario
    return None

def eliminar_usuario(id):
    """Elimina un usuario existente."""
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False
