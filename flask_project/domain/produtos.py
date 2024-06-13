from slugify import slugify

produtos = [
    { "name": "Guaraná", "description": "Melhor refrigerante do mundo" },
    { "name": "Coca-cola", "description": "Veneno" },
    { "name": "Pepsi", "description": "Ruim" },
    { "name": "Água", "description": "Bom" },
    { "name": "Doritos", "description": "Salgado" },
]

for produto in produtos:
    produto["slug"] = slugify(produto["name"])