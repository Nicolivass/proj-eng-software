from flask import Blueprint, request, jsonify
from services.usuario_service import *

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = get_all_usuarios()
    return jsonify([{
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "id_tipo_usuario": usuario.id_tipo_usuario,
        "foto_perfil": usuario.foto_perfil
    } for usuario in usuarios])

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = get_usuario_by_id(id)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "id_tipo_usuario": usuario.id_tipo_usuario,
        "foto_perfil": usuario.foto_perfil
    })

@usuario_bp.route('/', methods=['POST'])
def add_usuario():
    data = request.get_json()
    usuario = create_usuario(
        nome=data['nome'],
        email=data['email'],
        id_tipo_usuario=data['id_tipo_usuario'],
        foto_perfil=data.get('foto_perfil')
    )
    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "id_tipo_usuario": usuario.id_tipo_usuario,
        "foto_perfil": usuario.foto_perfil
    }), 201

@usuario_bp.route('/<int:id>', methods=['PUT'])
def edit_usuario(id):
    data = request.get_json()
    usuario = update_usuario(
        usuario_id=id,
        nome=data['nome'],
        email=data['email'],
        id_tipo_usuario=data['id_tipo_usuario'],
        foto_perfil=data.get('foto_perfil')
    )
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "id_tipo_usuario": usuario.id_tipo_usuario,
        "foto_perfil": usuario.foto_perfil
    })

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def delete_usuario_controller(id):
    usuario = delete_usuario(id)
    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário deletado com sucesso"})
