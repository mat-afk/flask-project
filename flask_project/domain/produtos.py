from slugify import slugify

produtos_list = [
    { "name": "Guaraná", "description": "Melhor refrigerante do mundo" },
    { "name": "Coca-cola", "description": "Veneno" },
    { "name": "Pepsi", "description": "Ruim" },
    { "name": "Água", "description": "Bom" },
]

for produto in produtos_list:
    produto["slug"] = slugify(produto["name"])