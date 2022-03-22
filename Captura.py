# Função escrita para o programa
import Var
import Tabuleiro
import Jogadas

# Função
def Retorno(casa_cond, dado, pc_cap_cl, pc_cap_es):
    """Função para permutar a peça retornada ao jogo"""
    pecas_casa = 0
    # Se jogador 1
    if Var.jog_1:
        # Dado válido para retorno se a casa for vazia
        if casa_cond == 1:
            Var.pecas_posi[dado-1][0], Var.pecas_capturadas_claras[pc_cap_cl-1] = Var.pecas_capturadas_claras[pc_cap_cl-1], Var.pecas_posi[dado-1][0]
        # Dado válido para retorno se a casa somente tiver uma peça adversária,
        # a qual será capturada
        elif casa_cond == 2:
            Var.pecas_posi[dado-1][0], Var.pecas_capturadas_escuras[pc_cap_es] = Var.pecas_capturadas_escuras[pc_cap_es], Var.pecas_posi[dado-1][0]
            Var.pecas_posi[dado-1][0], Var.pecas_capturadas_claras[pc_cap_cl-1] = Var.pecas_capturadas_claras[pc_cap_cl-1], Var.pecas_posi[dado-1][0]
        # Dado válido para retorno em uma casa que contém peças suas (brancas)
        else:
            for cont in range(len(Var.pecas_posi[dado-1])):
                if Var.pecas_posi[dado-1][cont] == Var.PC_CLARA:
                    pecas_casa += 1
            Var.pecas_posi[dado-1][pecas_casa], Var.pecas_capturadas_claras[pc_cap_cl-1] = Var.pecas_capturadas_claras[pc_cap_cl-1], Var.pecas_posi[dado-1][pecas_casa]
        return
    # Jogador 2
    else:
        # Dado válido para retorno se a casa for vazia
        if casa_cond == 1:
            Var.pecas_posi[24-dado][0], Var.pecas_capturadas_escuras[pc_cap_es-1] = Var.pecas_capturadas_escuras[pc_cap_es-1], Var.pecas_posi[24-dado][0]
        # Dado válido para retorno se a casa somente tiver uma peça adversária,
        # a qual será capturada
        elif casa_cond == 2:
            Var.pecas_posi[24-dado][0], Var.pecas_capturadas_claras[pc_cap_cl] = Var.pecas_capturadas_claras[pc_cap_cl], Var.pecas_posi[24-dado][0]
            Var.pecas_posi[24-dado][0], Var.pecas_capturadas_escuras[pc_cap_es-1] = Var.pecas_capturadas_escuras[pc_cap_es-1], Var.pecas_posi[24-dado][0]
        # Dado válido para retorno em uma casa que contém peças suas (brancas)
        else:
            for cont in range(len(Var.pecas_posi[dado-1])):
                if Var.pecas_posi[24-dado][cont] == Var.PC_ESCURA:
                    pecas_casa += 1
            Var.pecas_posi[24-dado][pecas_casa], Var.pecas_capturadas_escuras[pc_cap_es-1] = Var.pecas_capturadas_escuras[pc_cap_es-1], Var.pecas_posi[24-dado][pecas_casa]
        return


