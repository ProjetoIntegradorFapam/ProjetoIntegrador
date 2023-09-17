#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template

#importanto conexão com banco de dados
from db import connection

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('home', __name__)

#Definindo rota "/home"
@bp.route('/home', methods=['GET'])
def login():

  #renderizando home e enviando os usuários do banco
  return render_template('home.html', users=connection.select_users())
  