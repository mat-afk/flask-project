from flask import Flask, render_template

produtos_list = [
    { "name": "Guaraná", "description": "Melhor refrigerante do mundo" },
    { "name": "Coca-cola", "description": "Veneno" },
    { "name": "Pepsi", "description": "Ruim" },
    { "name": "Água", "description": "Bom" },
]


app = Flask(__name__, template_folder="./templates")


@app.route("/")
def home():
    return "<h1>Home</h1>"


@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=produtos_list)


@app.route("/produtos/<name>")
def produto(name):

    for produto in produtos_list:
        if produto["name"].lower() == name:
            return render_template("produto.html", produto=produto)
        
    return "Erro: não existe produto com esse nome"
            
    