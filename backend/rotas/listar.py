from importacoes import *

@app.route("/")
def r_list():
    return "Rotas para listar."

# curl localhost:5000/listar/Pessoa -H 'Authorization: Bearer TOKEN'
@app.route("/listar/<string:classe>", methods=['GET'])
def listar(classe: str):
    try:
        objetos = db.session.query(retornar_classe(classe)).all()
        if objetos == None:
            raise Exception("CLasse não encontrada.")
        objetos_em_json = [x.json() for x in objetos] # percorre cada objeto da classe e transforma em json
        resposta = jsonify(objetos_em_json)           # retorno da lista
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Allow-Controll-Origin", "*")
    return resposta

def retornar_classe(classe: str):
    return {
        "Agenda": Agenda, "Aluno": Aluno, "Autor": Autor, "Instrumento": Instrumento, "Musica": Musica, "Pessoa": Pessoa, "Professor": Professor, "Turma": Turma
    }[classe]