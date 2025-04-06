# Solicita ao usuário que digite seu nome
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is not True:
    try:
        nome:str = str(input("Digite seu nome: "))

        # Verifica se o nome está vazio
        if len(nome) == 0:

            raise ValueError("O nome não pode estar vazio.")

        # Verifica se há números no nome
        elif nome.isdigit():

            raise ValueError("O nome não deve conter números.")
        elif nome.isnumeric():

            raise ValueError("O nome não deve conter números.")

        else:
            nome_valido = True
            print("Nome válido:", nome)
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

while salario_valido is not True:
    try:
        salario:float = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")


    # Solicita ao usuário que digite o valor do bônus recebido e converte para float
while bonus_valido is not True:
    try:
        bonus:float = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")


bonus_recebido:float = 1000 + (salario * bonus)  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")