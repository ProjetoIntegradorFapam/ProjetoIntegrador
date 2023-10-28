#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, redirect

#importando gerenciamento de autenticação do usuário
from routes.login import user

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('home', __name__)

#Definindo rota "/home"
@bp.route('/home', methods=['GET'])
def home():
    
  if user.isAuthenticated():

    #renderizando home e enviando os usuários do banco
    return render_template('home.html')
  else:
    #redireciona para login
    return redirect('/login')