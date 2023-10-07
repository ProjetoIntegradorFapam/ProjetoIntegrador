#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template

#importanto conexão com banco de dados
from db import utils

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('home', __name__)

#Definindo rota "/home"
@bp.route('/home', methods=['GET'])
def home():

  #renderizando home e enviando os usuários do banco
  return render_template('home.html')

@bp.route('/editarperfil', methods=['GET'])
def editProfile():

  return render_template('edit_profile.html')
  