from flask import Blueprint, request, jsonify
from venv.services.perfil_service import obtener_perfiles, crear_perfil, obtener_perfil_por_id, actualizar_perfil
from venv.schemas.perfil import PerfilSchema

perfil_bp = Blueprint('perfil_bp', __name__, url_prefix='/perfiles')
perfil_schema = PerfilSchema()
perfiles_schema = PerfilSchema(many=True)

@perfil_bp.route('', methods=['GET'])
def obtener():
    """Obtiene todos los perfiles."""
    perfiles = obtener_perfiles()  # Ajusta esta función según sea necesario
    result = perfiles_schema.dump(perfiles)
    return jsonify(result)

@perfil_bp.route('', methods=['POST'])
def crear():
    """Crea un nuevo perfil."""
    data = request.json
    nuevo_perfil = crear_perfil(data)  # Ajusta esta función según sea necesario
    result = perfil_schema.dump(nuevo_perfil)
    return jsonify(result), 201

@perfil_bp.route('/<int:id>', methods=['GET'])
def obtener_por_id(id):
    """Obtiene un perfil por ID."""
    perfil = obtener_perfil_por_id(id)  # Ajusta esta función según sea necesario
    if perfil:
        result = perfil_schema.dump(perfil)
        return jsonify(result)
    else:
        return jsonify({'mensaje': 'Perfil no encontrado'}), 404

@perfil_bp.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    """Actualiza un perfil existente."""
    data = request.json
    perfil_actualizado = actualizar_perfil(id, data)  # Ajusta esta función según sea necesario
    if perfil_actualizado:
        result = perfil_schema.dump(perfil_actualizado)
        return jsonify(result)
    else:
        return jsonify({'mensaje': 'Perfil no encontrado'}), 404
