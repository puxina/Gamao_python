"""
Definição das variáveis globais
"""

from glob import glob

from jogadas import jogada_dados_diff

def init():
    """Função para inicializar as variáveis globais"""

    # Variáveis que determina a cores das peças
    # Círculo branco
    global pc_clara
    pc_clara = '\u001b[38;5;231m●' 
    # Círculo preto
    global pc_escura
    pc_escura = '\u001b[38;5;232m●'
    # Círculo pontilhado branco
    global pc_nula
    pc_nula = '\u001b[38;5;231m◌'
    # Barra azul
    global cs_clara
    cs_clara = '\u001b[34;1m|\u001b[0m'
    # Barra vermelha
    global cs_escura
    cs_escura = '\u001b[31;1m|\u001b[0m'
    # Barra verde
    global cs_meio
    cs_meio = '\u001b[32;1m|\u001b[0m'

    # Matriz com os elementos das peças distribuídas no tabuleiro
    global  pecas_posi
    """ pecas_posi = [[pc_clara, pc_nula, pc_nula, pc_nula, pc_nula],        [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_escura, pc_escura, pc_escura, pc_escura, pc_escura],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_escura, pc_escura, pc_escura, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_clara, pc_clara, pc_clara, pc_clara, pc_nula],
                  [pc_escura, pc_escura, pc_escura, pc_escura, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_clara, pc_clara, pc_clara, pc_nula, pc_nula],      [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_clara, pc_clara, pc_clara, pc_clara, pc_nula],     [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_clara, pc_nula, pc_nula, pc_nula, pc_nula],        [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],         [pc_escura, pc_nula, pc_nula, pc_nula, pc_nula]] """

    pecas_posi = [[pc_clara, pc_clara, pc_nula, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_escura, pc_escura, pc_escura, pc_escura, pc_escura],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_escura, pc_escura, pc_escura, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_clara, pc_clara, pc_clara, pc_clara, pc_clara],
                  [pc_escura, pc_escura, pc_escura, pc_escura, pc_escura], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_clara, pc_clara, pc_clara, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_clara, pc_clara, pc_clara, pc_clara, pc_clara], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula],
                  [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula], [pc_escura, pc_escura, pc_nula, pc_nula, pc_nula]]

    # Lista das peças capturadas
    global pecas_capturadas_claras
    """ pecas_capturadas_claras = [pc_clara, pc_clara, pc_nula, pc_nula, pc_nula] """
    pecas_capturadas_claras = [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula]

    global pecas_capturadas_escuras
    """ pecas_capturadas_escuras = [pc_escura, pc_escura, pc_nula, pc_nula, pc_nula] """
    pecas_capturadas_escuras = [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula]

    # Lista das peças que foram retiradas do jogo e suas variáveis que sinaliza o fim de jogo retirando as 15 peças
    global pecas_retiradas_claras
    pecas_retiradas_claras = [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula,
                              pc_nula, pc_nula, pc_nula, pc_nula, pc_nula,
                              pc_nula, pc_nula, pc_nula, pc_nula, pc_nula]
    global pecas_retiradas_escuras
    pecas_retiradas_escuras = [pc_nula, pc_nula, pc_nula, pc_nula, pc_nula,
                               pc_nula, pc_nula, pc_nula, pc_nula, pc_nula,
                               pc_nula, pc_nula, pc_nula, pc_nula, pc_nula]

    global pecas_retiradas_claras_quant
    pecas_retiradas_claras_quant = 0
    
    global pecas_retiradas_escuras_quant
    pecas_retiradas_escuras_quant = 0

    # Lista das peças sobrepostas por casa
    global pecas_sobre
    pecas_sobre = [[pc_nula]] * 24

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