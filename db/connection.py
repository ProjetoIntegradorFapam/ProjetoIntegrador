def db_connect():
    import psycopg2
    connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='8072',
            database='clinica_nutricional'
        )
    
    if connection:
        return connection