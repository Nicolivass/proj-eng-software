from app import db

class Restaurante(db.Model):
    __tablename__ = 'restaurante'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    foto = db.Column(db.String)
    foto_capa_de_fundo = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # Relacionamento
    usuario = db.relationship('Usuario', backref='restaurantes', lazy=True)

    def __repr__(self):
        return f"<Restaurante {self.nome}>"