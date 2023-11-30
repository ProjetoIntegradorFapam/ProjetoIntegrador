#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, redirect, request, flash

#importando gerenciamento de autenticação do usuário
from routes.login import user

#importando utils
from db.utils import select_users, delete_user_db, select_alimentarPlan, insert_alimentarPlan, select_user_all

#instanciando "users" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('users', __name__)

#Definindo rota "/home"
@bp.route('/users', methods=['GET'])
def users():
    
  if user.isAuthenticated():

    cpf = request.args.get('cpf')

    users = select_users(cpf)
    print(users)
    #renderizando home e enviando os usuários do banco
    return render_template('users.html', title='Lista de Usuários', users=users)
  else:
    #redireciona para login
    return redirect('/login')

#Definindo rota "/delete_user"
@bp.route('/delete_user', methods=['GET'])
def delete_user():

  cpf = request.args.get('cpf')

  if delete_user_db(cpf):

    #mensagem flash
    flash('Usuário removido com sucesso!', 'success')
    #renderizando home e enviando os usuários do banco
    return redirect('/users')
  else:
    #mensagem flash
    flash('Não foi possível remover o usuário!', 'error')
    return redirect('/users')

#Definindo rota "/alimentar_plan"
@bp.route('/alimentar_plan/<cpf>', methods=['GET'])
def alimentar_plan(cpf):

  if user.isAuthenticated():

    _user = select_user_all(cpf)
    plans = select_alimentarPlan(cpf)

    return render_template('alimentar_plan.html', title='Plano alimentar', alimentar_plan=plans, user=_user)
  else:
    return redirect('/login')

#definindo rota "cadastrar/plano_alimentar"
@bp.route('/cadastrar/plano_alimentar/<cpf>', methods=['GET'])
def cadastrar_plano_get(cpf):

  if user.isAuthenticated():
    _user = select_user_all(cpf)
    return render_template('alimentar_plan_form.html', title='Cadastrar plano', user=_user)
  else:
    return redirect('/login')

@bp.route('/cadastrar/plano_alimentar', methods=['POST'])
def cadastrar_plano_post():

  cpf = request.form.get('_cpf')
  titulo = request.form.get('titulo')
  descricao = request.form.get('descricao')

  insert_plan = insert_alimentarPlan(cpf, titulo, descricao)

  if insert_plan:
    flash('Plano cadastrado com suceso!', 'success')
    return redirect(f"/alimentar_plan/{cpf}")
  else:
    flash('Não foi possível cadastrar esse plano!', 'error')
    return redirect(f"/alimentar_plan/{cpf}")