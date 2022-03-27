# Funções do Pyhon
import random

# Função das variáveis globais
import var_global

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed()

def rola_dado(jogador):

    """Função que retorna, para o respectivo jogador, os valores de dados lançados para a jogada"""
    if var_global.jog_1:
        print(jogador + ", aperte enter para rolar os dados:")
        input()
    else:
        print(jogador + ", aperte enter para rolar os dados:")
        input()
    
    var_global.dado_1 = random.randint(1, 6)
    var_global.dado_2 = random.randint(1, 6)
    print("Resultado dos dados: D1 =", var_global.dado_1, "D2 =", var_global.dado_2, "\n")
    return