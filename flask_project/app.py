from flask import Flask, render_template, redirect, url_for, request
from .domain.produtos import produtos as produtos_list, Produto

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos/produtos.html", produtos=produtos_list)


@app.route("/produtos/<name>")
def produto(name):
    for produto in produtos_list:
        if produto.slug == name:
            return render_template("produtos/produto.html", produto=produto)
        
    return "Erro: Produto não encontrado"


@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("produtos/cadastro_produto.html")


@app.route("/produtos", methods=["POST"])
def salvar_produto():
    name = request.form["name"]
    description = request.form["description"]
    price = request.form["price"]
    image_url = request.form["image_url"]

    produto = Produto(name, description, price, image_url)

    produtos_list.append(produto)

    return redirect(url_for("produtos"))


if __name__ == "__main__":
    app.run()