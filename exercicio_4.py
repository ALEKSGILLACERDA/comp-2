
produtos = {
    "Notebook": 5000,
    "Celular": 2500,
    "Fone": 200,
    "Cadeira": 750
}

resultado = dict(map(lambda item: (item[0], item[1]/5), produtos.items()))
print(resultado)
