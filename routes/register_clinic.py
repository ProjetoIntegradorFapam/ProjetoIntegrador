from flask import Blueprint, render_template, request, redirect, url_for, flash

#importando gerenciamento de autenticação do usuário
from routes.login import user

from db import utils

bp = Blueprint('register_clinic', __name__)

@bp.route('/register_clinic', methods=['GET','POST'])
def render_user():

    if user.isAuthenticated():
        if request.method == 'GET':
            return render_template('register_clinic.html')
        else:
            cnpj = str(request.form.get('cnpj')).replace(".","")
            cnpj = cnpj.replace("/","")
            cnpj = cnpj.replace("-","")
            razao_social = str(request.form.get('razao_social'))
            rua = str(request.form.get('rua'))
            numero = str(request.form.get('numero'))
            bairro = str(request.form.get('bairro'))
            cidade = str(request.form.get('cidade'))
            celular = str(request.form.get('celular')).replace("(","")
            celular = celular.replace(")","")
            celular = celular.replace(" ","")
            celular = celular.replace("-","")
            telefone = str(request.form.get('telefone')).replace("(","")
            telefone = telefone.replace(")","")
            telefone = telefone.replace(" ","")
            telefone = telefone.replace("-","")
            email = str(request.form.get('email'))


            register_clinic = utils.insert_clinic(cnpj, razao_social, rua, numero, bairro, cidade, celular, telefone, email)

            if register_clinic == True:
                flash('Empresa cadastrada com sucesso!', 'success')
                return redirect('/register_clinic')
            else:
                flash('Não foi possível cadastrar a empresa!', 'error')
                return redirect('/register_clinic')
    else:
        return redirect('/login')