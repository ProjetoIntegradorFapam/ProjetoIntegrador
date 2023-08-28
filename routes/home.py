#importando bibliotecas, frameworks e microframeworks
#o microframework blueprint é responsável por criar uma coleção de views, ou seja, rotas separadas.
from flask import Blueprint, render_template

#importando função para buscar usuários
from db import users

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('home', __name__)

#Definindo rota "/home"
@bp.route('/home', methods=['GET'])
def login():

  #renderizando home e enviando os usuários do banco
  return render_template('home.html', users=users.select())
  