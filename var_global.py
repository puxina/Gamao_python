"""
Definição das variáveis globais
"""

from glob import glob

from jogadas import jogada_dados_diff

from def_cores import *

def init():
    """Função para inicializar as variáveis globais"""

    # Variáveis que determina a cores das peças
    # Círculo branco
    global PC_CLARA
    PC_CLARA = COR_BRANCO + "●" 
    # Círculo preto
    global PC_ESCURA
    PC_ESCURA = COR_PRETO + "●"
    # Círculo pontilhado branco
    global PC_NULA
    PC_NULA = COR_BRANCO + "◌"
    # Barra azul
    global CS_CLARA
    CS_CLARA = COR_AZUL + "|" + COR_RESETALL
    # Barra vermelha
    global CS_ESCURA
    CS_ESCURA = COR_VERMELHO + "|" + COR_RESETALL
    # Barra verde
    global CS_MEIO
    CS_MEIO = COR_VERDE + "|" + COR_RESETALL

    # Matriz com os elementos das peças distribuídas no tabuleiro
    global  pecas_posi
    """ pecas_posi = [[PC_CLARA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],        [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA],
                  [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA, PC_NULA],      [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA],     [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_CLARA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],        [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_ESCURA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]] """

    pecas_posi = [[PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA],
                  [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA]]

    # Lista das peças capturadas
    global pecas_capturadas_claras
    """ pecas_capturadas_claras = [PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA] """
    pecas_capturadas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

    global pecas_capturadas_escuras
    """ pecas_capturadas_escuras = [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA] """
    pecas_capturadas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

    # Lista das peças que foram retiradas do jogo e suas variáveis que sinaliza o fim de jogo retirando as 15 peças
    global pecas_retiradas_claras
    pecas_retiradas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                              PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                              PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
    global pecas_retiradas_escuras
    pecas_retiradas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                               PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                               PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

    global pecas_retiradas_claras_quant
    pecas_retiradas_claras_quant = 0
    
    global pecas_retiradas_escuras_quant
    pecas_retiradas_escuras_quant = 0

    # Lista das peças sobrepostas por casa
    global pecas_sobre
    pecas_sobre = [[PC_NULA]] * 24

    global pecas_sobre_quant
    pecas_sobre_quant = [1] * 24

    # Variáveis da quantidade de peças na casa campo do jogador
    global pecas_casa_campo_clara
    pecas_casa_campo_clara = 0
    
    global pecas_casa_campo_escura
    pecas_casa_campo_escura = 0

    # Variáveis dos valores de dados
    global dado_1
    dado_1 = 1
    global dado_2
    dado_2 = 1

    # Variável que sinaliza qual dado foi usado para o retorno de uma peça capturada
    # ou para o movimento de uma peça
    global dado_usado
    dado_usado = 0

    # Variável para contar a quantidade de jogadas
    global cont_jogadas
    cont_jogadas = 0

    # Variáveis para sinalizar quem é o jogador da vez
    global jog_1
    jog_1 = True
    global jog_2
    jog_2 = False

    # Variáveis contendo os nomes dos jogadores
    global jogador_1
    jogador_1 = ""
    global jogador_2
    jogador_2 = ""