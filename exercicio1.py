#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista: list  = (range(1, 11))

for numero in lista:
    print("O quadrado de {} é {}".format(numero, numero ** 2))
    print("O cubo de {} é {}".format(numero, numero ** 3))