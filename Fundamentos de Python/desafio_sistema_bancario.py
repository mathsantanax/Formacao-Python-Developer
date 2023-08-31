# Este é um projeto desenvolvido atráves dos desafios da dio.me 

# fomos contratados por um grande banco para desenvolver o seu novo sistema.
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
# Para a primeira versão do sistema devemos implementar apenas 3 operações: Depósito, Saque, Extrato.

# Operação De Depósito

# Deve ser possivel depositar valores positivos para a minha conta bancarias.
# A v1 do projeto trabalha apenas com 1 usuários, dessa forma não precisamos
# nos preocupar em identificar qual é o número da agência e conta bancária.
# todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de Saque

# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando
# que não será possível sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de Extrato

# Essa operação deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, 
# exemplo 1500,45 = R$ 1500,45

import time

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

# Menu de Seleção para aprensentação
menu = """
    Bem-vindo ao Banco xxxxxx

    [1] EXTRATO
    [2] DEPÓSITO
    [3] SAQUE
    [0] SAIR

    Seu dinheiro é o nosso negócio.
 """

# funçao extrato
def extrato():
    print('extrato')

# função deposito
def deposito():
    print('deposito')

# função saque
def saque():
    print('saque')

while True: # seleção do menu em loop

    op = int(input(menu)) #opção do usuário

    if op == 1: # opção 1 para extrato 
        extrato() # chama a função extrato

    elif op == 2: # opção 2 para deposito
        deposito()# chama a função deposito

    elif op == 3: # opção 3 para saque
        saque()  # chama a função saque

    elif op == 0: # opção 0 para sair do programa 
        break # encerra o loop e sai do programa
    
    else:
        print('Opção inválida, Por Favor selecione uma da opção a baixo ! ')

    time.sleep(3)