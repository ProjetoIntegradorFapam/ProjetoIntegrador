#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, redirect, request, flash

#importando gerenciamento de autenticação do usuário
from routes.login import user

#importando função utils
from db import utils

#instanciando "edit_user" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('edit_user', __name__)

#Definindo rota "/edit_user"
@bp.route('/edit_user/<cpf>', methods=['GET','POST'])
def edit_user(cpf):

    user = utils.select_user_all(cpf)

    if request.method == 'GET':

        return render_template('edit_user.html', title='Editar usuário', user=user)
    else:

        rua = str(request.form.get('rua'))
        numero = str(request.form.get('numero'))
        bairro = str(request.form.get('bairro'))
        cidade = str(request.form.get('cidade'))
        celular = str(request.form.get('celular')).replace('(','')
        email = str(request.form.get('email'))
        #Celular sem máscar
        celular = celular.replace(')', '')
        celular = celular.replace(' ','')
        celular = celular.replace('-','')

        if utils.update_user(cpf, rua, numero, bairro, cidade, celular, email):
            flash('Dados do usuário atualizado com sucesso!','success')
            return redirect('/users')
        else :
            flash('Não foi possível atualizar os dados do usuário!','error')
            return render_template('edit_user.html', title='Editar usuário', user=user)