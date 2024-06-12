from flask import Flask, render_template
from flask_project.domain.produtos import produtos_list

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=produtos_list)


@app.route("/produtos/<name>")
def produto(name):
    for produto in produtos_list:
        if produto["slug"] == name:
            return render_template("produto.html", produto=produto)
        
    return "Erro: Produto não encontrado"
            
    