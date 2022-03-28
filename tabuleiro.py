"""
Módulo para a impressão na tela da atual situação do tabuleiro/jogo

Função:
    * print_tabuleiro():
        Não recebe e nem retorna argumento algum
"""

# Função das variáveis globais
import var_global

def print_tabuleiro():
    """Definição da função que printa o tabuleiro e as peças na tela"""

    print("\u001b[37;1mPeças Escuras retiradas do jogo: \u001b[48;5;244m", end = '')
    for cont in range(15):
        print(var_global.pecas_retiradas_escuras[cont], end = ' ')
    print("\u001b[0m")
    print("\u001b[37;1mPeças Claras retiradas do jogo: \u001b[48;5;244m", end = '')
    for cont in range(15):
        print(var_global.pecas_retiradas_claras[cont], end = ' ')
    print("\u001b[0m\n")

    print("\u001b[1m     24   23   22   21   20   19        18   17   16   15   14   13\u001b[0m")
    # Topo do tabuleiro
    for linha in range(5):
        print("\u001b[1m", linha+1, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(6):
            if coluna % 2 == 0:
                print(var_global.cs_clara + "\u001b[48;5;12m " + var_global.pecas_posi[coluna][linha] + " \u001b[0m" + var_global.cs_clara, end = '')
            else:
                print(var_global.cs_escura + "\u001b[48;5;9m " + var_global.pecas_posi[coluna][linha] + " \u001b[0m" + var_global.cs_escura, end = '')
        
        # Meio do tabuleiro para as peças claras capturadas
        print(var_global.cs_meio + "\u001b[42;1m " + var_global.pecas_capturadas_claras[linha] + " \u001b[0m" + var_global.cs_meio, end = '')
        
        # Lado direito
        for coluna in range(6, 12):
            if coluna % 2 == 0:
                print(var_global.cs_clara + "\u001b[48;5;12m " + var_global.pecas_posi[coluna][linha] + " \u001b[0m" + var_global.cs_clara, end = '')
            else:
                print(var_global.cs_escura + "\u001b[48;5;9m " + var_global.pecas_posi[coluna][linha] + " \u001b[0m" + var_global.cs_escura, end = '')
        print()
    print()

    # Inferior do tabuleiro
    for linha in range(5, 0, -1):
        print("\u001b[1m", linha, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(23, 17, -1):
            if coluna % 2 == 0:
                print(var_global.cs_clara + "\u001b[48;5;12m " + var_global.pecas_posi[coluna][linha-1] + " \u001b[0m" + var_global.cs_clara, end = '')
            else:
                print(var_global.cs_escura + "\u001b[48;5;9m " + var_global.pecas_posi[coluna][linha-1] + " \u001b[0m" + var_global.cs_escura, end = '')
        
        # Meio do tabuleiro para as peças escuras capturadas
        print(var_global.cs_meio + "\u001b[42;1m " + var_global.pecas_capturadas_escuras[linha-1] + " \u001b[0m" + var_global.cs_meio, end = '')
        
        # Lado direito
        for coluna in range(17, 11, -1):
            if coluna % 2 == 0:
                print(var_global.cs_clara + "\u001b[48;5;12m " + var_global.pecas_posi[coluna][linha-1] + " \u001b[0m" + var_global.cs_clara, end = '')
            else:
                print(var_global.cs_escura + "\u001b[48;5;9m " + var_global.pecas_posi[coluna][linha-1] + " \u001b[0m" + var_global.cs_escura, end = '')
        print()
    print("\u001b[1m     01   02   03   04   05   06        07   08   09   10   11   12\u001b[0m\n")