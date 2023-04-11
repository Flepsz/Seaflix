import getpass
from connect import conexao

cursor = conexao.cursor()


def criar_user(nome, idade, email, plano, tipo):
    nome = input('Digite seu nome: ')
    idade = int(input("Digite sua idade: "))
    email = input('Digite seu E-mail: ')
    senha = getpass.getpass("Digite sua senha: ")
    plano = input("Digite o novo plano do usuário (Basic, Medium ou Premium): ").title()
    tipo = input("Escolha seu tipo de Usuário (User ou Admin): ")
    sql = "INSERT INTO usuarios(usuario, email, senha, plano, tipo, idade) values (%s, %s, %s, %s, %s, %s)"
    val = (nome, email, senha, plano, tipo, idade)
    cursor.execute(sql, val)
    conexao.commit()

    print("Usuário cadastrado com sucesso")


def criar_filmes():
    titulo = input("Título: ").title()
    plano = input("Digite o novo plano do usuário (Basic, Medium ou Premium): ").title()
    descricao = input("Descrição: ").title()
    classficacao = input('Digite a classificação do filme (em idade): ')

    sql = "INSERT INTO filmes(filme, plano, descricao, class) values (%s, %s, %s, %s)"
    valores = (titulo, plano, descricao, classficacao)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Filme registrado com sucesso")
