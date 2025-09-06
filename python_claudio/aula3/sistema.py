from models.Pessoa import Pessoa
def menu():
    print("=== MENU ===")
    print("1 - Criar Pessoa")
    print("2 - Listar Pessoa")
    print("3 - Limpar Lista")
    print("9 - Sair do Sistema")

def iniciarSistema():
    print("Sistema Iniciado")

    while(True):
        menu()
        opcao = input("Selecione uma opção...")
        if opcao == "1":
            nome = input ("Digite o nome da pessoa..")
            email= input ("digite o email da pessoa..")
            pessoa = Pessoa(nome,email) # Manifestando a Entidade Pessoa

# Lógica para iniciar automaticamente
if __name__ == "__main__":
    iniciarSistema()