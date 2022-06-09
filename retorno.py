"""
Módulo para tratar se há ou não peça(s) para retornar, verificando
a condição e realizando o retorno, caso esse seja válido. Em caso
de sobrar ainda um dado para ser usado em movimento, será sinali-
zado e a jogada será executada conforme o dado que sobrou dentro
do módulo jogadas.py

Funções:
    * dado_valido(d1, d2):
        Recebe os valores dos dados e retorna se os dados são 
        válidos e para quais condições (casa vazia, captura ou
        casa com peças do jogador)
    
    * peca_retorno(casa_cond, dado, pc_cap_cl, pc_cap_es):
        Recebe o tipo de condição de retorno, o valor do dado e,
        se há peça para capturar, sua posição. Realiza a permuta
    
    * peca_capturada(d1, d2):
        Recebe os valores dos dados e determina se há peças capturadas
        para que elas possam ser retornadas
"""

# Função escrita para o programa
import var_global
from def_cores import *
import tabuleiro

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
        if var_global.jog_1 and var_global.pecas_posi[cont][0] == var_global.PC_NULA:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 1
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 1
        # Jogador 2 e Condição 1:: Dado válido para retorno se a casa for vazia
        elif var_global.jog_2 and var_global.pecas_posi[23-cont][0] == var_global.PC_NULA:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 1
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 1
        # Jogador 1 e Condição 2: Dado válido para retorno se a casa somente tiver uma
        # peça adversária, a qual será capturada
        elif var_global.jog_1 and var_global.pecas_posi[cont][0] == var_global.PC_ESCURA and var_global.pecas_posi[cont][1] == var_global.PC_NULA:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 2
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 2
        # Jogador 2 e Condição 2: Dado válido para retorno se a casa somente tiver uma
        # peça adversária, a qual será capturada
        elif var_global.jog_2 and var_global.pecas_posi[23-cont][0] == var_global.PC_CLARA and var_global.pecas_posi[23-cont][1] == var_global.PC_NULA:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 2
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 2
        # Jogador 1 e Condição 3: Dado válido para retorno em uma casa que contém peças suas (brancas)
        elif var_global.jog_1 and var_global.pecas_posi[cont][0] == var_global.PC_CLARA:
            if d1 == (cont+1):
                d1_val = True
                casa_d1_cond = 3
            if d2 == (cont+1):
                d2_val = True
                casa_d2_cond = 3
        # Jogador 2 e Condição 3: Dado válido para retorno em uma casa que contém peças suas (pretas)
        elif var_global.jog_2 and var_global.pecas_posi[23-cont][0] == var_global.PC_ESCURA:
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
    if var_global.jog_1:
        # Dado válido para retorno se a casa for vazia
        if casa_cond == 1:
            var_global.pecas_posi[dado-1][0], var_global.pecas_capturadas_claras[pc_cap_cl-1] = var_global.pecas_capturadas_claras[pc_cap_cl-1], var_global.pecas_posi[dado-1][0]
        # Dado válido para retorno se a casa somente tiver uma peça adversária,
        # a qual será capturada
        elif casa_cond == 2:
            var_global.pecas_posi[dado-1][0], var_global.pecas_capturadas_escuras[pc_cap_es] = var_global.pecas_capturadas_escuras[pc_cap_es], var_global.pecas_posi[dado-1][0]
            var_global.pecas_posi[dado-1][0], var_global.pecas_capturadas_claras[pc_cap_cl-1] = var_global.pecas_capturadas_claras[pc_cap_cl-1], var_global.pecas_posi[dado-1][0]
        # Dado válido para retorno em uma casa que contém peças suas (brancas)
        elif casa_cond == 3:
            for cont in range(len(var_global.pecas_posi[dado-1])):
                if var_global.pecas_posi[dado-1][cont] == var_global.PC_CLARA:
                    pecas_casa += 1
            var_global.pecas_posi[dado-1][pecas_casa], var_global.pecas_capturadas_claras[pc_cap_cl-1] = var_global.pecas_capturadas_claras[pc_cap_cl-1], var_global.pecas_posi[dado-1][pecas_casa]
        return
    # Jogador 2
    else:
        # Dado válido para retorno se a casa for vazia
        if casa_cond == 1:
            var_global.pecas_posi[24-dado][0], var_global.pecas_capturadas_escuras[pc_cap_es-1] = var_global.pecas_capturadas_escuras[pc_cap_es-1], var_global.pecas_posi[24-dado][0]
        # Dado válido para retorno se a casa somente tiver uma peça adversária,
        # a qual será capturada
        elif casa_cond == 2:
            var_global.pecas_posi[24-dado][0], var_global.pecas_capturadas_claras[pc_cap_cl] = var_global.pecas_capturadas_claras[pc_cap_cl], var_global.pecas_posi[24-dado][0]
            var_global.pecas_posi[24-dado][0], var_global.pecas_capturadas_escuras[pc_cap_es-1] = var_global.pecas_capturadas_escuras[pc_cap_es-1], var_global.pecas_posi[24-dado][0]
        # Dado válido para retorno em uma casa que contém peças suas (brancas)
        elif casa_cond == 3:
            for cont in range(len(var_global.pecas_posi[dado-1])):
                if var_global.pecas_posi[24-dado][cont] == var_global.PC_ESCURA:
                    pecas_casa += 1
            var_global.pecas_posi[24-dado][pecas_casa], var_global.pecas_capturadas_escuras[pc_cap_es-1] = var_global.pecas_capturadas_escuras[pc_cap_es-1], var_global.pecas_posi[24-dado][pecas_casa]
        return

