#importação de bibliotecas, frameworks e microframeworks
from flask import Flask

#importação da rota "minha_rota", que se encontra na pasta "routes" 
from routes import login

#exemplo de importação para mais de uma rota
"""
from routes import minha_rota, minha_segunda_rota, minha_terceira_rota
"""

#instanciando flask
app = Flask(__name__)

#registrando rota "/login"
app.register_blueprint(login.bp) 

#verificando se está em ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)