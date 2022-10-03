from geral.config import *
from modelo.turma import Turma

class Instrumento(db.Model):
    #criação da tabela
    __tablename__ = "instrumento"

    #colunas com os atributos pra tabela no SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey(Turma.id))
    #na lista reversa em Turma já é criado o atributo "turma" em Instrumento

    #função pra transformar os atributos em json
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "turma_id":self.turma_id
        } 