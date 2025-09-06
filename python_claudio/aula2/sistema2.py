
# SISTEMA GERENCIADOR DE NOMES
nomes = [] # lista vazia
while True:  
    print("=== MENU NOMES ===")
    print("1 - Adicionar Nomes")
    print("2 - Listar Nomes")
    print("3 - Deletar Nomes")
    print("4 - Deletar Nome Especifico")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")

    #Adicionar tarefa
    if opcao == "1":
        nome = input("Digite o novo nome: ")
        # append -> adicionar a lista
        nomes.append(nome)
        print("Nome adicionado com sucesso!")

    #Listar Tarefas
    elif opcao == "2":
        #len -> length -> tamanho
        if len(nomes) == 0:
            print("Não existem nomes cadastrados")
        else:
            for nome in nomes:
                print(nome)

    elif opcao == "3":
        nomes = []
        print("Nome deletado com sucesso ")
       
    elif opcao == "4":
        if len(nomes) == 0:
            print("Nenhum nome cadastrado")
        else:
            for posicao, nome in enumerate(nomes):
                print(f"{posicao}. {nome}")
            pos = input("Escolha o nome para deletar..")
            nomes.remove(nomes[pos])
            print("Nome especifico deletado")

    elif opcao == "9":
        print("Saindo do Sistema")
        break
    else:
        print("Opção inexistente, tente novamente...")





