from geral.config import *
from modelo.agenda import Agenda

class Turma(db.Model):
    # criação da tabela
    __tablename__ = "turma"
    
    # colunas com os atributos pra tabela no SQLAlchemy 
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer, nullable = False)
    semestre = db.Column(db.Integer, nullable = False)
    
    # lista reversa de instrumentos que uma turma estuda
    instrumentos = db.relationship("Instrumento", backref="turma")

    # associação com a classe Pessoa
    pessoa = db.relationship("Pessoa", back_populates="turma")

    # autor que fez a musica não pode ser nulo por conta da composição
    agenda_id = db.Column(db.Integer, db.ForeignKey(Agenda.id), nullable = False)
    agenda = db.relationship("Agenda")

    # função pra transformar os atributos em json
    def json(self):
        return {
            "id":self.id,
            "ano":self.ano,
            "semestre":self.semestre,
        }
