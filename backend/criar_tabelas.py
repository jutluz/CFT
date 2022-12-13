from importacoes import *

# cada vez que rodar esse arquivo as tabelas serão restauradas, então para preencher as tabelas vá para "teste_classes"
if __name__ == "__main__":
    db.drop_all()
    print("Tabelas excluídas")
    
    db.create_all()
    print("Tabelas criadas")
