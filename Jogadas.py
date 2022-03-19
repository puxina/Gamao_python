def Opcoes(d1, d2):
    """Função para indicar as várias opções disponíveis do uso dos dados ao jogador"""
    if d1 == d2:
        while True:
            try:
                print("\nSelecione uma das opções de jogadas disponíveis abaixo:\n")
                print("1 - A soma dos dados")
                print("2 - Dado D1+D2")
                print("3 - Dado D2+D3")
                print("4 - Dado D3+D4\n")
                opcao = int(input("Opção: "))
                if opcao < 1 or opcao > 4:
                    raise ValueError
                else:
                    return opcao
            except ValueError:
                print("\u001b[41mOpção inválida.\u001b[0m Repita a operação.")
    else:
        while True:
            try:
                print("\nSelecione uma das opções de jogadas disponíveis abaixo:\n")
                print("1 - A soma dos dados")
                print("2 - Dado D1")
                print("3 - Dado D2\n")
                opcao = int(input("Opção: "))
                if opcao < 1 or opcao > 3:
                    raise ValueError
                else:
                    return opcao
            except ValueError:
                print("\u001b[41mOpção inválida.\u001b[0m Repita a operação.")