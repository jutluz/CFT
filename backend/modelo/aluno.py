from geral.config import *
from modelo.pessoa import Pessoa

class Aluno(Pessoa):
    # criação da tabela
    __tablename__ = "aluno"

    # chave estrangeira
    id = db.Column(db.Integer, db.ForeignKey("pessoa.id"), primary_key=True)

    # type na classe mãe -Pessoa-
    __mapper_args__ = {
        "polymorphic_identity": "aluno",
    }
