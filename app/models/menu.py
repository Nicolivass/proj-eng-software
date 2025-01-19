from app import db

class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    foto = db.Column(db.String)
    descricao = db.Column(db.String)
    id_restaurante = db.Column(db.Integer, db.ForeignKey('restaurante.id'), nullable=False)

    # Relacionamento
    restaurante = db.relationship('Restaurante', backref='menus', lazy=True)

    def __repr__(self):
        return f"<Menu {self.nome}>"