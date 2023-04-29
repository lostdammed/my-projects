print("""

BEM VINDO AO SISTEMA BANCÁRIO!

Digite a operação desejada:

[s] para SAQUE;
[d] para DEPÓSITO;
[e] para EXTRATO;
[q] para SAIR;

""")

saldo = 1500.00
limite = 500
extrato = ""
contagem_de_saques = -1
LIMITE_SAQUES = 3

while True:
    
    opcao = str(input())

    if opcao == "s":
        if contagem_de_saques >= LIMITE_SAQUES:
            print("Você atingiu seu número diário de saques!")
        else:
            valor_de_saque = int(input("Informe o valor para saque:\n"))
            if saldo < valor_de_saque:
                  print("Você não possui saldo para realizar o saque!")
            elif valor_de_saque > limite:
                 print("Seu limite diário para saque é de R$ 500.00")
            else:    
                print("Valor sacado com sucesso, retire na boca do caixa!")
                contagem_de_saques +=1
                saldo -= valor_de_saque
                extrato += f"\nSaque R$ {valor_de_saque:.2f}"
        
    elif opcao =="d":
        valor_de_deposito = float(input("Informe o valor para depósito:\n"))
        if valor_de_deposito < 0:
             print("Não é possível depositar um valor negativo, informe um valor válido!")
        else:
             print("Valor depositado com sucesso!")
             saldo += valor_de_deposito
             extrato += f"\nDepósito R$ {valor_de_deposito:.2f}"

    elif opcao =="e":
            if extrato == "":
                print("Não foram realizadas movimentações.")
            else:
                print("EXTRATO:\n")
                print(f"Saldo: {saldo:.2f}\n")
                print(extrato)
    
    elif opcao =="q":
           print("\nObrigado pela preferência!\n")
           break
    else:
            print("OPÇÃO INVÁLIDA!")