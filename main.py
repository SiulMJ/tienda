from flask import Flask, render_template
import MySQLdb

cone = MySQLdb.connect(host="localhost", user="root", password="")
cur = db.cursor()

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comprar')
def comprar():
    return render_template('comprar.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

app.run(host="localhost", port=4000, debug="True")