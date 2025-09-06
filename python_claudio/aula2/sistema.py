# SISTEMA DE TAREFAS
tarefas =[] # lista vazia

while True:
    print("=== MENU TAREFAS ===")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefa")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")

    #Adicionar tarefa
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        # append -> adicionar a lista
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    #Listar Tarefas
    elif opcao == "2":
        #len -> length -> tamanho
        if len(tarefas) == 0:
            print("Não existem tarefas cadastradas")
        else:
            for tarefa in tarefas:
                print(tarefa)
    elif opcao == "9":
        print("Saindo do Sistema")
        break
    else:
        print("Opção inexistente, tente novamente...")



