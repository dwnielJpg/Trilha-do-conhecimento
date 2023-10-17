# al.py
from sla import criar_pessoa, editar_pessoa, remover_pessoa

while True:
    condicao = "01" or "02"
    while condicao:
        print("Menu:\n[01]Criar uma nova Pessoa\n[02] Editar uma Pessoa\n[03] Remover uma Pessoa\n[04] Sair\n")

        escolha = int(input("Escolha uma opção (1/2/3/4): "))

        if escolha <= 0:
            print("Escolha uma opção valida.")
            condicao =  "01"

        if escolha >= 5:
            print("Escolha uma opção valida.")
            condicao = "02"
        if escolha == 1:
            id = input("ID da Pessoa: ")
            nome = input("Nome: ")
            idade = input("Idade: ")
            email = input("E-mail: ")
            criar_pessoa(id, nome, idade, email)

        elif escolha == 2:
            id = input("ID da Pessoa a ser editada: ")
            nome = input("Novo nome: ")
            idade = input("Nova idade: ")
            email = input("Novo e-mail: ")
            editar_pessoa(id, nome, idade, email)

        elif escolha == 3:
            id = input("ID da Pessoa a ser removida: ")
            remover_pessoa(id)

        elif escolha == 4:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
