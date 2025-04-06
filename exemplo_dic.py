#https://docs.python.org/3/tutorial/datastructures.html#dictionaries

import json

produto_01:dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02:dict = {
    "nome":"Televisao",
    "quantidade":39,
    "preco": 70.38,
    "disponibilidade": False
}


carrinho: list = [] #Cria uma lista nova

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho) #O json é o dicionário do Javascript. 
#Para trabalhar no Python é preciso usasr o dump
print(carrinho_json)
