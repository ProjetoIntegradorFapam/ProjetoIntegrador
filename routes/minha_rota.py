#importando bibliotecas, frameworks e microframeworks
#o microframework blueprint é responsável por criar uma coleção de views, ou seja, rotas separadas.
from flask import Blueprint, render_template

#instanciando "minha_rota" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('minha_rota', __name__)

#Definindo rota "minha_rota"
@bp.route('/minha_rota')
def minha_rota():
    return render_template('index.html')