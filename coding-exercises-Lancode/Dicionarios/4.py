D_CORRETO = {
    'nome': 'Dias',
    'senha': '123'
}


for Tentativas in range(3, 0, -1):
    D_Entrada = {
        'nome': input('Digite seu nome: '),
        'senha': input('Digite seu Senha: '),
    }

    if D_Entrada['nome'] == D_CORRETO['nome'] and D_Entrada['senha'] == D_CORRETO['senha']:
        print("==============================="),
        print('Acesso autorizado')
        break

    elif  D_Entrada['nome'] != D_CORRETO['nome']:
        print("==============================="),
        print("Nome errado!! "),
        print(f'Resta {Tentativas - 1} tentativa(s)')
        
    elif D_Entrada['senha'] != D_CORRETO['senha']:
        print("==============================="),
        print("Senha Incorreta "),
        print(f'Resta {Tentativas - 1} tentativa(s)')
        
    
    



else :
    print("Acesso bloqueado! ")