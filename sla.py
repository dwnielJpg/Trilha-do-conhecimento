# sla.py

def criar_pessoa(id, nome, idade, email):
    comando_sql = f"INSERT INTO Pessoa (ID, Nome, Idade, Email) VALUES ({id}, '{nome}', {idade}, '{email}');"
    with open("sql.txt", "a") as arquivo_sql:
        arquivo_sql.write(comando_sql + "\n")

def editar_pessoa(id, nome, idade, email):
    comando_sql = f"UPDATE Pessoa SET Nome = '{nome}', Idade = {idade}, Email = '{email}' WHERE ID = {id};"
    with open("sql.txt", "a") as arquivo_sql:
        arquivo_sql.write(comando_sql + "\n")

def remover_pessoa(id):
    comando_sql = f"DELETE FROM Pessoa WHERE ID = {id};"
    with open("sql.txt", "a") as arquivo_sql:
        arquivo_sql.write(comando_sql + "\n")
