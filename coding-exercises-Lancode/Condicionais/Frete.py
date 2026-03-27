print("Bem vindo ao estudo Frete\n")


Valor = float(input("Digite o valor do produto >> "))

Programa = str(input("Está no programa??  ")).lower() .strip()


if Valor >= 100 and Programa == 'sim':
    print("Frete grátis aplicado! ")

elif Valor < 100 and Programa == 'nao':
    print("Frete não disponível gratuitamente. ")

elif Programa == 'nao':
    print("Frete não disponível gratuitamente.")

else: ("Não repondido")

