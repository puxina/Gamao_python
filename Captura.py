# Função escrita para o programa
import Var
import Tabuleiro

def Peca_Capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    # Jogador 1
    if Var.jog_1:
        # Contagem de quantas peças claras foram capturadas
        pecas_capturadas = 0
        for cont in range(5):
            if Var.pecas_capturadas_claras[cont] == Var.PC_CLARA:
                pecas_capturadas += 1
        print("Variável: ", pecas_capturadas)

        # Teste das condições 
        if pecas_capturadas == 0:
            return True
        else:
            for cont in range(6):
                if Var.pecas_posi[cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        Var.d1_valido = True
                    if d2 == (cont+1):
                        Var.d2_valido = True
                    print(cont, Var.d1_valido, Var.d2_valido)
            
            if Var.d1_valido and Var.d2_valido:
                print("\n\u001b[4mOs valores de Dado 1 e Dado 2 permitem retornar a peça capturada ao tabuleiro\u001b[0m")
                while True:
                    try:
                        dado_x = int(input("Escolha qual Dado você deseja (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
                if dado_x == 1:
                    Var.pecas_posi[d1-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d1-1][0]
                    Var.d1_valido = False
                else:
                    Var.pecas_posi[d2-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d2-1][0]
                    Var.d2_valido = False
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            elif Var.d1_valido:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[d1-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d1-1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    Var.d1_valido = False
                    return True
                else:
                    return False
            elif Var.d2_valido:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[d2-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d2-1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    Var.d2_valido = False
                    return True
                else:
                    return False
            else:
                if Var.d1_valido == False and Var.d2_valido == False:
                    print("\n\u001b[4mNenhum dos dois valores permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                elif Var.d1_valido == True:
                    print("\n\u001b[4mO Dado 2 não permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                    Var.d1_valido = False
                else:
                    print("\n\u001b[4mO Dado 1 não permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                    Var.d2_valido = False
                return False

    if Var.jog_2:
        # Contagem de quantas peças escuras foram capturadas
        pecas_capturadas = 0
        for cont in range(5):
            if Var.pecas_capturadas_escuras[cont] == Var.PC_ESCURA:
                pecas_capturadas += 1
        print("Variável: ", pecas_capturadas)

        # Teste das condições 
        if pecas_capturadas == 0:
            return True
        else:
            for cont in range(6):
                if Var.pecas_posi[23-cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        Var.d1_valido = True
                    if d2 == (cont+1):
                        Var.d2_valido = True
                    print(cont, Var.d1_valido, Var.d2_valido)
            
            if Var.d1_valido and Var.d2_valido:
                print("\n\u001b[4mOs valores de Dado 1 e Dado 2 permitem retornar a peça capturada ao tabuleiro\u001b[0m")
                while True:
                    try:
                        dado_x = int(input("Escolha qual Dado você deseja (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
                if dado_x == 1:
                    Var.pecas_posi[24-d1][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d1][0]
                    Var.d1_valido = False
                else:
                    Var.pecas_posi[24-d2][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d2][0]
                    Var.d2_valido = False
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            elif Var.d1_valido:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[24-d1][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if pecas_capturadas == 0:
                    Var.d1_valido = False
                    return True
                else:
                    if Peca_Capturada(d1, d2):
                        return True
                    else:
                        return False
            elif Var.d2_valido:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[24-d2][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d2][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if pecas_capturadas == 0:
                    Var.d2_valido = False
                    return True
                else:
                    if Peca_Capturada(d1, d2):
                        return True
                    else:
                        return False
            else:
                if Var.d1_valido == False and Var.d2_valido == False:
                    print("\n\u001b[4mNenhum dos dois valores permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                elif Var.d1_valido == True:
                    print("\n\u001b[4mO Dado 2 não permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                    Var.d1_valido = False
                else:
                    print("\n\u001b[4mO Dado 1 não permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                      "Passe a jogada =( \n")
                    Var.d2_valido = False
                return False