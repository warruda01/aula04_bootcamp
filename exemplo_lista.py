#https://docs.python.org/3/tutorial/datastructures.html

produto:str = "sapato"
produto_2:str = "camiseta"
produto_3: str = "videogame"

produtos: list = [] #Criando lista vazia

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

produtos.pop() #Tira o último produto da lista

print(produtos)

produtos.pop() #Tira o último produto da lista novamente

print(produtos)
produtos.append(produto_2) #Colocando os produtos novamente
produtos.append(produto_3)#Colocando os produtos novamente
print(produtos)
produtos.remove(produto_2)
print(produtos)

numeros: list = []
numeros.extend(range(0, 5)) #Adicionando um Range em uma lista
print(numeros)