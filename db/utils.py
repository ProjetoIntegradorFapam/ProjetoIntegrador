def select_users():
    
    from db.connection import db_connect

    connection = db_connect()
    
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

    from db.connection import db_connect

    connection = db_connect()

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

def insert_user(cpf, nome, rua, numero, bairro, cidade, celular, email, permissao_id, senha):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cpf from usuario where cpf = '{cpf}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if len(response) != 0:
        return False
    else:
        command = f'INSERT INTO usuario (cpf, nome, rua, numero, bairro, cidade, celular, email, permissao_id, senha) values ("{cpf}", "{nome}", "{rua}", {numero}, "{bairro}", "{cidade}", "{celular}", "{email}", {permissao_id}, "{senha}")'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True