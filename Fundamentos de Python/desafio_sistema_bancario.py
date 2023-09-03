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
import os

saldo = 0
LIMITE = 500
limite_valor = 0
extrato = ''
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

# função saque
def saque():
    print('saque')

while True: # seleção do menu em loop

    op = int(input(menu)) # opção do usuário

    if op == 1: # opção 1 para extrato 
        print('\n =================== EXTRATO ==================== \n')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\n Saldo Atual R$ {saldo:.2f}\n')
        print('====================================================')
        input('\n\nAperte qualquer tecla para continuar...')

    elif op == 2: # opção 2 para deposito
            valor = float(input('informe o valor que deseja depositar: '))
    
            if valor > 0:
                saldo += valor
                extrato += f"Depósito R${valor:.2f}\n"
                print('\nRealizando Operação \nAguarde...')
            else:
                ('\nValor inválido !')

    elif op == 3: # opção 3 para saque
        if numero_saques < LIMITE_SAQUE:
            if(limite_valor <= LIMITE):
                valor = float(input('Informe o valor que deseja sacar: '))
                if(valor <= saldo):
                    numero_saques += 1
                    limite_valor += valor
                    saldo -= valor
                    extrato += f'Saque de R$ {valor:.2f}\n'
                    print('\nRealizando Operação \nAguarde...')
                else:
                    print('\nImpossível realizar saque, valor de saque menor que saldo Atual')
            else:
                print('\nValor da Saque excedido ')
        else:
            print('\nLimite de Saque por dia Alcançado !')

    elif op == 0: # opção 0 para sair do programa 
        break # encerra o loop e sai do programa
    
    else:
        print('\nOpção inválida, Por Favor selecione uma da opção a baixo ! ')

    time.sleep(3)# temporizado de 3 segundo
    os.system('cls') # limpa a tela do usuário 