# Função
def Peca_Capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    dado_val = [False, False]
    pecas_capturadas = [0, 0]
    casa_cond = [0, 0]

    for cont in range(6):
        if Var.pecas_capturadas_claras[cont] == Var.PC_CLARA:
            pecas_capturadas[0] += 1
        if Var.pecas_capturadas_escuras[cont] == Var.PC_ESCURA:
            pecas_capturadas[1] += 1

    # Jogador 1
    if Var.jog_1:
        # Teste das condições 
        if pecas_capturadas[0] == 0:
            Jogadas.Jogada_Opcoes(d1, d2)
            return True
        else:
            # Verificação de qual(is) dado(s) é(são) válido(s) para retornar a peça ao tabuleiro
            for cont in range(6):
                # Dado válido para retorno se a casa for vazia
                if Var.pecas_posi[cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        casa_cond[0] = 1
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 1
                        dado_val[1] = True
                # Dado válido para retorno se a casa somente tiver uma peça adversária,
                # a qual será capturada
                if Var.pecas_posi[cont][0] == Var.PC_ESCURA and Var.pecas_posi[cont][1] == Var.PC_NULA:
                    if d1 == (cont+1):
                        casa_cond[0] = 2
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 2
                        dado_val[1] = True
                # Dado válido para retorno em uma casa que contém peças suas (brancas)
                if Var.pecas_posi[cont][0] == Var.PC_CLARA:
                    if d1 == (cont+1):
                        casa_cond[0] = 3
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 3
                        dado_val[1] = True
                
            # Condições de retorno conforme a validade dos dados:
            # Ambos os dados podem ser usados e o usuário irá escolher qual
            if dado_val[0] and dado_val[1] and Var.dado_usado == 0:
                print("\n\u001b[4mOs valores de D1 e D2 permitem retornar a peça capturada ao tabuleiro\u001b[0m")
                while True:
                    try:
                        dado_x = int(input("Escolha qual dado você deseja (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
                # Escolheu D1
                if dado_x == 1:
                    Retorno(casa_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 1
                # Escolheu D2
                else:
                    Retorno(casa_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 2
                pecas_capturadas[0] -= 1
                Tabuleiro.Print_Tabuleiro()
                if Peca_Capturada(d1, d2):
                    return True
                else:
                    return False
            # Somente dado 1 está apto a ser usado
            elif dado_val[0]:
                print("\n\u001b[4mO valor do D1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Retorno(casa_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 1
                pecas_capturadas[0] -= 1
                Tabuleiro.Print_Tabuleiro()
                return False
            # Somente dado 2 está apto a ser usado
            elif dado_val[1]:
                print("\n\u001b[4mO valor do D2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Retorno(casa_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 2
                pecas_capturadas[0] -= 1
                Tabuleiro.Print_Tabuleiro()
                return False
            # Nenhum dado está apto a ser usado
            else:
                print("\n\u001b[4mNenhum valor dos dados permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                "Passe a jogada =( \n")
                return False
    # Jogador 2
    if Var.jog_2:
        # Teste das condições 
        # Teste das condições 
        if pecas_capturadas[1] == 0:
            Jogadas.Jogada_Opcoes(d1, d2)
            return True
        else:
            # Verificação de qual(is) dado(s) é(são) válido(s) para retornar a peça ao tabuleiro
            for cont in range(6):
                # Dado válido para retorno se a casa for vazia
                if Var.pecas_posi[23-cont][0] == Var.PC_NULA:
                    if d1 == (cont+1):
                        casa_cond[0] = 1
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 1
                        dado_val[1] = True
                # Dado válido para retorno se a casa somente tiver uma peça adversária,
                # a qual será capturada
                if Var.pecas_posi[23-cont][0] == Var.PC_CLARA and Var.pecas_posi[23-cont][1] == Var.PC_NULA:
                    if d1 == (cont+1):
                        casa_cond[0] = 2
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 2
                        dado_val[1] = True
                # Dado válido para retorno em uma casa que contém peças suas (brancas)
                if Var.pecas_posi[23-cont][0] == Var.PC_ESCURA:
                    if d1 == (cont+1):
                        casa_cond[0] = 3
                        dado_val[0] = True
                    if d2 == (cont+1):
                        casa_cond[1] = 3
                        dado_val[1] = True
            
            # Condições de retorno conforme a validade dos dados:
            # Ambos os dados podem ser usados e o usuário irá escolher qual
            if dado_val[0] and dado_val[1] and dado_usar == 0:
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
                # Escolheu D1
                if dado_x == 1:
                    Retorno(casa_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    pecas_capturadas[1] -= 1
                    Tabuleiro.Print_Tabuleiro()
                    if Peca_Capturada(d1, d2, 2):
                        return True
                    else:
                        return False
                # Escolheu D2
                else:
                    Retorno(casa_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    pecas_capturadas[1] -= 1
                    Tabuleiro.Print_Tabuleiro()
                    if Peca_Capturada(d1, d2, 1):
                        return True
                    else:
                        return False
            # Somente dado 1 está apto a ser usado
            elif dado_val[0]:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Retorno(casa_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                pecas_capturadas[1] -= 1
                Tabuleiro.Print_Tabuleiro()
                return False
            # Somente dado 2 está apto a ser usado
            elif dado_val[1]:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                Retorno(casa_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                pecas_capturadas[1] -= 1
                Tabuleiro.Print_Tabuleiro()
                return False
            # Nenhum dado está apto a ser usado
            else:
                print("\n\u001b[4mNenhum valor permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                                "Passe a jogada =( \n")
                return False