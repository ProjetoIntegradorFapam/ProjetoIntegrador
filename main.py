#importação de bibliotecas, frameworks e microframeworks
from flask import Flask

#importação da rota "minha_rota", que se encontra na pasta "routes" 
from routes import minha_rota

#exemplo de importação para mais de uma rota
"""
from routes import minha_rota, minha_segunda_rota, minha_terceira_rota
"""

#instanciando flask
app = Flask(__name__)

#registrando rota "minha_rota", (ORBIGATORIAMENTE COLOR ".bp" NO FINAL DO ARQUIVO DA ROTA)
app.register_blueprint(minha_rota.bp) #para registrar mais rotas copie esta linha e altere somente o nome da nova rota

#verificando se está em ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)