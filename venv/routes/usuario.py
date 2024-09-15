from flask import Blueprint, request, jsonify
from venv.services.usuario_service import obtener_usuarios, crear_usuario, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario
from venv.schemas.usuario import UsuarioSchema

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/api/v1/usuarios')
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@usuario_bp.route('', methods=['GET'])
def obtener():
    """Obtiene todos los usuarios."""
    usuarios = obtener_usuarios()
    return usuarios_schema.jsonify(usuarios)

@usuario_bp.route('', methods=['POST'])
def crear():
    """Crea un nuevo usuario."""
    data = request.json
    nuevo_usuario = crear_usuario(data)
    return usuario_schema.jsonify(nuevo_usuario), 201

@usuario_bp.route('/<int:id>', methods=['GET'])
def obtener_por_id(id):
    """Obtiene un usuario por ID."""
    usuario = obtener_usuario_por_id(id)
    if usuario:
        return usuario_schema.jsonify(usuario)
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    """Actualiza un usuario existente."""
    data = request.json
    usuario_actualizado = actualizar_usuario(id, data)
    if usuario_actualizado:
        return usuario_schema.jsonify(usuario_actualizado)
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
