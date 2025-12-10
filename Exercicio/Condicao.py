Nota1 = float(input("Digite Nota 1 "))
Nota2 = float(input("Digite Nota 2 "))
Nota3 = float(input("Digite Nota 3 "))
Nota4 = float(input("Digite Nota 4 "))

Media = (Nota1 + Nota2 + Nota3 + Nota4) /4

if Media >= 6:
    print(f"Você está aprovado {Media}")

elif Media >= 4:
    print(f"Você está em recuperação {Media}")

else:
    print("Reprovado")