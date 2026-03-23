# Exibição do Menu
print("      MENU DE OPÇÕES")
print("--------------------------")
print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Sair")
print("--------------------------")

# Entrada do usuário
opcao = input("Digite uma opção: ")

# Processamento das escolhas
match opcao:
    case "1":
        print("Você selecionou a opção 1")
    case "2":
        print("Você selecionou a opção 2")
    case "3":
        print("Você selecionou a opção 3")
    case "4":
        print("Você selecionou sair")
    case _:
        print("Opção inválida!!!")

# Mensagem final obrigatória
print("Fim do programa!")
