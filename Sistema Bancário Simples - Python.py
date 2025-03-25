# Variáveis globais
saldo = 0.0
extrato = []
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500.0

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do depósito precisa ser positivo.")

def sacar(valor):
    global saldo, extrato, saques_diarios
    if valor > saldo:
        print("Erro: Saldo insuficiente para realizar o saque.")
    elif valor > limite_saque:
        print(f"Erro: O valor máximo para saque é R$ {limite_saque:.2f}.")
    elif saques_diarios >= limite_saques_diarios:
        print("Erro: Limite diário de saques atingido.")
    elif valor <= 0:
        print("Erro: Valor de saque inválido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    print("\n=== Extrato Bancário ===")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("========================\n")

# Menu principal
while True:
    print("\n=== Banco Python ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir Extrato")
    print("4 - Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        valor = float(input("Digite o valor a depositar: "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor a sacar: "))
        sacar(valor)
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por usar o Banco Python! Até logo!")
        break
    else:
        print("Opção inválida, tente novamente.")
