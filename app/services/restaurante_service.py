from models.restaurante import Restaurante
from app import db

def get_all_restaurantes():
    return Restaurante.query.all()

def get_restaurante_by_id(restaurante_id):
    return Restaurante.query.get(restaurante_id)

def get_restaurantes_by_nome(nome):
    return Restaurante.query.filter(Restaurante.nome.ilike(f"%{nome}%")).all()

def create_restaurante(nome, id_usuario, foto=None, foto_capa_de_fundo=None, latitude=None, longitude=None):
    restaurante = Restaurante(
        nome=nome,
        id_usuario=id_usuario,
        foto=foto,
        foto_capa_de_fundo=foto_capa_de_fundo,
        latitude=latitude,
        longitude=longitude
    )
    db.session.add(restaurante)
    db.session.commit()
    return restaurante

def update_restaurante(restaurante_id, nome, id_usuario, foto=None, foto_capa_de_fundo=None, latitude=None, longitude=None):
    restaurante = get_restaurante_by_id(restaurante_id)
    if restaurante:
        restaurante.nome = nome
        restaurante.id_usuario = id_usuario
        restaurante.foto = foto
        restaurante.foto_capa_de_fundo = foto_capa_de_fundo
        restaurante.latitude = latitude
        restaurante.longitude = longitude
        db.session.commit()
    return restaurante

def delete_restaurante(restaurante_id):
    restaurante = get_restaurante_by_id(restaurante_id)
    if restaurante:
        db.session.delete(restaurante)
        db.session.commit()
    return restaurante