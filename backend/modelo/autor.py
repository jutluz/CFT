from geral.config import *

class Autor(db.Model):
    # criação da tabela
    __tablename__ = "autor"

    # atributos do autor
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable = False)

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }
