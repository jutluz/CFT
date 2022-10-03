from geral.config import *
from modelo import *
from rotas import *

@app.route("/")
def inicio():
    return "Backend operando."

app.run(debug=True)