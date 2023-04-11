from connect import conexao

cursor = conexao.cursor()


def excluir_user():
    email = input("Digite o e-mail com permissão para excluir o usuário: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para excluir esse usuário.")
    else:
        email = input("Digite o e-mail do usuário a ser excluído: ")
        sql = "DELETE FROM usuarios WHERE email = %s"
        val = (email,)
        cursor.execute(sql, val)
        conexao.commit()

        print("Usuário excluído com sucesso")


def excluir_film():
    email = input("Digite o e-mail com permissão para excluir o filme: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para excluir filmes.")
    else:
        id_filme = input("Digite o ID do filme a ser excluído: ")
        sql = "DELETE FROM filmes WHERE id_filme = %s"
        val = (id_filme,)
        cursor.execute(sql, val)
        conexao.commit()

        if cursor.rowcount == 0:
            print("Filme não encontrado")
        else:
            print("Filme excluído com sucesso")
