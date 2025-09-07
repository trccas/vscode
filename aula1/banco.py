print ("Bem vindo ao Banco girabonk")
saldo = float(input(" Digite seu saldo... R$"))

transferencia = float (input("Qual o valor da transferência? R$"))

# valide se ela possui saldo suficiente para transferência
if saldo >= transferencia:
    print("saldo suficiente!")
    # Atualizandio valor do saldo
    saldo - transferencia
    print("Seu saldo atual é de R$", saldo)
else:
    print("Saldo não é suficiente")


