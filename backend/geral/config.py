#IMPORTAÇÕES
import os
from flask import Flask, jsonify, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_cors import CORS # permitir back receber dados do front

#CONFIGURAÇÕES
#cria a aplicação Flask
app = Flask(__name__)

#adiciona o Cors ao app (Flask)
CORS(app)

#pega a path (caminho) deste arquivo
path = os.path.dirname(os.path.abspath(__file__))

#cria o arquivo do banco de dados
arquivobd = os.path.join(path, 'data.db')

#configurações do sqlalchemy ()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#configurações da sessão
app.secret_key = 'kW0Ws9q9lg#jdE4WP7FmTTFBVk7EdY' #chave secreta
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) #adiciona a sessão ao app