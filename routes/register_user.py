#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, redirect, url_for, flash

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_user', __name__)

@bp.route('/register_user', methods=['GET','POST'])
def render_user():
    if request.method == 'GET':
        return render_template('register_user.html')
    else:
        cpf = str(request.form.get('cpf'))
        nome = str(request.form.get('nome'))
        rua = str(request.form.get('rua'))
        numero = str(request.form.get('numero'))
        bairro = str(request.form.get('bairro'))
        cidade = str(request.form.get('cidade'))
        celular = str(request.form.get('celular'))
        email = str(request.form.get('email'))
        permissao_id = str(request.form.get('permissao_id'))
        senha = str(request.form.get('senha'))

        utils.insert_user(cpf, nome, rua, numero, bairro, cidade, celular, email, int(permissao_id), senha)
        
        flash('Falha ao efetuar o login!')
        return redirect(url_for('home.home'))



# @bp.route('/register_user', methods=['POST'])
# def insert_user():
