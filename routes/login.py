#importando bibliotecas, frameworks e microframeworks
#o microframework blueprint é responsável por criar uma coleção de views, ou seja, rotas separadas.
from flask import Blueprint, render_template, request, redirect, flash

#instanciando "login" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('login', __name__)

#Definindo rota "/login"
@bp.route('/login', methods=['GET','POST'])
def login():
  if request.method == "GET":
    return render_template('login.html')
  elif request.method == "POST":
    flash('Logado com sucesso!')
    return redirect('/login')