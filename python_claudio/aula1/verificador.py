idade = int(input("Digite sua idade.. "))

if idade < 18:
    print("Você é menor de idade.")
else:
    print("Maior de idade")
    # and -> 0
    if idade >= 18 and idade <= 70:
        print("Seu voto é obrigatório")
    else:
        print("Seu voto é facultativo")