# Função escrita para o programa
import Var
import Tabuleiro

def Peca_Capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    dado_val = [False, False]
    pecas_capturadas = 0

    # Jogador 1
    if Var.jog_1:
        for cont in range(5):
            if Var.pecas_capturadas_claras[cont] == Var.PC_CLARA:
                pecas_capturadas += 1

        # Teste das condições 
        if pecas_capturadas == 0:
            return True
        else:
            for cont in range(6):
                if Var.pecas_posi[cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        dado_val[0] = True
                    if d2 == (cont+1):
                        dado_val[1] = True
            
            if dado_val[0] and dado_val[1]:
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
                else:
                    Var.pecas_posi[d2-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d2-1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            elif dado_val[0]:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[d1-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d1-1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            elif dado_val[1]:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[d2-1][0], Var.pecas_capturadas_claras[pecas_capturadas-1] = Var.pecas_capturadas_claras[pecas_capturadas-1], Var.pecas_posi[d2-1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            else:
                print("\n\u001b[4mNenhum valor permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                "Passe a jogada =( \n")
                return False

    if Var.jog_2:
        for cont in range(5):
            if Var.pecas_capturadas_escuras[cont] == Var.PC_ESCURA:
                pecas_capturadas += 1

        # Teste das condições 
        if pecas_capturadas == 0:
            return True
        else:
            for cont in range(6):
                if Var.pecas_posi[23-cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        dado_val[0] = True
                    if d2 == (cont+1):
                        dado_val[1] = True
            
            if dado_val[0] and dado_val[1]:
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
                else:
                    Var.pecas_posi[24-d2][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d2][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            elif dado_val[0]:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[24-d1][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d1][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return True
                else:
                    if Peca_Capturada(d1, d2):
                        return True
                    else:
                        return False
            elif dado_val[1]:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Var.pecas_posi[24-d2][0], Var.pecas_capturadas_escuras[pecas_capturadas-1] = Var.pecas_capturadas_escuras[pecas_capturadas-1], Var.pecas_posi[24-d2][0]
                pecas_capturadas -= 1
                Tabuleiro.Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return True
                else:
                    if Peca_Capturada(d1, d2):
                        return True
                    else:
                        return False
            else:
                print("\n\u001b[4mNenhum valor permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                "Passe a jogada =( \n")
                return False