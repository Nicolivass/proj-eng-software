from flask import Blueprint, request, jsonify
from services.menu_service import *

menu_bp = Blueprint('menu', __name__, url_prefix='/menus')

@menu_bp.route('/', methods=['GET'])
def get_menus():
    menus = get_all_menus()
    return jsonify([{
        "id": menu.id,
        "nome": menu.nome,
        "descricao": menu.descricao,
        "id_restaurante": menu.id_restaurante,
        "foto": menu.foto
    } for menu in menus])

@menu_bp.route('/<int:id>', methods=['GET'])
def get_menu(id):
    menu = get_menu_by_id(id)
    if not menu:
        return jsonify({"error": "Menu não encontrado"}), 404
    return jsonify({
        "id": menu.id,
        "nome": menu.nome,
        "descricao": menu.descricao,
        "id_restaurante": menu.id_restaurante,
        "foto": menu.foto
    })

@menu_bp.route('/', methods=['POST'])
def add_menu():
    data = request.get_json()
    menu = create_menu(
        nome=data['nome'],
        descricao=data['descricao'],
        id_restaurante=data['id_restaurante'],
        foto=data.get('foto')
    )
    return jsonify({
        "id": menu.id,
        "nome": menu.nome,
        "descricao": menu.descricao,
        "id_restaurante": menu.id_restaurante,
        "foto": menu.foto
    }), 201

@menu_bp.route('/<int:id>', methods=['PUT'])
def edit_menu(id):
    data = request.get_json()
    menu = update_menu(
        menu_id=id,
        nome=data['nome'],
        descricao=data['descricao'],
        id_restaurante=data['id_restaurante'],
        foto=data.get('foto')
    )
    if not menu:
        return jsonify({"error": "Menu não encontrado"}), 404
    return jsonify({
        "id": menu.id,
        "nome": menu.nome,
        "descricao": menu.descricao,
        "id_restaurante": menu.id_restaurante,
        "foto": menu.foto
    })

@menu_bp.route('/<int:id>', methods=['DELETE'])
def delete_menu_controller(id):
    menu = delete_menu(id)
    if not menu:
        return jsonify({"error": "Menu não encontrado"}), 404
    return jsonify({"message": "Menu deletado com sucesso"})
