from AtividadePython2.eldiano import Eldiano

ListaDeEldianos = []

while True:
    print("\nMenu:")
    print("1. Criar Eldiano")
    print("2. Listar")
    print("3. Editar")
    print("4. Deletar")
    print("5. Sair")
    
    escolha = input("Escolha uma opção(1,2,3,4,5): ")

    if escolha == "1":
        nome = input("Nome do Eldiano: ")
        nascionalidade = input("Nacionalidade do Eldiano: ")
        titan_input = input("O Eldiano possui o poder de se transformar em titã? (True/False): ")
        titan = titan_input.lower() == "true"
        eldiano = Eldiano(nome, nascionalidade, titan)
        ListaDeEldianos.append(eldiano)  # Adiciona o objeto à lista
        print(f"Eldiano {eldiano.nome} criado com sucesso!")
        
    
    elif escolha == "2":
        if not ListaDeEldianos:
            print("Nenhum Eldiano encontrado ainda.")
            continue
        else:
            print("Lista de Eldianos:")
            for eldiano in ListaDeEldianos:
                print(f" Nome: {eldiano.nome}, Nacionalidade: {eldiano.nascionalidade}, Titan: {'Sim' if eldiano.titan else 'Não'}")
                
                while True:
                    print("Ações disponíveis:\n1.Ação(Métodos)\n2.Sair\n")
                    
                    escolha_in_list = input("Escolha(1,2): ")
                    
                    if escolha_in_list == "1":
                        
                        while True:
                            print("Escolha uma ação: \n1. Transformar\n2. Regenerar\n3. Endurecer\n4. Sair")
                            
                            acao = input("Escolha(1,2,3,4): ")
                            
                            if acao == "1":
                                eldiano.transformar_em_titan()
                            elif acao == "2":
                                eldiano.regenerar()
                            elif acao == "3":
                                eldiano.endurecer()
                            elif acao == "4":
                                break
                            else:
                                print("Ação inválida. Tente novamente.")
                                
                    elif escolha_in_list == "2":
                        break
                    
    elif escolha == "3":
        if not ListaDeEldianos:
            print("Nenhum Eldiano para editar.")
            continue
        
        nome_para_editar = input("Digite o nome do Eldiano que deseja editar: ")
        
        for eldiano in ListaDeEldianos:
            if eldiano.nome == nome_para_editar:
                novo_nome = input("Novo nome (deixe em branco para manter o atual): ")
                nova_nascionalidade = input("Nova nacionalidade (deixe em branco para manter a atual): ")
                novo_titan_input = input("O Eldiano possui o poder de se transformar em titã? (True/False, deixe em branco para manter o atual): ")
                
                if novo_nome:
                    eldiano.nome = novo_nome
                if nova_nascionalidade:
                    eldiano.nascionalidade = nova_nascionalidade
                if novo_titan_input.lower() in ["true", "false"]:
                    eldiano.titan = novo_titan_input.lower() == "true"
                
                print(f"Eldiano {eldiano.nome} atualizado com sucesso!")
                break
        else:
            print("Eldiano não encontrado.")
            
    elif escolha == "4":
        if not ListaDeEldianos:
            print("Nenhum Eldiano para deletar.")
            continue
        
        nome_para_deletar = input("Digite o nome do Eldiano que deseja deletar: ")
        
        for i, eldiano in enumerate(ListaDeEldianos):
            if eldiano.nome == nome_para_deletar:
                del ListaDeEldianos[i]
                print(f"Eldiano {nome_para_deletar} deletado com sucesso!")
                break
        else:
            print("Eldiano não encontrado.")
            
    elif escolha == "5":
        print("Saindo do programa...")
        break