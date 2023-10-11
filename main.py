#importação de bibliotecas, frameworks e microframeworks
from flask import Flask, session

#importação de rotas
from routes import login, home, register_user

#instanciando flask
app = Flask(__name__)

#configurando secret_key
app.secret_key = "projeto_integrador:SSH-xlmns2qw89@web_application_with_python.projeto_integrador"

#registro de rotas
app.register_blueprint(login.bp)
app.register_blueprint(home.bp)
app.register_blueprint(register_user.bp)

#verificando se está em ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)))