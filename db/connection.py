def db_connect():
    import pg8000
    try:
        connection = pg8000.connect(
            host='localhost',
            user='postgres',
            password='8072',
            database='clinica_nutricional'
        )
        return connection
    except Exception as e:
        print('Erro de conexão com o BD {}'.format(e))
        return None