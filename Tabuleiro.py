# Função das variáveis globais
import Var

def Print_Tabuleiro():
    """Definição da função que printa o tabuleiro e as peças na tela"""

    print("\u001b[37;1mPeças Escuras retiradas do jogo: \u001b[48;5;244m", end = '')
    for cont in range(15):
        print(Var.pecas_retiradas_escuras[cont], end = ' ')
    print("\u001b[0m")
    print("\u001b[37;1mPeças Claras retiradas do jogo: \u001b[48;5;244m", end = '')
    for cont in range(15):
        print(Var.pecas_retiradas_claras[cont], end = ' ')
    print("\u001b[0m\n")

    print("\u001b[1m     24   23   22   21   20   19        18   17   16   15   14   13\u001b[0m")
    # Topo do tabuleiro
    for linha in range(5):
        print("\u001b[1m", linha+1, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(6):
            if coluna % 2 == 0:
                print(Var.CS_CLARA + "\u001b[48;5;12m " + Var.pecas_posi[coluna][linha] + " \u001b[0m" + Var.CS_CLARA, end = '')
            else:
                print(Var.CS_ESCURA + "\u001b[48;5;9m " + Var.pecas_posi[coluna][linha] + " \u001b[0m" + Var.CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças claras capturadas
        print(Var.CS_MEIO + "\u001b[42;1m " + Var.pecas_capturadas_claras[linha] + " \u001b[0m" + Var.CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(6, 12):
            if coluna % 2 == 0:
                print(Var.CS_CLARA + "\u001b[48;5;12m " + Var.pecas_posi[coluna][linha] + " \u001b[0m" + Var.CS_CLARA, end = '')
            else:
                print(Var.CS_ESCURA + "\u001b[48;5;9m " + Var.pecas_posi[coluna][linha] + " \u001b[0m" + Var.CS_ESCURA, end = '')
        print()
    print()

    # Inferior do tabuleiro
    for linha in range(5, 0, -1):
        print("\u001b[1m", linha, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(23, 17, -1):
            if coluna % 2 == 0:
                print(Var.CS_CLARA + "\u001b[48;5;12m " + Var.pecas_posi[coluna][linha-1] + " \u001b[0m" + Var.CS_CLARA, end = '')
            else:
                print(Var.CS_ESCURA + "\u001b[48;5;9m " + Var.pecas_posi[coluna][linha-1] + " \u001b[0m" + Var.CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças escuras capturadas
        print(Var.CS_MEIO + "\u001b[42;1m " + Var.pecas_capturadas_escuras[linha-1] + " \u001b[0m" + Var.CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(17, 11, -1):
            if coluna % 2 == 0:
                print(Var.CS_CLARA + "\u001b[48;5;12m " + Var.pecas_posi[coluna][linha-1] + " \u001b[0m" + Var.CS_CLARA, end = '')
            else:
                print(Var.CS_ESCURA + "\u001b[48;5;9m " + Var.pecas_posi[coluna][linha-1] + " \u001b[0m" + Var.CS_ESCURA, end = '')
        print()
    print("\u001b[1m     01   02   03   04   05   06        07   08   09   10   11   12\u001b[0m\n")