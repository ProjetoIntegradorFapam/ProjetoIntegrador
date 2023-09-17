def select_users():

    #importação do mysql
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

    #Utilize "cursor.fechtall()" para buscar dados.
    #cursor.fechtall()

    #armazenando dados do banco na variável response.
    response = cursor.fetchall()

    #encerrando cursor
    cursor.close()

    #encerrando conexão
    connection.close()

    #retornando dados da variável response
    return response

def select_user(cpf,senha):

    #importação do mysql
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
    command = f"select cpf,senha from usuario where cpf = '{cpf}' and senha = '{senha}'"

    #executando comando
    cursor.execute(command)

    #Utilize "connection.commit()" para editar banco
    #connection.commit()

    #Utilize "cursor.fetchall()" para buscar dados.
    #cursor.fetchall()

    #armazenando dados
    response = cursor.fetchall()

    #variável para retornar valor booleano em relação a validação dos dados
    validate = False

    #tratando verificação de dados
    if len(response) == 0:
        validate = False
    elif response[0][0] == cpf and response[0][1] == senha:
        validate = True
    else:
        validate = False

    #encerrando cursor
    cursor.close()

    #encerrando conexão
    connection.close()

    #retornando dados da variável response
    return validate