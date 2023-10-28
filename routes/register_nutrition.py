#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for

#importando gerenciamento de autenticação do usuário
from routes.login import user

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_nutrition', __name__)

@bp.route('/register_nutrition', methods=['GET','POST'])
def render_nutrition():

    if user.isAuthenticated():

        if request.method == 'GET':
            return render_template('register_nutrition.html', title='Cadastro de nutricionista')
        else:
            
            cpf = str(request.form.get('cpf')).replace('.', '')
            cfn = str(request.form.get('cfn'))
            
            register_nutrition = utils.insert_nutrition(cfn, cpf)

            if register_nutrition == True:
                flash('Usuário cadastrado com sucesso!','success')
                return redirect(url_for('register_nutrition.render_nutrition'))
            else:
                flash('Não foi possível cadastrar o usuário!','error')
                return redirect(url_for('register_nutrition.render_nutrition'))
    else:
        return redirect('/login')

# Definir uma rota para a página inicial
@bp.route('/search_nutrition/<cpf>', methods=['GET'])
def search_nutrition(cpf):

    # Consultar o banco de dados para obter o nome do usuário
    nome = utils.select_nutrition(cpf)

    if nome:
        return jsonify({'nome': nome})
    else:
        return jsonify({'nome': 'Usuário não encontrado!'})

# @bp.route('/register_user', methods=['POST'])
# def insert_user():
