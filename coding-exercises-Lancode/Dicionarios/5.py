def Login():
    V_CORRETO = {
        "nome": "Dias",
        "senha": "123",
    }
    for tentativa in range(3, 0, -1):
        nome = input("Digite Seu Nome: ")
        senha = input("Digite Seu Senha: ")

        if nome == V_CORRETO["nome"] and senha == V_CORRETO["senha"]:
            print("Parabéns você é um otario")
            return True

        else:
            print("Erro de Senha! ")

        print(f"Restam {tentativa - 1} tentativas\n")

    else:
        print("Erro Usúario")

    return False


if Login():
    print("Entrou no sistema")
else:
    print("Sistema bloqueado")

    # Upgrade +++++++++++++++++++++
