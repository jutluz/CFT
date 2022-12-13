from importacoes import *
from geral.cripto import *

@app.route("/")
def r_add():
    return "Um momento."

'''
Teste para adicionar aluno:
curl -d '{"nome":"Camila", "email":"camila@gmail.com", "senha":"camila123", "turma_id":1}' -X POST -H "Content-Type:application/json" localhost:5000/adicionar/Aluno -H 'Authorization: Bearer TOKEN'

Teste para adicionar professor:
curl -d '{"nome":"Polano", "email":"polanoprof@gmail.com", "senha":"polano123", "turma_id":2, "salario":2500}' -X POST -H "Content-Type:application/json" localhost:5000/adicionar/Professor

Teste para adicionar agenda:
curl -d '{"dia_semana": "sexta-feira"}' -X POST -H "Content-Type:application/json" localhost:5000/adicionar/Agenda

Teste para adicionar turma:
curl -d '{"ano": "2023", "semestre": 1, "agenda_id": "3"}' -X POST -H "Content-Type:application/json" localhost:5000/adicionar/Turma

Teste para adicionar instrumento:
curl -d '{"nome":"Violoncelo", "turma_id":2}' -X POST -H "Content-Type:application/json" localhost:5000/adicionar/Instrumento
'''

@app.route("/adicionar/<string:classe>", methods=['POST'])
@jwt_required()
def adicionar(classe: str):
    try:
        dados = request.get_json() # requisita os dados em formato json e guarda na variável 'novo'
        if classe == "Aluno":
            dados["senha"] = cifrar(dados["senha"]) # cifra a senha fornecida
            novo = Aluno(**dados)                   # cria o objeto 'novo' de aluno na classe
            nome_classe = ("Aluno")
        elif classe == "Professor":
            dados["senha"] = cifrar(dados["senha"])
            novo = Professor(**dados)
            nome_classe = ("Professor")
        elif classe == "Agenda":
            novo = Agenda(**dados)
            nome_classe = ("Agenda")
        elif classe == "Turma":
            novo = Turma(**dados)
            nome_classe = ("Turma")
        elif classe == "Instrumento":
            novo = Instrumento(**dados)
            nome_classe = ("Instrumento")
        elif classe == "Autor":
            novo = Autor(**dados)
            nome_classe = ("Autor")
        elif classe == "Musica":
            novo = Musica(**dados)
            nome_classe = ("Musica")
        else:
            raise Exception("Classe não encontrada.")
        db.session.add(novo) # insere a pessoa, mesma função do "insert into" do MySQL
        db.session.commit()  # persiste a inclusão
        resposta = jsonify({"resultado": "ok", "detalhes": nome_classe+" add com sucesso!"}) # retorno de resposta positiva
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)}) # retorno de resposta negativa
    resposta.headers.add("Access-Allow-Controll-Origin", "*")         # dá acesso à resposta
    return resposta


'''
Rota alternativa de adição, porém, sem tratamento de dados (tipo a senha)

curl -d '{"nome":"Sol", "email":"sol@gmail.com", "senha":"wde23", "turma_id":2}' -X POST -H "Content-Type:application/json" localhost:5000/add/Aluno
@app.route("/add/<string:classe>", methods=['POST'])
def add(classe: str):
    try:
        dados = request.get_json()
        novo = retornar_classe(classe)(**dados)
        db.session.add(novo)
        db.session.commit()
        resposta = jsonify(
            {"resultado": "ok", "detalhes": " add com sucesso!"})
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Allow-Controll-Origin", "*")
    return resposta

def retornar_classe(classe: str):
    return {
        "Agenda": Agenda, "Aluno": Aluno, "Autor": Autor, "Instrumento": Instrumento, "Musica": Musica, "Professor": Professor, "Turma": Turma
    }[classe]
'''