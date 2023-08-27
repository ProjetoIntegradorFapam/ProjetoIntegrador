#importação de bibliotecas, frameworks e microframeworks
from flask import Flask, session

#importação da rota "login"
from routes import login, home

#instanciando flask
app = Flask(__name__)

#configurando secret_key
app.secret_key = "hsjebej337isb"

#registrando rota "/login"
app.register_blueprint(login.bp)

#registrando rota "/home"
app.register_blueprint(home.bp)

#verificando se está em ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)