from models.menu import Menu
from app import db

def get_all_menus():
    return Menu.query.all()

def get_menu_by_id(menu_id):
    return Menu.query.get(menu_id)

def create_menu(nome, descricao, id_restaurante, foto=None):
    menu = Menu(nome=nome, descricao=descricao, id_restaurante=id_restaurante, foto=foto)
    db.session.add(menu)
    db.session.commit()
    return menu

def update_menu(menu_id, nome, descricao, id_restaurante, foto=None):
    menu = get_menu_by_id(menu_id)
    if menu:
        menu.nome = nome
        menu.descricao = descricao
        menu.id_restaurante = id_restaurante
        menu.foto = foto
        db.session.commit()
    return menu

def delete_menu(menu_id):
    menu = get_menu_by_id(menu_id)
    if menu:
        db.session.delete(menu)
        db.session.commit()
    return menu