from geral.config import *
from modelo.autor import Autor

class Musica(db.Model):
    # criação da tabela
    __tablename__ = "musica"

    # colunas com os atributos pra tabela no SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable = False)
    
    # autor que fez a musica não pode ser nulo por conta da composição
    autor_id = db.Column(db.Integer, db.ForeignKey(Autor.id), nullable = False)
    autor = db.relationship("Autor")

    # função pra transformar os atributos em json
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "autor_id":self.autor_id,
            "autor":self.autor.json()
        }