###############################################
def peca_capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    pecas_capturadas = [0, 0]
    dado_val = [False, False]
    casa_dx_cond = [0, 0]

    for cont in range(5):
        if var_global.pecas_capturadas_claras[cont] == var_global.PC_CLARA:
            pecas_capturadas[0] += 1
        if var_global.pecas_capturadas_escuras[cont] == var_global.PC_ESCURA:
            pecas_capturadas[1] += 1

    # Jogador 1
    if var_global.jog_1:
        # Teste das condições 
        if pecas_capturadas[0] == 0:
            return True
        else:
            dado_val[0], dado_val[1], casa_dx_cond[0], casa_dx_cond[1] = dado_valido(d1, d2)
            # Condições de retorno conforme a validade dos dados:
            # 1 - Ambos os dados podem ser usados e o usuário irá escolher qual
            if var_global.dado_usado == 0 and dado_val[0] and dado_val[1]:
                while True:
                    try:
                        print(COR_SUBLINHADO + "O valor ou de D1 ou de D2 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL)
                        dado_x = int(input("Escolha qual dado você deseja usar (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\n" + COR_FUNDO_VERMELHO + "Valor inválido." + COR_RESETALL + " Repita a operação.\n")
                # Escolheu D1
                if dado_x == 1:
                    peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    var_global.dado_usado = 1
                # Escolheu D2
                else:
                    peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    var_global.dado_usado = 2
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    peca_capturada(d1, d2)
                    return False
            # 2 - Somente dado 1 está apto a ser usado
            elif var_global.dado_usado != 1 and dado_val[0]:
                print(COR_SUBLINHADO + "O valor de D1 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL + "\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                var_global.dado_usado = 1
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 3 - Somente dado 2 está apto a ser usado
            elif var_global.dado_usado != 2 and dado_val[1]:
                print(COR_SUBLINHADO + "O valor de D2 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL + "\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                var_global.dado_usado = 2
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[0] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 4 - Nenhum dado está apto a ser usado
            else:
                print(COR_SUBLINHADO + "Nenhum valor dos dados permite retornar a peça capturada ao tabuleiro\n" +
                                "Passe a jogada =(" + COR_RESETALL + "\n")
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
            if var_global.dado_usado == 0 and dado_val[0] and dado_val[1]:
                while True:
                    try:
                        print(COR_SUBLINHADO + "O valor ou de D1 ou de D2 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL)
                        dado_x = int(input("Escolha qual dado você deseja usar (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            print()
                            break
                    except ValueError:
                        print("\n" + COR_FUNDO_VERMELHO + "Valor inválido." + COR_RESETALL + " Repita a operação.\n")
                # Escolheu D1
                if dado_x == 1:
                    peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                    var_global.dado_usado = 1
                # Escolheu D2
                else:
                    peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                    var_global.dado_usado = 2
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    peca_capturada(d1, d2)
                    return False
            # 2 - Somente dado 1 está apto a ser usado
            elif var_global.dado_usado != 1 and dado_val[0]:
                print(COR_SUBLINHADO + "O valor de D1 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL + "\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[0], d1, pecas_capturadas[0], pecas_capturadas[1])
                var_global.dado_usado = 1
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 3 - Somente dado 2 está apto a ser usado
            elif var_global.dado_usado != 2 and dado_val[1]:
                print(COR_SUBLINHADO + "O valor de D2 permite retornar a peça capturada ao tabuleiro" + COR_RESETALL + "\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                peca_retorno(casa_dx_cond[1], d2, pecas_capturadas[0], pecas_capturadas[1])
                var_global.dado_usado = 2
                tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)

                var_global.cont_jogadas += 1
                if pecas_capturadas[1] == 1:
                    if var_global.cont_jogadas == 2:
                        return False
                    else:
                        return True
                else:
                    return False
            # 4 - Nenhum dado está apto a ser usado
            else:
                print(COR_SUBLINHADO + "Nenhum valor dos dados permite retornar a peça capturada ao tabuleiro\n" +
                                "Passe a jogada =(" + COR_RESETALL + "\n")
                return False