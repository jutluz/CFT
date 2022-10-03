from geral.config import *
from modelo.pessoa import *
from modelo.professor import *
from modelo.aluno import *
from modelo.turma import *
from modelo.instrumento import *
from modelo.agenda import *

def addAgendaTurmaInstrumentoPessoa():
    #adicionando agendas
    ag1 = Agenda(dia_semana = "segunda-feira", horario = 13.30)
    db.session.add(ag1)
    db.session.commit()

    ag2 = Agenda(dia_semana = "terça-feira", horario = 14.15)
    db.session.add(ag2)
    db.session.commit()

    print("Agendas adicionadas")

    #adicionando turmas e instrumentos
    t1 = Turma(ano = "2021", semestre = "2", agenda = ag1)
    db.session.add(t1)
    db.session.commit()

    i1 = Instrumento(nome = "Flauta", turma = t1)
    db.session.add(i1)
    db.session.commit()

    i2 = Instrumento(nome = "Piano", turma = t1)
    db.session.add(i2)
    db.session.commit()

    t2 = Turma(ano = "2022", semestre = "1", agenda = ag2)
    db.session.add(t2)
    db.session.commit()

    i3 = Instrumento(nome = "Violão", turma = t2)
    db.session.add(i3)
    db.session.commit()

    i4 = Instrumento(nome = "Guitarra", turma = t2)
    db.session.add(i4)
    db.session.commit()

    print("Turma adicionada com seus instrumentos")

    #adicionando professores
    p1 = Professor(nome = "Laura", email = "lauraprof@gmail.com", turma = t1, senha = "lauraprof123", salario = 2000.5)
    p2 = Professor(nome = "Jorge", email = "jorgeprof@gmail.com", turma = t2, senha = "jorgeprof123", salario = 2000)
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print("Professores adicionados")

    #adicionando alunos
    a1 = Aluno(nome = "Catarina", email = "catarinaaluna@gmail.com", turma = t1, senha = "cata123")
    a2 = Aluno(nome = "Fernanda", email = "fernandaaluna@gmail.com", turma = t1, senha = "fefe123")
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
    print("Alunos da turma 1 adicionados")

    a3 = Aluno(nome = "Patolino", email = "patolino@gmail.com", turma = t2, senha = "patolinosenha")
    a4 = Aluno(nome = "Pocoyo", email = "pocoyo@gmail.com", turma = t2, senha = "pocoyo321")
    db.session.add(a3)
    db.session.add(a4)
    db.session.commit()
    print("Alunos da turma 2 adicionados")

    #mostrando a lista reversa

    print("\n", "Turma 1: ", t1.json(), "\n", "Instrumento 1: ", i1.json(), "\n", "Instrumento 2: ", i2.json())
    print("\n", "Turma 2: ", t2.json(), "\n", "Instrumento 3: ", i3.json(), "\n", "Instrumento 4: ", i4.json())

addAgendaTurmaInstrumentoPessoa()