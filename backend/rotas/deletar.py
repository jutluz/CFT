from importacoes import *

@app.route("/")
def r_delete():
    return "Rotas para excluir."

# curl -X DELETE localhost:5000/remover/Pessoa/2 -H 'Authorization: Bearer TOKEN'
@app.route("/remover/<string:classe>/<int:id>", methods=['DELETE'])
@jwt_required()
def remover(classe: str, id: int):
    try:
        tchau = db.session.query(retornar_classe(classe)).filter_by(id = id).first()
        if tchau == None:
            raise Exception("Objeto não encontrado.")
        db.session.delete(tchau)
        db.session.commit()
        resposta = jsonify({"resultado": "ok", "detalhes": "Objeto removido com sucesso :) !"})
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Allow-Controll-Origin", "*")
    return resposta

def retornar_classe(classe: str):
    return {
        "Agenda": Agenda, "Aluno": Aluno, "Autor": Autor, "Instrumento": Instrumento, "Musica": Musica, "Pessoa": Pessoa, "Professor": Professor
    }[classe]