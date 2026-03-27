print("Bem vindos a aula do Match\n")
print("Escolha seu meio de transposte")
print(" 1: Carro,\n 2: Bicicleta,\n 3: Avião,\n OU 4: helicóptero \n ")

Escolha = int(input('Digite Sua escolha '))



match Escolha:
    case 1:
        print("Carro")
    case 2:
        print("bicicleta")
    case 3:
        print("avião")
    case 4:
        print("helicóptero")
    case _:
        print("Transporte desconhecido")


