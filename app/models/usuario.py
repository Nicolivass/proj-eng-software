from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'), nullable=False)
    foto_perfil = db.Column(db.String)

    # Relacionamento
    tipo_usuario = db.relationship('TipoUsuario', backref='usuarios', lazy=True)

    def __repr__(self):
        return f"<Usuario {self.nome} - {self.email}>"