from geral.config import *
from modelo.professor import *
from modelo.aluno import *
from modelo.pessoa import *

@app.route("/")
def inicio():
    return "Rota padrão - OK."