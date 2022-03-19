# Funções do Pyhon
import random
import os

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed(os.urandom(1))

def Print_Dado():
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