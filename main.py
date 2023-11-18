#importação de bibliotecas, frameworks e microframeworks
from flask import Flask

#importação de rotas
from routes import login, home, register_user, register_nutrition, register_clinic, users, edit_user, report

#instanciando flask
app = Flask(__name__)

#configurando secret_key
app.secret_key = "projeto_integrador:SSH-xlmns2qw89@web_application_with_python.projeto_integrador"

#registro de rotas
app.register_blueprint(login.bp)
app.register_blueprint(home.bp)
app.register_blueprint(register_user.bp)
app.register_blueprint(register_nutrition.bp)
app.register_blueprint(register_clinic.bp)
app.register_blueprint(users.bp)
app.register_blueprint(edit_user.bp)
app.register_blueprint(report.bp)

#verificando se está em ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)