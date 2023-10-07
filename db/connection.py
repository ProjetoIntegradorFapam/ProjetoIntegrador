def db_connect():

    #importação do mysql
    import mysql.connector

    #instanciando conexão
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='clinica_nutricional'
    )

    if connection:
        return connection