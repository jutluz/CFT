from geral.config import *
from modelo.turma import Turma

class Pessoa(db.Model):
    # criação da tabela
    __tablename__ = "pessoa"

    # colunas com os atributos pra tabela no SQLAlchemy    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254), nullable = False)
    email = db.Column(db.String(254), nullable = False, unique = True)
    senha = db.Column(db.Text)
    type = db.Column(db.String(50)) #atributo discriminador

    # identidade polimórfica da classe
    __mapper_args__ = {
        "polymorphic_identity": "pessoa",
        "polymorphic_on": type,
    }

    # associação com a classe Turma
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable = False)
    turma = db.relationship("Turma", back_populates="pessoa")

    # função pra transformar os atributos em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "turma_id": self.turma_id,
            "type": self.type
        }
