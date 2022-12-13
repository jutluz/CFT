from geral.config import *
from modelo import *
from rotas import *

@app.route("/")
def padrao():
    return "Backend operando."

app.run(debug=True, host="0.0.0.0")
