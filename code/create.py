import inquirer
import getpass
from connect import conexao

cursor = conexao.cursor()


def criar_user():
    nome = input('Digite seu nome: ')
    idade = int(input("Digite sua idade: "))
    email = input('Digite seu E-mail: ')
    senha = getpass.getpass("Digite sua senha: ")
    questions = [
        inquirer.List('planos',
                      message="Escolha um plano",
                      choices=['Basic', 'Medium', 'Premium'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    plano = answers['planos']
    questions2 = [
        inquirer.List('tipos',
                      message="Escolha seu tipo de Usuário",
                      choices=['User', 'Admin'],
                      ),
    ]
    answers = inquirer.prompt(questions2)
    tipo = answers['tipos']
    sql = "INSERT INTO usuarios(usuario, email, senha, plano, tipo, idade) values (%s, %s, %s, %s, %s, %s)"
    val = (nome, email, senha, plano, tipo, idade)
    cursor.execute(sql, val)
    conexao.commit()

    print("Usuário cadastrado com sucesso")


def criar_filmes():
    titulo = input("Título: ").title()
    questions = [
        inquirer.List('planos',
                      message="Escolha um plano",
                      choices=['Basic', 'Medium', 'Premium'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    plano = answers['planos']
    descricao = input("Descrição: ").title()
    questions1 = [
        inquirer.List('class',
                      message="Escolha a classificação do filme",
                      choices=['0', '10', '12', '14', '16', '18'],
                      ),
    ]
    answers = inquirer.prompt(questions1)
    classficacao = str(answers['class'])

    sql = "INSERT INTO filmes(filme, plano, descricao, class) values (%s, %s, %s, %s)"
    valores = (titulo, plano, descricao, classficacao)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Filme registrado com sucesso")
