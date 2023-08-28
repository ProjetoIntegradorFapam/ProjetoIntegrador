def select():

    #importação do driver mysql
    import mysql.connector

    #instanciando conexão
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_integrador'
    )

    #instanciando cursor
    cursor = connection.cursor()

    #comando a ser utilizado
    command = 'SELECT * FROM usuario'

    #executando comando
    cursor.execute(command)

    #Utilize "connection.commit()" para editar banco
    #connection.commit()

    #Utilize "cursor.fechtall()" para buscar dados e adicionando á lista response
    response = cursor.fetchall()

    #encerrando cursor
    cursor.close()

    #encerrando conexão
    connection.close()

    return response