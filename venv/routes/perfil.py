from flask import Blueprint, request, jsonify
from venv.services.perfil_service import obtener_usuarios, crear_usuario, obtener_usuario_por_id, actualizar_usuario
from venv.schemas.perfil import PerfilSchema

perfil_bp = Blueprint('perfil_bp', __name__, url_prefix='/api/v1/perfiles')
usuario_schema = PerfilSchema()
perfiles_schema = PerfilSchema(many=True)

@perfil_bp.route('', methods=['GET'])
def obtener():
    """Obtiene todos los perfiles."""
    perfiles = obtener_usuarios()  # Suponiendo que esta función obtiene perfiles, ajusta según sea necesario
    return usuario_schema.jsonify(perfiles, many=True)

@perfil_bp.route('', methods=['POST'])
def crear():
    """Crea un nuevo perfil."""
    data = request.json
    nuevo_perfil = crear_usuario(data)  # Suponiendo que esta función crea un perfil, ajusta según sea necesario
    return usuario_schema.jsonify(nuevo_perfil), 201

@perfil_bp.route('/<int:id>', methods=['GET'])
def obtener_por_id(id):
    """Obtiene un perfil por ID."""
    perfil = obtener_usuario_por_id(id)  # Suponiendo que esta función obtiene un perfil por ID, ajusta según sea necesario
    if perfil:
        return usuario_schema.jsonify(perfil)
    else:
        return jsonify({'mensaje': 'Perfil no encontrado'}), 404

@perfil_bp.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    """Actualiza un perfil existente."""
    data = request.json
    perfil_actualizado = actualizar_usuario(id, data)  # Suponiendo que esta función actualiza un perfil, ajusta según sea necesario
    if perfil_actualizado:
        return usuario_schema.jsonify(perfil_actualizado)
    else:
        return jsonify({'mensaje': 'Perfil no encontrado'}), 404

