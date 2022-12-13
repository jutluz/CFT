from importacoes import *
from geral.cripto import *

@app.route("/")
def r_login():
    return "Rota padrão de login"

@app.route("/teste", methods = ["GET"])
def teste():
    print("Funcioando")
    resposta = ("Funcionando")
    return resposta

# curl -X POST localhost:5000/login -d '{"login":"catarinaaluna@gmail.com","senha":"cata123"}' -H 'Content-Type: application/json'
@app.route("/login", methods=['POST'])
def login():
    dados = request.get_json(force=True) # requisita os dados

    login = dados['login']
    senha = dados['senha']
    
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    
    if encontrado is None: 
        resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})
    else:
        access_token = create_access_token(identity=login)
        resposta = jsonify({"resultado":"ok", "detalhes": access_token}) 
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# curl -X POST localhost:5000/login -d '{"login":"catarinaaluna@gmail.com","senha":"cata123"}' -H 'Content-Type: application/json'
@app.route("/cadastro/<string:classe>", methods=['POST'])
def cadastro(classe: str):
    dados = request.get_json(force=True) # requisita os dados
    try:
        if classe == "Aluno":
            dados["senha"] = cifrar(dados["senha"]) # cifra a senha fornecida
            novo = Aluno(**dados)                   # cria o objeto 'novo' de aluno na classe
        elif classe == "Professor":
            dados["senha"] = cifrar(dados["senha"])
            novo = Professor(**dados) 
        else:
            raise Exception("Classe não encontrada.")
        
        db.session.add(novo) # insere a pessoa, mesma função do "insert into" do MySQL
        db.session.commit()  # persiste a inclusão
        access_token = create_access_token(identity=dados["email"])
        resposta = jsonify({"resultado":"ok", "detalhes": access_token}) 
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)}) # retorno de resposta negativa
    
    resposta.headers.add("Access-Allow-Controll-Origin", "*")         # dá acesso à resposta
    return resposta