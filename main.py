from flask import Flask, render_template, redirect

app = Flask(__name__)

#Rota principal
@app.route('/')
def homepage():
    return render_template('index.html')

#Rota para tratar erro 404
@app.errorhandler(404)
def error(error):
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)