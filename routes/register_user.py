#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, redirect, url_for, flash

#importanto conexão com banco de dados
from db import utils

#importando gerenciamento de autenticação do usuário
from routes.login import user

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_user', __name__)

@bp.route('/register_user', methods=['GET','POST'])
def render_user():

    if user.isAuthenticated():

        if request.method == 'GET':
            return render_template('register_user.html')
        else:
            cpf = str(request.form.get('cpf')).replace('.', '')
            nome = str(request.form.get('nome'))
            rua = str(request.form.get('rua'))
            numero = str(request.form.get('numero'))
            bairro = str(request.form.get('bairro'))
            cidade = str(request.form.get('cidade'))
            celular = str(request.form.get('celular')).replace('(','')
            email = str(request.form.get('email'))
            permissao_id = str(request.form.get('permissao_id'))
            senha = str(request.form.get('senha'))

            #Cpf sem máscara
            cpf = cpf.replace('-', '')
            #Celular sem máscar
            celular = celular.replace(')', '')
            celular = celular.replace(' ','')
            celular = celular.replace('-','')

            register_user = utils.insert_user(cpf, nome, rua, numero, bairro, cidade, celular, email, int(permissao_id), senha)

            if register_user == True:
                flash('Usuário cadastrado com sucesso!','success')
                return redirect(url_for('register_user.render_user'))
            else:
                flash('Não foi possível cadastrar o usuário!','error')
                return redirect(url_for('register_user.render_user'))
    else:
        return redirect('/login')
            
# @bp.route('/register_user', methods=['POST'])
# def insert_user():
