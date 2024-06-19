from slugify import slugify

class Produto:
    def __init__(self, name, description, price=0, image_url=""):
        self.name = name
        self.description = description
        self.slug = slugify(name)
        self.price = price
        self.image_url = image_url

produtos = [
    Produto("Guaraná", "Melhor refrigerante do mundo", 7.90, "https://acdn.mitiendanube.com/stores/001/165/503/products/guarana1-b5047b4aaf1e0c9b6b16192134101772-1024-1024.png"),
    Produto("Coca-cola", "Veneno", 8.0, "https://acdn.mitiendanube.com/stores/001/165/503/products/coca-normal11-2cb12d901c0ec9eb9716192140335257-1024-1024.png"),
    Produto("Pepsi", "Ruim", 6.90, "https://www.jauserve.com.br/dw/image/v2/BFJL_PRD/on/demandware.static/-/Sites-jauserve-master/default/dw44e5d80d/7892840800079.png?sw=1800"),
    Produto("Água", "Bom", 3.50, "https://s3-sa-east-1.amazonaws.com/superimg/img.produtos/7894900531008/img_1200_1.png"),
    Produto("Doritos", "Salgado", 5.90, "https://giassi.vtexassets.com/arquivos/ids/1163835/Salgadinho-de-Milho-Queijo-Nacho-Doritos-Pacote-300g.png?v=638510248118900000"),
]