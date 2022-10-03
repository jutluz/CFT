from geral.config import *
from modelo.professor import *
from modelo.aluno import *
from modelo.pessoa import *
from modelo.turma import *
from modelo.instrumento import *
from modelo.agenda import *

if __name__ == "__main__":
    #db.drop_all()
    #print("Tabelas excluídas")
    
    db.create_all()
    print("Tabelas criadas")