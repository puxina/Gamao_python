# Função escrita para o programa
import Var
import Tabuleiro

###############################################
def dado_valido(d1, d2):
    """Verificação de quais dados são válidos para retornar a peça ao tabuleiro, conforme
       três possíveis condições de retorno: casa vazia, captura do oponente e casa com
       peças do jogador"""
    d1_val = False
    d2_val = False
    casa_d1_cond = 0
    casa_d2_cond = 0
    for cont in range(6):
        # Jogador 1 e Condição 1: Dado válido para retorno se a casa for vazia
        if Var.jog_1 and Var.pecas_posi[cont][0] == Var.pc_nula:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 1
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 1
        # Jogador 2 e Condição 1:: Dado válido para retorno se a casa for vazia
        elif Var.jog_2 and Var.pecas_posi[23-cont][0] == Var.pc_nula:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 1
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 1
        # Jogador 1 e Condição 2: Dado válido para retorno se a casa somente tiver uma
        # peça adversária, a qual será capturada
        elif Var.jog_1 and Var.pecas_posi[cont][0] == Var.pc_escura and Var.pecas_posi[cont][1] == Var.pc_nula:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 2
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 2
        # Jogador 2 e Condição 2: Dado válido para retorno se a casa somente tiver uma
        # peça adversária, a qual será capturada
        elif Var.jog_2 and Var.pecas_posi[23-cont][0] == Var.pc_clara and Var.pecas_posi[23-cont][1] == Var.pc_nula:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 2
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 2
        # Jogador 1 e Condição 3: Dado válido para retorno em uma casa que contém peças suas (brancas)
        elif Var.jog_1 and Var.pecas_posi[cont][0] == Var.pc_clara:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 3
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 3
        # Jogador 2 e Condição 3: Dado válido para retorno em uma casa que contém peças suas (pretas)
        elif Var.jog_2 and Var.pecas_posi[23-cont][0] == Var.pc_escura:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 3
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 3
    return d1_val, d2_val, casa_d1_cond, casa_d2_cond

###############################################
def peca_retorno(casa_cond, dado, pc_cap_cl, pc_cap_es):
    """Função para permutar a peça que será retornada ao tabuleiro, conforme a condição possível"""
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
        elif casa_cond == 3:
            for cont in range(len(Var.pecas_posi[dado-1])):
                if Var.pecas_posi[dado-1][cont] == Var.pc_clara:
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
        elif casa_cond == 3:
            for cont in range(len(Var.pecas_posi[dado-1])):
                if Var.pecas_posi[24-dado][cont] == Var.pc_escura:
                    pecas_casa += 1
            Var.pecas_posi[24-dado][pecas_casa], Var.pecas_capturadas_escuras[pc_cap_es-1] = Var.pecas_capturadas_escuras[pc_cap_es-1], Var.pecas_posi[24-dado][pecas_casa]
        return

###############################################
def peca_capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    pecas_capturadas = [0, 0]
    dado_val = [False, False]
    casa_dx_cond = [0, 0]

    for cont in range(5):
        if Var.pecas_capturadas_claras[cont] == Var.pc_clara:
            pecas_capturadas[0] += 1
        if Var.pecas_capturadas_escuras[cont] == Var.pc_escura:
            pecas_capturadas[1] += 1

    # Jogador 1
    if Var.jog_1:
        # Teste das condições 
        if pecas_capturadas[0] == 0:
            return True
        else:
            dado_val[0], dado_val[1], casa_dx_cond[0], casa_dx_cond[1] = dado_valido(d1, d2)
            # Condições de retorno conforme a validade dos dados:
            # 1 - Ambos os dados podem ser usados e o usuário irá escolher qual
            if Var.dado_usado == 0 and dado_val[0] and dado_val[1]:
                while True:
                    try:
                        print("\u001b[4mO valor ou de D1 ou de D2 permite retornar a peça capturada ao tabuleiro\u001b[0m")
                        dado_x = int(input("Escolha qual dado você deseja usar (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\n\u001b[41mValor inválido.\u001b[0m Repita a operação.\n")
                # Escolheu D1
                if dado_x == 1:
                    peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 1
                # Escolheu D2
                else:
                    peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 2
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    peca_capturada(d1, d2)
                    return False
            # 2 - Somente dado 1 está apto a ser usado
            elif Var.dado_usado != 1 and dado_val[0]:
                print("\u001b[4mO valor de D1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 1
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 3 - Somente dado 2 está apto a ser usado
            elif Var.dado_usado != 2 and dado_val[1]:
                print("\u001b[4mO valor de D2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 2
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 4 - Nenhum dado está apto a ser usado
            else:
                print("\u001b[4mNenhum valor dos dados permite retornar a peça capturada ao tabuleiro\n" +
                                "Passe a jogada =( \u001b[0m\n")
                return False
    # Jogador 2
    else:
        # Teste das condições 
        if pecas_capturadas[1] == 0:
            return True
        else:
            dado_val[0], dado_val[1], casa_dx_cond[0], casa_dx_cond[1] = dado_valido(d1, d2)
            # Condições de retorno conforme a validade dos dados:
            # 1 - Ambos os dados podem ser usados e o usuário irá escolher qual
            if Var.dado_usado == 0 and dado_val[0] and dado_val[1]:
                while True:
                    try:
                        print("\u001b[4mO valor ou de D1 ou de D2 permite retornar a peça capturada ao tabuleiro\u001b[0m")
                        dado_x = int(input("Escolha qual dado você deseja usar (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\n\u001b[41mValor inválido.\u001b[0m Repita a operação.\n")
                # Escolheu D1
                if dado_x == 1:
                    peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 1
                # Escolheu D2
                else:
                    peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    Var.dado_usado = 2
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    peca_capturada(d1, d2)
                    return False
            # 2 - Somente dado 1 está apto a ser usado
            elif Var.dado_usado != 1 and dado_val[0]:
                print("\u001b[4mO valor de D1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 1
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 3 - Somente dado 2 está apto a ser usado
            elif Var.dado_usado != 2 and dado_val[1]:
                print("\u001b[4mO valor de D2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                Var.dado_usado = 2
                Tabuleiro.print_tabuleiro()
                Var.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if Var.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 4 - Nenhum dado está apto a ser usado
            else:
                print("\u001b[4mNenhum valor dos dados permite retornar a peça capturada ao tabuleiro\n" +
                                "Passe a jogada =( \u001b[0m\n")
                return False