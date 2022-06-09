"""
Módulo para a impressão na tela da atual situação do tabuleiro/jogo

Função:
    * print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)
:
        Não recebe e nem retorna argumento algum
"""

from def_cores import *

def print_tabuleiro(pecas_posi, pecas_retiradas_escuras, pecas_retiradas_claras, pecas_capturadas_escuras, pecas_capturadas_claras, CS_CLARA, CS_ESCURA, CS_MEIO):
    """Definição da função que printa o tabuleiro e as peças na tela"""

    print(COR_BRANCO_BRILHANTE + "Peças Escuras retiradas do jogo: " + COR_FUNDO_CINZA, end = '')
    for cont in range(15):
        print(pecas_retiradas_escuras[cont], end = ' ')
    print(COR_RESETALL)
    print(COR_BRANCO_BRILHANTE + "Peças Claras retiradas do jogo: " + COR_FUNDO_CINZA, end = '')
    for cont in range(15):
        print(pecas_retiradas_claras[cont], end = ' ')
    print(COR_RESETALL + "\n")

    print(COR_NEGRITO + "     24   23   22   21   20   19        18   17   16   15   14   13" + COR_RESETALL)
    # Topo do tabuleiro
    for linha in range(5):
        print(COR_NEGRITO, linha+1, COR_RESETALL, end = '')
        # Lado esquerdo
        for coluna in range(6):
            if coluna % 2 == 0:
                print(CS_CLARA + COR_FUNDO_AZUL_CLARO + " " + pecas_posi[coluna][linha] + " " + COR_RESETALL + CS_CLARA, end = '')
            else:
                print(CS_ESCURA + COR_FUNDO_VERM_CLARO + " " + pecas_posi[coluna][linha] + " " + COR_RESETALL + CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças claras capturadas
        print(CS_MEIO + COR_FUNDO_VERDE_BRIL + " " + pecas_capturadas_claras[linha] + " " + COR_RESETALL + CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(6, 12):
            if coluna % 2 == 0:
                print(CS_CLARA + COR_FUNDO_AZUL_CLARO + " " + pecas_posi[coluna][linha] + " " + COR_RESETALL + CS_CLARA, end = '')
            else:
                print(CS_ESCURA + COR_FUNDO_VERM_CLARO + " " + pecas_posi[coluna][linha] + " " + COR_RESETALL + CS_ESCURA, end = '')
        print()
    print()

    # Inferior do tabuleiro
    for linha in range(5, 0, -1):
        print(COR_NEGRITO, linha, COR_RESETALL, end = '')
        # Lado esquerdo
        for coluna in range(23, 17, -1):
            if coluna % 2 == 0:
                print(CS_CLARA + COR_FUNDO_AZUL_CLARO + " " + pecas_posi[coluna][linha-1] + " " + COR_RESETALL + CS_CLARA, end = '')
            else:
                print(CS_ESCURA + COR_FUNDO_VERM_CLARO + " " + pecas_posi[coluna][linha-1] + " " + COR_RESETALL + CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças escuras capturadas
        print(CS_MEIO + COR_FUNDO_VERDE_BRIL + " " + pecas_capturadas_escuras[linha-1] + " " + COR_RESETALL + CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(17, 11, -1):
            if coluna % 2 == 0:
                print(CS_CLARA + COR_FUNDO_AZUL_CLARO + " " + pecas_posi[coluna][linha-1] + " " + COR_RESETALL + CS_CLARA, end = '')
            else:
                print(CS_ESCURA + COR_FUNDO_VERM_CLARO + " " + pecas_posi[coluna][linha-1] + " " + COR_RESETALL + CS_ESCURA, end = '')
        print()
    print(COR_NEGRITO + "     01   02   03   04   05   06        07   08   09   10   11   12" + COR_RESETALL + "\n")