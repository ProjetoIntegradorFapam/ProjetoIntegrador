#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_user', __name__)

@bp.route('/register_user', methods=['GET'])
def render_user():
    return render_template('register_user.html')

# @bp.route('/register_user', methods=['POST'])
# def insert_user():