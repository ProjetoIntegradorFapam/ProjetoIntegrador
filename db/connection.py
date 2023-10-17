def db_connect():
    import mysql.connector
    connection = mysql.connector.connect(
            host='localhost',
            user='postgres',
            password='8072',
            database='clinica_nutricional'
        )
    
    if connection:
        print('Banco de dados conectado com sucesso!')
        return connection