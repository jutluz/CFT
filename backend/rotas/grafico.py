from importacoes import *

@app.route("/obter_dados_prof")
def criar_tabelas():
    dados = {
        "x": [professor.nome for professor in db.session.query(Professor).all()],
        "y": [professor.salario for professor in db.session.query(Professor).all()],
        "type": "bar"
    }
    retorno = {"resultado":"ok"}
    retorno.update({"detalhes":dados}); #coloca os dados no retorno
    resposta = jsonify(retorno)         #cria a variavel resposta que recebe o retorno jasonificado
    resposta.headers.add("Access-Control-Allow-Origin", "*") #permissão
    print(dados)                        
    return resposta