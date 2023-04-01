import inquirer
from create import criar_user, criar_filmes
from read import ler_filmes, ler_usuarios, login
from connect import conexao


def menu():
    while True:
        questions = [
            inquirer.List('modes',
                          message="Menu",
                          choices=['Sair', 'Cadastrar Usuário', 'Entrar', 'Registrar Filme', 'Listar Filmes',
                                   'Listar Usuários'],
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

        elif modules == 'Listar Filmes':
            ler_filmes()

        elif modules == 'Listar Usuários':
            cursor = conexao.cursor()
            sql = "SELECT tipo FROM usuarios WHERE email = %s"
            email = input("Digite o e-mail do usuário com permissão para listar: ")
            val = (email,)
            cursor.execute(sql, val)
            tipo_usuario = cursor.fetchone()[0]

            if tipo_usuario == "Admin":
                ler_usuarios()
            else:
                print("Acesso negado. Você não tem permissão para listar usuários.")


menu()
