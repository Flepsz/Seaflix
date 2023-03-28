import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="seaflix"
    )

    if conexao.is_connected():
        print("Conectado ao banco de dados MySQL!")
except:
    print("Falha na conexão")
