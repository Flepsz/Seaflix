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
    sql = f"INSERT INTO usuarios(usuario, email, senha, plano, tipo, idade) \
    values ('{nome}','{email}','{senha}','{plano}','{tipo}', '{idade}')"
    cursor.execute(sql)
    conexao.commit()

    print("Usuário cadastrado com sucesso")


def criar_filmes():
    titulo = input("Título: ").title()
    plano = input("Digite o novo plano do usuário (Basic, Medium ou Premium): ").title()
    descricao = input("Descrição: ").title()
    classificacao = input('Digite a classificação do filme (em idade): ')

    sql = f"INSERT INTO filmes(filme, plano, descricao, class) \ 
    values ('{titulo}','{plano}','{descricao}','{classificacao}','{plan}')"

    cursor.execute(sql)
    conexao.commit()

    print("Filme registrado com sucesso")
