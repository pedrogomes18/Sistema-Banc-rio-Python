menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Exit
"""


saldo = 0
limite = 500
extrato = ""
numero_saques=0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor >0:
            saldo+=valor
            extrato+= f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou , O valor informado é inválido")
    
    elif opcao == "s":
        valor = float(input("Digite o valor de saque"))

        if valor > saldo:
            print("Operação Falhou. Você não tem saldo suficiente")

        elif  valor > limite:
            print("Operação Falhou. O valor excede Limite")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Nº máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1
        
        else: 
            print("Falhou, O valor informado é inválido")

    elif opcao == "e":
        print("\n### EXTRATO ###")
        print("Não foram realizados as movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("operação inválida, pf selecione novamente")





