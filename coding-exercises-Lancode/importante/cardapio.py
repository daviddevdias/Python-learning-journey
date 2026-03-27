print('Pizza, Sushi ,Salada\n')

Escolha = int(input("Digite oque deseja do menu: "))

match Escolha:
    case 1 :
        print('Pizza')
    case 2 :
        print('Suchi')
    case 3 :
        print('Salada')
    
    case _:
        print('número invalido')