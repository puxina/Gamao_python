"""
Módulo relacionado ao lançamento dos dados

Funções:
    * print_dado:
        Mostra na tela o valor do dado em formato de imagem ascii

    * rola_dado(jogador):
        Rola os dois dados para a jogada
"""

# Funções do Pyhon
import random

# Função das variáveis globais
import var_global

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed()

###############################################
def print_dado():
    """Função para imprimir na tela a figura do dado e retorna seu valor"""
    valor = random.randint(1, 6)
    if valor == 1:
        print(" ---------\n",
              "|       |\n",
              "|   ○   |\n",
              "|       |\n",
              "---------\n")
    elif valor == 2:
        print(" ---------\n",
              "|     ○ |\n",
              "|       |\n",
              "| ○     |\n",
              "---------\n")
    elif valor == 3:
        print(" ---------\n",
              "|     ○ |\n",
              "|   ○   |\n",
              "| ○     |\n",
              "---------\n")
    elif valor == 4:
        print(" ---------\n",
              "| ○   ○ |\n",
              "|       |\n",
              "| ○   ○ |\n",
              "---------\n")
    elif valor == 5:
        print(" ---------\n",
              "| ○   ○ |\n",
              "|   ○   |\n",
              "| ○   ○ |\n",
              "---------\n")
    else:
        print(" ---------\n",
              "| ○   ○ |\n",
              "| ○   ○ |\n",
              "| ○   ○ |\n",
              "---------\n")
    
    return valor

###############################################
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