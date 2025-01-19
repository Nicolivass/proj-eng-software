from app import db

class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<TipoUsuario {self.descricao}>"