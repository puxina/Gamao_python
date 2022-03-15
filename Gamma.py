import random
import os

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed(os.urandom(1))

# Variáveis que determina a cores das peças
PC_CLARA = '\u001b[33;1m●\u001b[0m'  # Círculo amarelo
PC_ESCURA = '\u001b[32;1m●\u001b[0m' # Círculo verde
PC_NULA = '\u001b[37;1m◌\u001b[0m'   # Círculo pontilhado branco
CS_CLARA = '\u001b[34;1m|\u001b[0m'  # Barra azul
CS_ESCURA = '\u001b[31;1m|\u001b[0m' # Barra vermelha
CS_MEIO = '\u001b[37;1m|\u001b[0m'   # Barra branca

# Variável para movimento de uma peça, com casa e linha
peca = [1, 1]

# Matriz com os elementos peças distribuídas no tabuleiro
pecas_posi = [[PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA],
              [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA]]

pecas_capturadas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
pecas_capturadas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

pecas_retiradas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                          PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                          PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
pecas_retiradas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                           PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                           PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

# Variáveis dos valores de dados
Dado_1 = 1
Dado_2 = 1

# Variáveis jogador da vez
Jog_1 = True
Jog_2 = False

################################################################################################
################################################################################################

def Print_Tabuleiro():
    """Definição da função que printa o tabuleiro e as peças na tela"""

    print("Peças Escuras retiradas do jogo: ", end =  '')
    for cont in range(15):
        print(pecas_retiradas_escuras[cont], end = ' ')
    print()
    print("Peças Claras retiradas do jogo: ", end =  '')
    for cont in range(15):
        print(pecas_retiradas_claras[cont], end = ' ')
    print("\n")

    print("\u001b[1m     24   23   22   21   20   19        18   17   16   15   14   13\u001b[0m")
    # Topo do tabuleiro
    for linha in range(5):
        print("\u001b[1m", linha+1, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(6):
            if coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha], CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças claras capturadas
        print(CS_MEIO, pecas_capturadas_claras[linha], CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(6, 12):
            if coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha], CS_ESCURA, end = '')
        print()
    print()

    # Inferior do tabuleiro
    for linha in range(5, 0, -1):
        print("\u001b[1m", linha, "\u001b[0m", end = '')
        # Lado esquerdo
        for coluna in range(23, 17, -1):
            if coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha-1], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha-1], CS_ESCURA, end = '')
        
        # Meio do tabuleiro para as peças escuras capturadas
        print(CS_MEIO, pecas_capturadas_escuras[linha-1], CS_MEIO, end = '')
        
        # Lado direito
        for coluna in range(17, 11, -1):
            if coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha-1], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha-1], CS_ESCURA, end = '')
        print()
    print("\u001b[1m     01   02   03   04   05   06        07   08   09   10   11   12\u001b[0m\n")

################################################################################################
################################################################################################

def Rola_Dado():
    """Função que retorna, para o respectivo jogador, os valores de dados lançados para a jogada"""
    if Jog_1:
        print(Jogador_1 + ", aperte enter para rolar os dados:", end = '')
        input()
    else:
        print(Jogador_2 + ", aperte enter para rolar os dados:", end = '')
        input()
    
    return random.randint(1, 6), random.randint(1, 6)

################################################################################################
################################################################################################

def Opcoes(D1, D2):
    """Função para indicar as várias opções disponíveis do uso dos dados ao jogador"""
    if D1 == D2:
        while True:
            try:
                print("\nSelecione uma das opções de jogadas disponíveis abaixo:\n")
                print("1 - A soma dos dados")
                print("2 - Dado D1+D2")
                print("3 - Dado D2+D3")
                print("4 - Dado D3+D4\n")
                opcao = int(input("Opção: "))
                if opcao < 1 or opcao > 4:
                    raise ValueError
                else:
                    return opcao
            except ValueError:
                print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
    else:
        while True:
            try:
                print("\nSelecione uma das opções de jogadas disponíveis abaixo:\n")
                print("1 - A soma dos dados")
                print("2 - Dado D1")
                print("3 - Dado D2\n")
                opcao = int(input("Opção: "))
                if opcao < 1 or opcao > 3:
                    raise ValueError
                else:
                    return opcao
            except ValueError:
                print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")

