from geral.config import *

class Agenda(db.Model):
    # criação da tabela
    __tablename__ = "agenda"

    # atributos da agenda
    id = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.String(100), nullable = False)
    # horario = db.Column(db.Time, nullable = False)

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "dia_semana": self.dia_semana,
            # "horario": self.horario
        }
