import textwrap
import os


def menu():
    menu = """
    Bem-vindo ao Banco xxxxxx

    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] NOVA USUÁRIO
    [5] NOVO CONTA
    [6] LISTAR CONTA
    [0] SAIR

    Seu dinheiro é o nosso negócio.
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\nDepósito Realizado com sucesso")
    else:
        print("Operação Falhou! O valor informado é inválido.")
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("\nOperação Falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação Falhou! O valor de saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação Falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação Falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n =================== EXTRATO ==================== \n')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'\n Saldo Atual R$ {saldo:.2f}\n')
    print('====================================================')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá Existe usuário com esse CPF!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endreço (logradouro, Nº, Bairro - Cidade/Estado (sigla do estado)): ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\nUsuário Cadastrado com sucesso! ")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe  o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta Criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado. ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t {conta["agencia"]}
        C/C:\t\t {conta["numero_conta"]}
        Titular:\t {conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha)) 

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

        if opcao == "1":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE,
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            break

main()