################################################################################################
################################################################################################

def Dado():
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

################################################################################################
################################################################################################

# Desenvolvimento do jogo    
print("\u001b[1m\u001b[46;1m Bem vindo ao jogo do gamão \u001b[0m\n")

# Seleção do primeiro jogador, o qual terá as peças claras (amarelas)
print("Escolha um entre os dois jogadores para lançar primeiro o dado.\nAquele que obtiver o maior número será o primeiro jogador\n")
while True:
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Dado_1 = Dado()
    
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Dado_2 = Dado()
    
    if Dado_1 == Dado_2:
        print("Empate nos dados. Repita o lançamento\n")
    else:
        break

if Dado_1 > Dado_2:
    print("A primeira pessoa que jogou o dado irá iniciar o jogo com as peças amarelas\n")
else:
    print("A segunda pessoa que jogou o dado irá iniciar o jogo com as peças amarelas\n")

Jogador_1 = input("Jogador 1, entre com seu nome: ")
Jogador_2 = input("\nJogador 2, entre com seu nome: ")

print("\n\u001b[4mQue vença o melhor entre", Jogador_1, "e", Jogador_2, "\u001b[0m\n")
Print_Tabuleiro()

while True:
    while Jog_1:
        Dado_1, Dado_2 = Rola_Dado()
        print("\nResultado dos dados: D1 =", Dado_1, "D2 =", Dado_2)
        Opcoes(Dado_1, Dado_2)

        while True:
            peca = [int(item) for item in input("Selecione a peça que você deseja mover (casa e linha): ").split()]
            
            if len(peca) > 2:
                print("\u001b[41mValor inválido:\u001b[0m Mais de dois valores. Repita a operação.\n")
            elif peca[1] == 0 or peca[1] > 5:
                print("\u001b[41mValor inválido:\u001b[0m Valor de linha inválido. Repita a operação.\n")
            elif peca[0] == 0 or peca[0] > 24:
                print("\u001b[41mValor inválido:\u001b[0m Valor de casa inválido. Repita a operação.\n")
            elif pecas_posi[24-peca[0]][peca[1]-1] == PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou um espaço vazio. Tente novamente\n")
            elif pecas_posi[24-peca[0]][peca[1]-1] == PC_ESCURA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a peça do adversário. Tente novamente\n")
            else:
                print("Funfou")
                Jog_1 = False
                Jog_2 = True
                Print_Tabuleiro()
                break
   
    while Jog_2:
        Dado_1, Dado_2 = Rola_Dado()
        print("\nResultado dos dados: D1 =", Dado_1, "D2 =", Dado_2)
        Opcoes(Dado_1, Dado_2)

        while True:
            peca = [int(item) for item in input("Selecione a peça que você deseja mover (casa e linha): ").split()]
            
            if len(peca) > 2:
                print("\u001b[41mValor inválido:\u001b[0m Mais de dois valores. Repita a operação.\n")
            elif peca[1] == 0 or peca[1] > 5:
                print("\u001b[41mValor inválido:\u001b[0m Valor de linha inválido. Repita a operação.\n")
            elif peca[0] == 0 or peca[0] > 24:
                print("\u001b[41mValor inválido:\u001b[0m Valor de casa inválido. Repita a operação.\n")
            elif pecas_posi[24-peca[0]][peca[1]-1] == PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou um espaço vazio. Tente novamente\n")
            elif pecas_posi[24-peca[0]][peca[1]-1] == PC_CLARA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a peça do adversário. Tente novamente\n")
            else:
                print("Funfou")
                Jog_1 = True
                Jog_2 = False
                Print_Tabuleiro()
                break

        
