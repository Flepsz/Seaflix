from mysql.connector.errors import Error
import mysql.connector

try:
    conexao = mysql.connector.connect(host='localhost', database='netflix', user='root', password='')

    insert_filmes = """INSERT INTO filmes(filme, plano, descricao, class)
    values
    ('Lagoa Azul', 'premium', 'xxxxxxxx', 18),
    ('Homem-Aranha', 'medium', 'xxxxxxxx', 0)"""
    cursor = conexao.cursor()
    cursor.execute(insert_filmes)
    conexao.commit()

    sql = 'SELECT * from  filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()

    print('-'*20)
    for linha in linhas:
        print(linha[0], '\t')
        print(linha[1], '\t')
        print(linha[2], '\t')
        print(linha[3])
    print('-' * 20)

except Error as e:
    print(f'Erro: {e}')

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
