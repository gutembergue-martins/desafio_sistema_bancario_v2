import datetime
import pytz


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1200
extrato = ""
numero_saques = 0
numero_depositos = 0
limite_operacao_diaria = 10

data_ultima_operacao = datetime.datetime.now()

while True:
    data_atual = datetime.datetime.now()
    if data_atual != data_ultima_operacao:
        numero_saques = 0
        numero_depositos = 0
        data_ultima_operacao = data_atual

    operacao_diaria = int((numero_saques) + (numero_depositos))

    opcao = input(menu)
        
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) 

        excedeu_limite_de_operacao_diaria = operacao_diaria >= limite_operacao_diaria
        
        if excedeu_limite_de_operacao_diaria:
            print("Você excedeu o número de transações permitidas para hoje!")

        elif valor > 0:
            saldo += valor
            numero_depositos += 1
            extrato += f"Depósito R$ {valor:.2f}    / Data: {data_atual.strftime('%d/%m/%Y %H:%M:%S')}\n"
                       

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_limite_de_operacao_diaria = operacao_diaria >= limite_operacao_diaria

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_limite_de_operacao_diaria:
            print("Você excedeu o número de transações permitidas para hoje!")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque    R$ {valor:.2f}     / Data: {data_atual.strftime('%d/%m/%Y %H:%M:%S')}\n"
            

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print(
        f"""
                            ***EXTRATO BANCÁRIO***
===========================================================================
                Movimentações realizadas na conta corrente

{extrato}


        Saldo: R$ {saldo:.2f}

============================================================================
        """                    
        )
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")