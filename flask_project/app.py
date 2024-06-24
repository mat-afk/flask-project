from flask import Flask, render_template, redirect, url_for, request
from flask_project.domain.produtos import produtos as produtos_list, Produto
from flask_project.docbr.docs import docs

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


@app.route("/<doc_name>/generate")
def generate(doc_name):
    doc = docs[doc_name]

    return render_template(
        "docbr/generate.html", 
        doc_name=doc_name.upper(), 
        docs=docs, 
        generated=doc.generate(True)
    )


@app.route("/<doc_name>/validate")
def validate_form(doc_name):
    return render_template("docbr/validate.html", doc_name=doc_name.upper(), docs=docs)


@app.route("/<doc_name>/validate", methods=["POST"])
def validate(doc_name):
    doc = docs[doc_name]
    doc_to_validate = request.form["doc"]

    return render_template(
        "docbr/validation_result.html", 
        doc_name=doc_name.upper(), 
        doc=doc_to_validate, 
        is_valid=doc.validate(doc_to_validate)
    )


if __name__ == "__main__":
    app.run(port=5001)