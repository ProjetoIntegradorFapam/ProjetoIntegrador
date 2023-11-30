def select_users(cpf):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    if cpf:
        #comando a ser utilizado
        command = f'SELECT cpf, nome, permissao_id FROM usuario where cpf = "{cpf}"'
    else:
        #comando a ser utilizado
        command = f'SELECT cpf, nome, permissao_id FROM usuario'

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

def select_nutrition(cpf):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    #comando a ser utilizado
    command = f'SELECT nome FROM usuario WHERE cpf = "{cpf}"'

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

    #tratando verificação de dados
    if len(response) == 0:
        return False
    else:
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

def insert_clinic(cnpj, razao_social, rua, numero, bairro, cidade, celular, telefone, email):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cnpj from empresa where cnpj = '{cnpj}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if len(response) != 0:
        return False
    else:
        command = f'INSERT INTO empresa (cnpj, razao_social, rua, numero, bairro, cidade, celular, telefone, email) values ("{cnpj}", "{razao_social}", "{rua}", {numero}, "{bairro}", "{cidade}","{celular}","{telefone}", "{email}")'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True

def insert_nutrition(cfn, cpf):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cfn from nutricionista where cfn = '{cfn}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if len(response) != 0:
        return False
    else:
        command = f'INSERT INTO nutricionista (cfn, cpf) values ("{cfn}", "{cpf}")'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True

def select_user_all(cpf):

    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    #comando a ser utilizado
    command = f'SELECT cpf, nome, rua, numero, bairro, cidade, celular, email, senha, permissao_id FROM usuario WHERE cpf = "{cpf}"' 

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

    #tratando verificação de dados
    if len(response) == 0:
        return False
    else:
        return response

def select_clinic_all(cnpj, razao_social, rua, numero, bairro, cidade, celular, telefone, email):
    
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    #comando a ser utilizado
    command = f'SELECT cnpj, razao_social, rua, numero, bairro, cidade, celular, telefone, email FROM empresa WHERE cnpj = "{cnpj}" and razao_social = "{razao_social}" and rua = "{rua}" and numero = {numero} and bairro = "{bairro}" and cidade = "{cidade}" and telefone = "{telefone}" and email = "{email}"'

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

    #tratando verificação de dados
    if len(response) == 0:
        return False
    else:
        return response

def update_user(cpf, rua, numero, bairro, cidade, celular, email):
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cpf from usuario where cpf = '{cpf}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if response:

        command = f'update usuario set rua = "{rua}", numero = {numero}, bairro = "{bairro}", cidade = "{cidade}", celular = "{celular}", email = "{email}" where cpf = "{cpf}"'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True
    else:
        return False

def update_clinic(cnpj, rua, numero, bairro, cidade, celular, telefone, email):
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cnpj from empresa where cnpj = '{cnpj}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if len(response) != 0:
        return False
    else:
        command = f'update empresa set rua = "{rua}", numero = {numero}, bairro = "{bairro}", cidade = "{cidade}", celular = "{celular}", telefone = "{telefone}", email = "{email}" where cnpj = "{cnpj}"'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True

def delete_user_db(cpf):

    from db.connection import db_connect

    try:
        connection = db_connect()
    
        #instanciando cursor
        cursor = connection.cursor()

        command = f'select cpf from usuario where cpf = "{cpf}"'
        cursor.execute(command)

        response = cursor.fetchall()

        if response:
            
            command = f'delete from usuario where cpf = "{cpf}"'
        
            cursor.execute(command)
            
            connection.commit()

            cursor.close()

            connection.close()

            return True
        else:
            return False
    except:
        return False

def select_alimentarPlan(cpf):

    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    #comando a ser utilizado
    command = f'SELECT cpf, titulo, descricao FROM plano_alimentar WHERE cpf = "{cpf}"'

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

    #tratando verificação de dados
    if len(response) == 0:
        return False
    else:
        return response

def insert_alimentarPlan(cpf, titulo, descricao):
        
    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()
    command = f'INSERT INTO plano_alimentar (cpf, titulo, descricao) values ("{cpf}", "{titulo}", "{descricao}")'

    cursor.execute(command)
    
    connection.commit()

    cursor.close()

    connection.close()

    return True

def update_alimentarPlan(cpf, descricao):

    from db.connection import db_connect

    connection = db_connect()
    
    #instanciando cursor
    cursor = connection.cursor()

    command = f"select cpf from plano_alimentar where cpf = '{cpf}'"
    cursor.execute(command)

    response = cursor.fetchall()

    if response:

        command = f'update plano_alimentar set descricao = "{descricao}" where cpf = "{cpf}"'
    
        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True
    else:
        return False

def delete_alimentarPlan(cpf):
    from db.connection import db_connect

    connection = db_connect()

    #instanciando cursor
    cursor = connection.cursor()

    command = f'select cpf from plano_aliemntar where cpf = "{cpf}"'
    cursor.execute(command)

    response = cursor.fetchall()

    if response:
        
        command = f'delete from plano_alimentar where cpf = "{cpf}"'

        cursor.execute(command)
        
        connection.commit()

        cursor.close()

        connection.close()

        return True
    else:
        return False 