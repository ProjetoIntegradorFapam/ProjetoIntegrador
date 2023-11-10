#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, redirect

#importando gerenciamento de autenticação do usuário
from routes.login import user

#importando utils
from db.utils import select_users

#instanciando "users" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('users', __name__)

#Definindo rota "/home"
@bp.route('/users', methods=['GET'])
def users():
    
  if user.isAuthenticated():

    users = select_users()

    #renderizando home e enviando os usuários do banco
    return render_template('users.html', title='Lista de Usuários', users=users)
  else:
    #redireciona para login
    return redirect('/login')

