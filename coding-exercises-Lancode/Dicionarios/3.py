D_CORRETO = {
    'usuario': 'Dias',
    'senha': 4567 ,
}

D_Entrada = {
    'usuario': input('Digite seu nome: '),
    'senha': int(input("Digite sua idade ")),

}

if  D_Entrada['usuario'] == D_CORRETO['usuario'] and D_Entrada['senha'] == D_CORRETO ['senha'] : 
    print("liberado")
    
    
else: print("negado")