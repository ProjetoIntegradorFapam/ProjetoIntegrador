#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, redirect, url_for, flash

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('register_nutrition', __name__)

@bp.route('/register_nutrition', methods=['GET','POST'])
def render_nutrition():
    return render_template('register_nutrition.html')

# @bp.route('/register_user', methods=['POST'])
# def insert_user():
