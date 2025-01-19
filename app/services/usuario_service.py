from models.usuario import Usuario
from app import db

def get_all_usuarios():
    return Usuario.query.all()

def get_usuario_by_id(usuario_id):
    return Usuario.query.get(usuario_id)

def create_usuario(nome, email, id_tipo_usuario, foto_perfil=None):
    usuario = Usuario(nome=nome, email=email, id_tipo_usuario=id_tipo_usuario, foto_perfil=foto_perfil)
    db.session.add(usuario)
    db.session.commit()
    return usuario

def update_usuario(usuario_id, nome, email, id_tipo_usuario, foto_perfil=None):
    usuario = get_usuario_by_id(usuario_id)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        usuario.id_tipo_usuario = id_tipo_usuario
        usuario.foto_perfil = foto_perfil
        db.session.commit()
    return usuario

def delete_usuario(usuario_id):
    usuario = get_usuario_by_id(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return usuario