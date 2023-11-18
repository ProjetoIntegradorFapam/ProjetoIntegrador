#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template, redirect, url_for
from reportlab.pdfgen import canvas

#importando gerenciamento de autenticação do usuário
from routes.login import user

#instanciando "report" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('report', __name__)

#Definindo rota "/report"
@bp.route('/report', methods=['GET'])
def report():
    
  if user.isAuthenticated():

    #renderizando home e enviando os usuários do banco
    return render_template('report.html', title='Página Inicial')
  else:
    #redireciona para login
    return redirect('/login')

#Definindo rota "/report/generate"
@bp.route('/report/generate', methods=['GET'])
def generate():
    
  if user.isAuthenticated():

    from datetime import date

    data = date.today()
    nome_arquivo = f"relatorio_tech {data}.pdf"
    slogan = "Clinica Nutricional"
    logo = url_for('static', filename='img/logo.png')
    endereco = "123 Tech Street, Cidade Tech, Estado Tech, CEP Tech"
    nome_empresa = "Tech Solutions Inc."
    telefone = "+55 123 456 789"

    gerar_pdf(nome_arquivo, slogan, logo, endereco, nome_empresa, telefone)

    #renderizando home e enviando os usuários do banco
    return redirect('/report')
  else:
    #redireciona para login
    return redirect('/login')

#função para gerar relatório
def gerar_pdf(nome_arquivo, slogan, logo, endereco, nome_empresa, telefone):

    c = canvas.Canvas(nome_arquivo)

    # Adiciona Logo
    if logo:
        c.drawImage(logo, 50, 751, width=120, height=80)
    
    # Adiciona o slogan
    c.setFont("Helvetica", 30)
    c.drawCentredString(300, 600, slogan)

    # Adiciona o endereço
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, "Endereço:")
    c.drawString(150, 700, endereco)

    # Adiciona o nome da empresa
    c.drawString(50, 680, "Nome da Empresa: ")
    c.drawString(150, 680, nome_empresa)

    # Adiciona o telefone
    c.drawString(50, 660, "Telefone:")
    c.drawString(150, 660, telefone)

    c.save()
