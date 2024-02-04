import textwrap


def menu():
    menu = """\n

    =================== MENU ===================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usúario
    [0]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:

    
main()