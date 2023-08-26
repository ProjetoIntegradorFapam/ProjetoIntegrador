#importando bibliotecas, frameworks e microframeworks
#o microframework blueprint é responsável por criar uma coleção de views, ou seja, rotas separadas.
from flask import Blueprint, render_template

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('home', __name__)

#Definindo rota "/home"
@bp.route('/home', methods=['GET'])
def login():

  return render_template('home.html')
  