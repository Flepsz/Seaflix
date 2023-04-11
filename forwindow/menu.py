from create import criar_user, criar_filmes
from read import ler_filmes, ler_usuarios, login
from update import update_user, update_film
from delete import excluir_user, excluir_film


def menu():
    while True:
        print("Selecione uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Entrar")
        print("3 - Registrar filme")
        print("4 - Listar filmes")
        print("5 - Listar usuários")
        print("6 - Atualizar usuário")
        print("7 - Excluir usuário")
        print("8 - Atualizar filme")
        print("9 - Excluir filme")
        print("0 - Sair")

        modules = input("Opção selecionada: ")

        if modules == '0':
            break

        elif modules == '1':
            criar_user()

        elif modules == '2':
            login()

        elif modules == '3':
            criar_filmes()

        elif modules == '4':
            ler_filmes()

        elif modules == '5':
            ler_usuarios()

        elif modules == '6':
            update_user()

        elif modules == '7':
            excluir_user()

        elif modules == '8':
            update_film()

        elif modules == '9':
            excluir_film()


menu()
