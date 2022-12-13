from importacoes import *
from geral.cripto import *

def addProfessor():
    #p1 = Professor(nome = "Laura", email = "lauraprof@gmail.com", senha = "lauraprof123")
    #p2 = Professor(nome = "Jorge", email = "jorgeprof@gmail.com", senha = "jorgeprof123")
    p3 = Professor(nome = "Akemi", email = "akemiprof@gmail.com", senha = cifrar("akemiprof123")) 
    #db.session.add(p1)
    #db.session.add(p2)
    db.session.add(p3)
    db.session.commit()
    #print(p1) - retorna <Professor 1>
    #print(p1.json()) - retorna {'idProf': 1, 'nomeProf': 'Laura', 'email': 'lauraprof@gmail.com', 'senha': 'lauraprof123'}
    #print(p1.json())
    print("Professores adicionados")

def addAluno():
    a1 = Aluno(nome = "Catarina", email = "catarinaaluna@gmail.com", senha = cifrar("cata123"))
    a2 = Aluno(nome = "Fernanda", email = "fernandaaluna@gmail.com", senha = cifrar("fefe123"))
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
    print("Alunos adicionados")

def addAutor():
    au1 = Autor(nome = "Gorillaz")
    au2 = Autor(nome = "Mac DeMarco")       
    db.session.add(au1)
    db.session.add(au2)
    db.session.commit()
    print("Autores adicionados")

#não tem como criar musica sem autor por conta da agregação de composição
def addMusicaAutor():
    au3 = Autor(nome = "Suki Waterhouse")
    m1 = Musica(nome = "My Good Looking Boy", autor=au3)
    db.session.add(au3)
    db.session.add(m1)
    db.session.commit()
    #print(m1.json())
    print("Musica e autor adicionados")

def addTurmaInstrumento():
    t1 = Turma(ano = "2022", semestre = "1")
    db.session.add(t1)
    db.session.commit()

    i1 = Instrumento(nome = "Flauta", turma = t1)
    db.session.add(i1)
    db.session.commit()

    i2 = Instrumento(nome = "Piano", turma = t1)
    db.session.add(i2)
    db.session.commit()

    #print(t1.json(), i1.json(), i2.json())

    print("Turma adicionada com seus instrumentos")

def addAgendaTurmaInstrumentoPessoa():
    ag1 = Agenda(dia_semana = "segunda-feira")
    # horario = time(13,30,00)
    db.session.add(ag1)
    db.session.commit()

    ag2 = Agenda(dia_semana = "quarta-feira")
    # horario = time(13,30,00)
    db.session.add(ag2)
    db.session.commit()
    
    ''' %H: 24 horas (00 até 23)
        %I: 12 horas (01 até 12)
        %M: minutos (01 até 59)'''

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

    i3 = Instrumento(nome = "Violao", turma = t2)
    db.session.add(i3)
    db.session.commit()

    i4 = Instrumento(nome = "Guitarra", turma = t2)
    db.session.add(i4)
    db.session.commit()

    print("Turma adicionada com seus instrumentos")

    p1 = Professor(nome = "Laura", email = "lauraprof@gmail.com", turma = t1, senha = cifrar("lauraprof123"), salario = 2000.50)
    p2 = Professor(nome = "Jorge", email = "jorgeprof@gmail.com", turma = t2, senha = cifrar("jorgeprof123"), salario = 2000) 
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print("Professores adicionados")

    a1 = Aluno(nome = "Catarina", email = "catarinaaluna@gmail.com", turma = t1, senha = cifrar("cata123"))
    a2 = Aluno(nome = "Fernanda", email = "fernandaaluna@gmail.com", turma = t1, senha = cifrar("fefe123"))
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
    print("Alunos da turma 1 adicionados")

    a3 = Aluno(nome = "Patolino", email = "patolino@gmail.com", turma = t2, senha = cifrar("patolinosenha"))
    a4 = Aluno(nome = "Pocoyo", email = "pocoyo@gmail.com", turma = t2, senha = cifrar("pocoyo321"))
    db.session.add(a3)
    db.session.add(a4)
    db.session.commit()
    print("Alunos da turma 2 adicionados")

    

    '''
    print("Turma e seus instrumentos: ", t1.json())
    print("Objeto <Instrumento 1>: ", i1.json())
    print("Objeto <Instrumento 2>: ", i2.json())

    o comando acima imprime:

    Turma e seus instrumentos:  {'id': 1, 'ano': 2021, 'semestre': 2, 'instrumentos': [<Instrumento 1>, <Instrumento 2>], 'agenda_id': 1, 'agenda': {'id': 1, 'dia_semana': 'segunda-feira', 'horario': 13.3}}
    Objeto <Instrumento 1>:  {'id': 1, 'nome': 'Flauta', 'turma_id': 1}
    Objeto <Instrumento 2>:  {'id': 2, 'nome': 'Piano', 'turma_id': 1}
    
    
    print("Turma e seus instrumentos: ", t2.json(), "\n", i3.json(), "\n", i4.json())
    '''

#addProfessor()
#addAluno()
addAutor()
addMusicaAutor()
#addTurmaInstrumento()
addAgendaTurmaInstrumentoPessoa() 
