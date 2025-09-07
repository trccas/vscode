print("SISTEMA DA ADMNISTRAÇÃO")

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "123456":
        print("Login bem sucedido!")
    else:
        print("usuário ou senha incorreta")
else:
    print("usuário ou senha incorreta")