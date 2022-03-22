from glob import glob

def init():
    """Função para definição das variáveis globais"""

    # Variáveis que determina a cores das peças
    # Círculo branco
    global PC_CLARA
    PC_CLARA = '\u001b[38;5;231m●' 
    # Círculo preto
    global PC_ESCURA
    PC_ESCURA = '\u001b[38;5;232m●'
    # Círculo pontilhado branco
    global PC_NULA
    PC_NULA = '\u001b[38;5;231m◌'
    # Barra azul
    global CS_CLARA
    CS_CLARA = '\u001b[34;1m|\u001b[0m'
    # Barra vermelha
    global CS_ESCURA
    CS_ESCURA = '\u001b[31;1m|\u001b[0m'
    # Barra verde
    global CS_MEIO
    CS_MEIO = '\u001b[32;1m|\u001b[0m'

    # Matriz com os elementos das peças distribuídas no tabuleiro
    global  pecas_posi
    pecas_posi = [[PC_CLARA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],        [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
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
                  [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],         [PC_ESCURA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]]

    # Lista das peças capturadas
    global pecas_capturadas_claras
    pecas_capturadas_claras = [PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA]
    global pecas_capturadas_escuras
    pecas_capturadas_escuras = [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA]

    # Lista das peças que foram retiradas do jogo e que sinaliza o fim de jogo retirando as 15 peças
    global pecas_retiradas_claras
    pecas_retiradas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                              PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                              PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
    global pecas_retiradas_escuras
    pecas_retiradas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                               PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                               PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

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
    global jogador_2