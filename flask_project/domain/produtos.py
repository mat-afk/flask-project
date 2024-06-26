from slugify import slugify

class Produto:
    def __init__(self, name, description, price=0, image_url=""):
        self.name = name
        self.description = description
        self.slug = slugify(name)
        self.price = price
        self.image_url = image_url


def list_produtos():
    with open("produtos.csv") as file:
        return [convert_row_to_produto(row) for row in file]


def save_produto(produto: Produto):
    with open("produtos.csv", "a") as file:

        row = f"\n{produto.name},{produto.description},{produto.price},{produto.image_url}"
        file.write(row)


def convert_row_to_produto(row):
    name, description, price, image_url = row.strip().split(",")

    return Produto(
        name=name,
        description=description,
        price=price,
        image_url=image_url
    )
