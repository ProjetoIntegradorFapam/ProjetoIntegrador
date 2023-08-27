#importando bibliotecas, frameworks e microframeworks
#o microframework blueprint é responsável por criar uma coleção de views, ou seja, rotas separadas.
from flask import Blueprint, render_template, request, redirect, flash

#instanciando "login" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('login', __name__)

#Definindo rota "/login"
@bp.route('/login', methods=['GET','POST'])
def login():

  #Tratamento de rotas

  #Trantando rota "GET" para renderizar o login.html
  if request.method == "GET":

    return render_template('login.html')
  
  #Tratando rota "POST" para validar os dados e fazer o redirecionamento
  elif request.method == "POST":

    #Dados do Front-End (AVISO: O CPF ESTÁ SENDO FORMATADO PORQUE O FRONT POSSUI UMA MÁSCARA QUE INCLUI CARACTERES NA STRING)
    cpf = str(request.form.get('cpf')).translate(str.maketrans('', '', '.-'))
    password = str(request.form.get('password'))

    #Validação dos dados (AVISO: USUÁRIO E SENHA PARA TESTES)
    if cpf == "00000000000" and password == "12345":

      #Enviando mensagem de sucesso e fazendo o redirecionamento para a rota "/home"
      return redirect('/home')

    else:

      #Enviando mensagem de erro e fazendo o redirecionamento para a rota "/login"
      flash('Falha ao efetuar o login!')
      return redirect('/login')
  else:
    return