import inquirer
from connect import conexao

cursor = conexao.cursor()


def update_user():
    email = input("Digite o e-mail com permissão para atualizar o usuário: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para atualizar esse usuário.")
    else:
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        questions = [
            inquirer.List('planos',
                          message="Escolha um plano",
                          choices=['Basic', 'Medium', 'Premium'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        plano = answers['planos']

        sql = "UPDATE usuarios SET usuario = %s, idade = %s, plano = %s WHERE email = %s"
        val = (nome, idade, plano, email)
        cursor.execute(sql, val)
        conexao.commit()

        print("Usuário atualizado com sucesso")


def update_film():
    email = input("Digite o e-mail do usuário com permissão para atualizar filmes: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para atualizar filmes.")
    else:
        id_filme = input("Digite o id do filme a ser atualizado: ")
        filme = input("Digite o novo título do filme: ")
        questions = [
            inquirer.List('planos',
                          message="Escolha um plano",
                          choices=['Basic', 'Medium', 'Premium'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        plano = answers['planos']
        desc = input("Digite uma nova descrição para o filme: ")

        sql = "UPDATE filmes SET filme = %s, plano = %s, ano = %s, desc = %s WHERE id_filme = %s"
        val = (filme, plano, desc, id_filme)
        cursor.execute(sql, val)
        conexao.commit()

        print("Filme atualizado com sucesso")
