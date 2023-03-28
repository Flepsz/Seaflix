import inquirer
from create import criar_user, criar_filmes
from read import ler_filmes, login


def menu():
    while True:
        questions = [
            inquirer.List('modes',
                          message="Menu",
                          choices=['Sair', 'Cadastrar', 'Entrar', 'Registrar filme', 'Lista filmes'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        modules = answers['modes']

        if modules == 'Sair':
            break

        elif modules == 'Cadastrar Usuários':
            criar_user()

        elif modules == 'Entrar':
            login()

        elif modules == 'Registrar Filme':
            criar_filmes()

        elif modules == 'Lista Filmes':
            ler_filmes()


menu()
