def db_connect():

    #importação do mysql
    import mysql.connector

    #instanciando conexão
    connection = mysql.connector.connect(
        host='localhost',
        user='postgres',
        password='123',
        dbname='clinica_nutricional'
    )

    if connection:
        return connection