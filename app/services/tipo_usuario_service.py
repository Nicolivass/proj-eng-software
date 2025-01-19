from models.tipo_usuario import TipoUsuario
from app import db

def get_all_tipo_usuario():
    return TipoUsuario.query.all()

def get_tipo_usuario_by_id(tipo_usuario_id):
    return TipoUsuario.query.get(tipo_usuario_id)

def create_tipo_usuario(descricao):
    tipo_usuario = TipoUsuario(descricao=descricao)
    db.session.add(tipo_usuario)
    db.session.commit()
    return tipo_usuario

def update_tipo_usuario(tipo_usuario_id, descricao):
    tipo_usuario = get_tipo_usuario_by_id(tipo_usuario_id)
    if tipo_usuario:
        tipo_usuario.descricao = descricao
        db.session.commit()
    return tipo_usuario

def delete_tipo_usuario(tipo_usuario_id):
    tipo_usuario = get_tipo_usuario_by_id(tipo_usuario_id)
    if tipo_usuario:
        db.session.delete(tipo_usuario)
        db.session.commit()
    return tipo_usuario