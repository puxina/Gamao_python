"""
Definição das variáveis globais
"""

from glob import glob

from jogadas import jogada_dados_diff

from def_cores import *

# Variáveis que determina a cores das peças
# Círculo branco
PC_CLARA = COR_BRANCO + "●" 
# Círculo preto
PC_ESCURA = COR_PRETO + "●"
# Círculo pontilhado branco
PC_NULA = COR_BRANCO + "◌"
# Barra azul
CS_CLARA = COR_AZUL + "|" + COR_RESETALL
# Barra vermelha
CS_ESCURA = COR_VERMELHO + "|" + COR_RESETALL
# Barra verde
CS_MEIO = COR_VERDE + "|" + COR_RESETALL

# Matriz com os elementos das peças distribuídas no tabuleiro
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
pecas_capturadas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

pecas_capturadas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

# Lista das peças que foram retiradas do jogo e suas variáveis que sinaliza o fim de jogo retirando as 15 peças
pecas_retiradas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                            PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                            PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
pecas_retiradas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                            PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                            PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

pecas_retiradas_claras_quant = 0

pecas_retiradas_escuras_quant = 0

# Lista das peças sobrepostas por casa
pecas_sobre = [[PC_NULA]] * 24

pecas_sobre_quant = [1] * 24

# Variáveis da quantidade de peças na casa campo do jogador
pecas_casa_campo_clara = 0

pecas_casa_campo_escura = 0

# Variáveis dos valores de dados
dado_1 = 1
dado_2 = 1

# Variável que sinaliza qual dado foi usado para o retorno de uma peça capturada
# ou para o movimento de uma peça
dado_usado = 0

# Variável para contar a quantidade de jogadas
cont_jogadas = 0

# Variáveis para sinalizar quem é o jogador da vez
jog_1 = True
jog_2 = False

# Variáveis contendo os nomes dos jogadores
jogador_1 = ""
jogador_2 = ""