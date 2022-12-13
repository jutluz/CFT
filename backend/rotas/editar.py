from importacoes import *
from geral.cripto import *

@app.route("/")
def r_edit():
    return "Rotas para editar."

# curl -X PUT localhost:5000/editar/Instrumento/3 -H "Content-Type:application/json" -d '{"nome":"Violao Editado", "turma_id":2}' -H 'Authorization: Bearer TOKEN'
# curl -X PUT localhost:5000/editar/Pessoa/1 -H "Content-Type:application/json" -d '{"senha":"Teste"}'
@app.route("/editar/<string:classe>/<int:id>", methods=['PUT'])
@jwt_required()
def editar(classe: str, id: int):
    try:
        dados = request.get_json()
        #print (dados)
        if classe == "Pessoa":
            dados["senha"] = cifrar(dados["senha"])
            Pessoa.query.filter_by(id = id).update(dados)
            nome_classe = ("Pessoa")
        elif classe == "Agenda":
            Agenda.query.filter_by(id = id).update(dados)
            nome_classe = ("Agenda")
        elif classe == "Turma":
            Turma.query.filter_by(id = id).update(dados)
            nome_classe = ("Turma")
        elif classe == "Instrumento":
            Instrumento.query.filter_by(id = id).update(dados)
            nome_classe = ("Instrumento")
        elif classe == "Autor":
            Autor.query.filter_by(id = id).update(dados)
            nome_classe = ("Autor")
        elif classe == "Musica":
            Musica.query.filter_by(id = id).update(dados)
            nome_classe = ("Musica")
        elif classe == "Aluno":
            #print (dados)
            aluno = Aluno.query.filter_by(id = id).first()
            aluno.nome = dados["nome"]
            aluno.email = dados["email"]
            aluno.turma_id = dados["turma_id"]
            aluno.senha = cifrar(dados["senha"])
            nome_classe = ("Aluno")
        elif classe == "Professor":
            professor = Professor.query.filter_by(id = id).first()
            professor.nome = dados["nome"]
            professor.email = dados["email"]
            professor.turma_id = dados["turma_id"]
            professor.salario = dados["salario"]
            professor.senha = cifrar(dados["senha"])
            nome_classe = ("Professor")
        else:
            raise Exception("Classe não encontrada.")
        db.session.commit()
        resposta = jsonify({"resultado": "ok", "detalhes": nome_classe+" editado(a) com sucesso!"})
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Allow-Controll-Origin", "*")
    return resposta