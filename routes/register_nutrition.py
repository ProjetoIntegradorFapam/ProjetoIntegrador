#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, jsonify

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_nutrition', __name__)

@bp.route('/register_nutrition', methods=['GET','POST'])
def render_nutrition():
    return render_template('register_nutrition.html')

# Definir uma rota para a página inicial
@bp.route('/search_nutrition/<cpf>', methods=['GET'])
def search_nutrition(cpf):

    # Consultar o banco de dados para obter o nome do usuário
    nome = utils.select_nutrition(cpf)

    if nome:
        return jsonify({'nome': nome})
    else:
        return jsonify({'nome': 'Usuário não encontrado!'})

# @bp.route('/register_user', methods=['POST'])
# def insert_user():
