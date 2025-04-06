#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação.
#Imprima cada informação.

livro: dict = {
    "Titulo": "Livro 1",
    "Autor": "Wilber Pacifico de Arruda",
    "Ano de Publicação": 1994

}

for chave, valor in livro.items():
    print(f"{chave}: {valor}")