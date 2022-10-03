from geral.config import *
from modelo.pessoa import Pessoa

class Professor(Pessoa):
    #criação da tabela
    __tablename__ = "professor"

    #chave estrangeira
    id = db.Column(db.Integer, db.ForeignKey("pessoa.id"), primary_key=True)
    salario = db.Column(db.Float, nullable = False)

    #type na classe mãe -Pessoa-
    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }

    #expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "salario": self.salario,
        }