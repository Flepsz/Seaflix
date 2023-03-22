import inquirer

cadastro = []
clientes = []
novo_usuario = []
cadastro_filme = []
filmes = []


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

        elif modules == 'Cadastrar':
            nome = input('Nome: ')
            cadastro.append(nome)
            email = input('Email: ')
            cadastro.append(email)
            questions = [
                inquirer.List('planos',
                              message="Escolha um plano",
                              choices=['basic', 'medium', 'premium'],
                              ),
            ]
            answers = inquirer.prompt(questions)
            planos = answers['planos']
            cadastro.append(planos)
            questions2 = [
                inquirer.List('tipos',
                              message="Escolha seu tipo de Usuário",
                              choices=['user', 'admin'],
                              ),
            ]
            answers = inquirer.prompt(questions2)
            tipo = answers['tipos']
            cadastro.append(tipo)
            clientes.append(cadastro[:])
            cadastro.clear()
            print(clientes)

        elif modules == 'Entrar':
            while True:
                novo_usuario.clear()
                if len(clientes) == 0:
                    print("Não há cadastros!")
                    break
                cliente = input('Nome: ')
                for i in range(len(clientes)):
                    if cliente == clientes[i][0]:
                        novo_usuario.append(clientes[i][0])
                        novo_usuario.append(clientes[i][1])
                        novo_usuario.append(clientes[i][2])
                        novo_usuario.append(clientes[i][3])
                        break
                else:
                    print("Cliente não encontrado.")
                    continue
                break
            print(novo_usuario)

        elif modules == 'Registrar filme':
            titulo = input("Título: ").title()
            cadastro_filme.append(titulo)
            questions = [
                inquirer.List('planos',
                              message="Escolha um plano",
                              choices=['basic', 'medium', 'premium'],
                              ),
            ]
            answers = inquirer.prompt(questions)
            planos = answers['planos']
            cadastro_filme.append(planos)
            filmes.append(cadastro_filme[:])
            cadastro_filme.clear()

        elif modules == 'Lista filmes':
            print(filmes)


menu()
