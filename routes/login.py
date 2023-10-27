#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, request, redirect, flash


#instanciando "login" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('login', __name__)

#Definindo rota "/login"
@bp.route('/', methods=['GET','POST'])
@bp.route('/login', methods=['GET','POST'])
def login():

  #Tratamento de rotas

  #Trantando rota "GET" para renderizar o login.html
  if request.method == "GET":

    return render_template('login.html')
  
  #Tratando rota "POST" para validar os dados e fazer o redirecionamento
  else:

    #importanto conexão com banco de dados
    from db import utils

    #Dados do Front-End (AVISO: O CPF ESTÁ SENDO FORMATADO PORQUE O FRONT POSSUI UMA MÁSCARA QUE INCLUI CARACTERES NA STRING)
    cpf = str(request.form.get('cpf')).translate(str.maketrans('', '', '.-'))
    senha = str(request.form.get('password'))

    #Validação dos dados (AVISO: USUÁRIO E SENHA PARA TESTES)
    if utils.select_user(cpf, senha) == True:

      #fazendo o redirecionamento para a rota "/home"
      return redirect('/home')

    else:

      #Enviando mensagem de erro e fazendo o redirecionamento para a rota "/login"
      flash('Falha ao efetuar o login!')
      return redirect('/login')


# Rota de logout (se desejar)
@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/login')