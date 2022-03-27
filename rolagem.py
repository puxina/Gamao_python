# Funções do Pyhon
import random

# Função das variáveis globais
import Var

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed()

def rola_dado(jogador):

    """Função que retorna, para o respectivo jogador, os valores de dados lançados para a jogada"""
    if Var.jog_1:
        print(jogador + ", aperte enter para rolar os dados:")
        input()
    else:
        print(jogador + ", aperte enter para rolar os dados:")
        input()
    
    Var.dado_1 = random.randint(1, 6)
    Var.dado_2 = random.randint(1, 6)
    print("Resultado dos dados: D1 =", Var.dado_1, "D2 =", Var.dado_2, "\n")
    return