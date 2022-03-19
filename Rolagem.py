# Funções do Pyhon
import random
import os

# Função das variáveis globais
import Var

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed(os.urandom(1))

def Rola_Dado(jogador):

    """Função que retorna, para o respectivo jogador, os valores de dados lançados para a jogada"""
    if Var.jog_1:
        print(jogador + ", aperte enter para rolar os dados:", end = '')
        input()
    else:
        print(jogador + ", aperte enter para rolar os dados:", end = '')
        input()
    
    return random.randint(1, 6), random.randint(1, 6)