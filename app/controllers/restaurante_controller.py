from flask import Blueprint, request, jsonify
from services.restaurante_service import *

restaurante_bp = Blueprint('restaurante', __name__, url_prefix='/restaurantes')

@restaurante_bp.route('/', methods=['GET'])
def get_restaurantes():
    restaurantes = get_all_restaurantes()
    return jsonify([{
        "id": restaurante.id,
        "nome": restaurante.nome,
        "foto": restaurante.foto,
        "foto_capa_de_fundo": restaurante.foto_capa_de_fundo,
        "latitude": restaurante.latitude,
        "longitude": restaurante.longitude,
        "id_usuario": restaurante.id_usuario
    } for restaurante in restaurantes])

@restaurante_bp.route('/<int:id>', methods=['GET'])
def get_restaurante(id):
    restaurante = get_restaurante_by_id(id)
    if not restaurante:
        return jsonify({"error": "Restaurante não encontrado"}), 404
    return jsonify({
        "id": restaurante.id,
        "nome": restaurante.nome,
        "foto": restaurante.foto,
        "foto_capa_de_fundo": restaurante.foto_capa_de_fundo,
        "latitude": restaurante.latitude,
        "longitude": restaurante.longitude,
        "id_usuario": restaurante.id_usuario
    })

@restaurante_bp.route('/buscar', methods=['GET'])
def buscar_restaurantes_por_nome():
    nome = request.args.get('nome', '')
    restaurantes = get_restaurantes_by_nome(nome)
    return jsonify([{
        "id": restaurante.id,
        "nome": restaurante.nome,
        "foto": restaurante.foto,
        "foto_capa_de_fundo": restaurante.foto_capa_de_fundo,
        "latitude": restaurante.latitude,
        "longitude": restaurante.longitude,
        "id_usuario": restaurante.id_usuario
    } for restaurante in restaurantes])

@restaurante_bp.route('/', methods=['POST'])
def add_restaurante():
    data = request.get_json()
    restaurante = create_restaurante(
        nome=data['nome'],
        id_usuario=data['id_usuario'],
        foto=data.get('foto'),
        foto_capa_de_fundo=data.get('foto_capa_de_fundo'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude')
    )
    return jsonify({
        "id": restaurante.id,
        "nome": restaurante.nome,
        "foto": restaurante.foto,
        "foto_capa_de_fundo": restaurante.foto_capa_de_fundo,
        "latitude": restaurante.latitude,
        "longitude": restaurante.longitude,
        "id_usuario": restaurante.id_usuario
    }), 201

@restaurante_bp.route('/<int:id>', methods=['PUT'])
def edit_restaurante(id):
    data = request.get_json()
    restaurante = update_restaurante(
        restaurante_id=id,
        nome=data['nome'],
        id_usuario=data['id_usuario'],
        foto=data.get('foto'),
        foto_capa_de_fundo=data.get('foto_capa_de_fundo'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude')
    )
    if not restaurante:
        return jsonify({"error": "Restaurante não encontrado"}), 404
    return jsonify({
        "id": restaurante.id,
        "nome": restaurante.nome,
        "foto": restaurante.foto,
        "foto_capa_de_fundo": restaurante.foto_capa_de_fundo,
        "latitude": restaurante.latitude,
        "longitude": restaurante.longitude,
        "id_usuario": restaurante.id_usuario
    })

@restaurante_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurante_controller(id):
    restaurante = delete_restaurante(id)
    if not restaurante:
        return jsonify({"error": "Restaurante não encontrado"}), 404
    return jsonify({"message": "Restaurante deletado com sucesso"})
