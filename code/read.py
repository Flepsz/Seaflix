import getpass
from mysql.connector.errors import Error
from connect import conexao

cursor = conexao.cursor()


def login():
    try:
        email = input("Digite seu e-mail: ")
        senha = getpass.getpass("Digite sua senha: ")

        sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        val = (email, senha)
        cursor.execute(sql, val)
        result = cursor.fetchone()

        if result:
            print("Login efetuado com sucesso")
        else:
            print("E-mail ou senha inválidos")

    except Error as e:
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def ler_usuarios():
    try:
        sql = 'SELECT * from usuarios'
        cursor.execute(sql)
        result = cursor.fetchall()

        id_width = 4
        nome_width = 20
        email_width = 25
        senha_width = 17
        plano_width = 20
        tipo_width = 18
        idade_width = 10

        header = f"|{'ID':^{id_width}}|{'NOME':^{nome_width}}|{'E-MAIL':^{email_width}}|" \
                 f"{'SENHA':^{senha_width}}|{'PLANO':^{plano_width}}|{'TIPO':^{tipo_width}}|{'IDADE':^{idade_width}}"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for usuarios in result:
            usuarios = f"|{usuarios[0]:^{id_width}}|{usuarios[1]:^{nome_width}}|{usuarios[2]:^{email_width}}|" \
                    f"{usuarios[3]:^{senha_width}}|{usuarios[4]:^{plano_width}}|{usuarios[5]:^{tipo_width}}|" \
                    f"{usuarios[6]:^{idade_width}}"
            print(usuarios)
        print("-" * len(header))

    except Error as e:
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def ler_filmes():
    try:
        sql = 'SELECT * from  filmes'
        cursor.execute(sql)
        linhas = cursor.fetchall()

        id_width = 4
        titulo_width = 40
        plano_width = 17
        descricao_width = 60
        classificacao_width = 18

        header = f"|{'ID':^{id_width}}|{'TÍTULO':^{titulo_width}}|{'PLANO':^{plano_width}}|" \
                 f"{'DESCRIÇÃO':^{descricao_width}}|{'CLASSIFICAÇÃO':^{classificacao_width}}|"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for linha in linhas:
            filmes = f"|{linha[0]:^{id_width}}|{linha[1]:^{titulo_width}}|{linha[2]:^{plano_width}}|" \
                     f"{linha[3]:^{descricao_width}}|{linha[4]:^{classificacao_width}}|"
            print(filmes)
        print("-" * len(header))

    except Error as e:
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
