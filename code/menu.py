import inquirer
from create import criar_user, criar_filmes
from read import ler_filmes, ler_usuarios, login
from update import update_user, update_film
from delete import excluir_user, excluir_film


def menu():
    while True:
        questions = [
            inquirer.List('modes',
                          message="Menu",
                          choices=['Sair', 'Cadastrar Usuário', 'Entrar', 'Registrar Filme',
                                   'Listar', 'Atualizar', 'Excluir'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        modules = answers['modes']

        if modules == 'Sair':
            break

        elif modules == 'Cadastrar Usuário':
            criar_user()

        elif modules == 'Entrar':
            login()

        elif modules == 'Registrar Filme':
            criar_filmes()

        elif modules == 'Listar':
            listar = [
                inquirer.List('read',
                              message="Deseja listar o que?",
                              choices=['Usuários', 'Filmes'],
                              ),
            ]
            answers = inquirer.prompt(listar)
            read = answers['read']

            if read == 'Usuários':
                ler_usuarios()

            elif read == 'Filmes':
                ler_filmes()

        elif modules == 'Atualizar':
            update = [
                inquirer.List('updt',
                              message="Deseja atualizar o que?",
                              choices=['Usuários', 'Filmes'],
                              ),
            ]
            answers = inquirer.prompt(update)
            updt = answers['updt']

            if updt == 'Usuários':
                update_user()

            elif updt == 'Filmes':
                update_film()

        elif modules == 'Excluir':
            delete = [
                inquirer.List('dele',
                              message="Deseja atualizar o que?",
                              choices=['Usuários', 'Filmes'],
                              ),
            ]
            answers = inquirer.prompt(delete)
            dele = answers['dele']

            if dele == 'Usuários':
                excluir_user()

            if dele == 'Filmes':
                excluir_film()


menu()
