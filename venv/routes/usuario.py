from flask import Blueprint, request, jsonify
from venv.services.usuario_service import obtener_usuarios, crear_usuario, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario
from venv.schemas.usuario import UsuarioSchema

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuarios')
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@usuario_bp.route('', methods=['GET'])
def obtener():
    """Obtiene todos los usuarios."""
    usuarios = obtener_usuarios()
    result = usuarios_schema.dump(usuarios)  # Serializa los usuarios
    return jsonify(result)  # Convierte el resultado a JSON

@usuario_bp.route('', methods=['POST'])
def crear():
    """Crea un nuevo usuario."""
    data = request.json
    nuevo_usuario = crear_usuario(data)
    result = usuario_schema.dump(nuevo_usuario)  # Serializa el nuevo usuario
    return jsonify(result), 201  # Convierte el resultado a JSON

@usuario_bp.route('/<int:id>', methods=['GET'])
def obtener_por_id(id):
    """Obtiene un usuario por ID."""
    usuario = obtener_usuario_por_id(id)
    if usuario:
        result = usuario_schema.dump(usuario)  # Serializa el usuario
        return jsonify(result)  # Convierte el resultado a JSON
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    """Actualiza un usuario existente."""
    data = request.json
    usuario_actualizado = actualizar_usuario(id, data)
    if usuario_actualizado:
        result = usuario_schema.dump(usuario_actualizado)  # Serializa el usuario actualizado
        return jsonify(result)  # Convierte el resultado a JSON
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def eliminar(id):
    """Elimina un usuario existente."""
    exito = eliminar_usuario(id)
    if exito:
        return jsonify({'mensaje': 'Usuario eliminado'}), 204
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
