from pickle import FALSE, TRUE
import random
import os

# Seed para geração aleatória dos números obtido do sistema Windows
random.seed(os.urandom(1))

# Variáveis que determina a cores das peças
PC_CLARA = '\u001b[37;1m●\u001b[0m'      # Círculo branco
PC_ESCURA = '\u001b[38;5;202m●\u001b[0m' # Círculo laranja
PC_NULA = '\u001b[37;1m◌\u001b[0m'       # Círculo pontilhado branco
CS_CLARA = '\u001b[34;1m|\u001b[0m'      # Barra azul
CS_ESCURA = '\u001b[31;1m|\u001b[0m'     # Barra vermelha
CS_MEIO = '\u001b[37;1m|\u001b[0m'       # Barra branca

# Matriz com os elementos peças distribuídas no tabuleiro
pecas_posi = [[PC_CLARA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA],
              [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]]

pecas_capturadas_claras = [PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA]
pecas_capturadas_escuras = [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA]

pecas_retiradas_claras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                          PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                          PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]
pecas_retiradas_escuras = [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                           PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA,
                           PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA]

# Variáveis dos valores de dados
dado_1 = 1
dado_2 = 1

# Variáveis jogador da vez
jog_1 = True
jog_2 = False

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
    if jog_1:
        print(Jogador_1 + ", aperte enter para rolar os dados:", end = '')
        input()
    else:
        print(Jogador_2 + ", aperte enter para rolar os dados:", end = '')
        input()
    
    return random.randint(1, 6), random.randint(1, 6)

################################################################################################
################################################################################################

def Opcoes(d1, d2):
    """Função para indicar as várias opções disponíveis do uso dos dados ao jogador"""
    if d1 == d2:
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
                print("\u001b[41mOpção inválida.\u001b[0m Repita a operação.")
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
                print("\u001b[41mOpção inválida.\u001b[0m Repita a operação.")

################################################################################################
################################################################################################

def Peca_Capturada(d1, d2):
    """Função para determinar se há peças capturadas dos jogadores e quais valores valores de dados usará para
       o retorno da peça ao tabuleiro"""

    global jog_1, jog_2
    # Jogador 1
    if jog_1:
        # Contagem de quantas peças claras foram capturadas
        pecas_capturadas = 0
        for cont in range(5):
            if pecas_capturadas_claras[cont] == PC_CLARA:
                pecas_capturadas += 1

        # Teste das condições 
        if pecas_capturadas == 0:
            return False
        else:
            casas_bahia = []
            d1_valido = False
            d2_valido = False
            for cont in range(6):
                if pecas_posi[cont][0] == PC_NULA:
                    casas_bahia.append(True)
                    if d1 == (cont+1):
                        d1_valido = True
                    if d2 == (cont+1):
                        d2_valido = True
                else:
                    casas_bahia.append(False)
            
            if d1_valido and d2_valido:
                print("\n\u001b[4mOs valores de Dado 1 e Dado 2 permitem retornar a peça capturada ao tabuleiro\u001b[0m")
                while True:
                    try:
                        dado_x = int(input("Escolha qual Dado você deseja (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
                if dado_x == 1:
                    pecas_posi[d1-1][0], pecas_capturadas_claras[pecas_capturadas-1] = pecas_capturadas_claras[pecas_capturadas-1], pecas_posi[d1-1][0]
                else:
                    pecas_posi[d2-1][0], pecas_capturadas_claras[pecas_capturadas-1] = pecas_capturadas_claras[pecas_capturadas-1], pecas_posi[d2-1][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False
                else:
                    Peca_Capturada(d1, d2)
            elif d1_valido:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                pecas_posi[d1-1][0], pecas_capturadas_claras[pecas_capturadas-1] = pecas_capturadas_claras[pecas_capturadas-1], pecas_posi[d1-1][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False
                else:
                    Peca_Capturada(d1, d2)
            elif d2_valido:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                pecas_posi[d2-1][0], pecas_capturadas_claras[pecas_capturadas-1] = pecas_capturadas_claras[pecas_capturadas-1], pecas_posi[d2-1][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False
                else:
                    Peca_Capturada(d1, d2)
            else:
                print("\n\u001b[4mNenhum dos dois valores permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Passe a jogada =( \n")
                jog_1 = False
                jog_2 = True
                Print_Tabuleiro()
                return False

    if jog_2:
        # Contagem de quantas peças escuras foram capturadas
        pecas_capturadas = 0
        for cont in range(5):
            if pecas_capturadas_escuras[cont] == PC_ESCURA:
                pecas_capturadas += 1

        # Teste das condições 
        if pecas_capturadas == 0:
            return False
        else:
            casas_bahia = []
            d1_valido = False
            d2_valido = False
            for cont in range(6):
                if pecas_posi[23-cont][0] == PC_NULA:
                    casas_bahia.append(True)
                    if d1 == (cont+1):
                        d1_valido = True
                    if d2 == (cont+1):
                        d2_valido = True
                else:
                    casas_bahia.append(False)
            
            if d1_valido and d2_valido:
                print("\n\u001b[4mOs valores de Dado 1 e Dado 2 permitem retornar a peça capturada ao tabuleiro\u001b[0m")
                while True:
                    try:
                        dado_x = int(input("Escolha qual Dado você deseja (1 ou 2): "))
                        if dado_x < 1 or dado_x > 2:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("\u001b[41mValor inválido.\u001b[0m Repita a operação.")
                if dado_x == 1:
                    pecas_posi[24-d1][0], pecas_capturadas_escuras[pecas_capturadas-1] = pecas_capturadas_escuras[pecas_capturadas-1], pecas_posi[24-d1][0]
                else:
                    pecas_posi[24-d2][0], pecas_capturadas_escuras[pecas_capturadas-1] = pecas_capturadas_escuras[pecas_capturadas-1], pecas_posi[24-d2][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False #chamar movimento
                else:
                    Peca_Capturada(d1, d2)
            elif d1_valido:
                print("\n\u001b[4mO valor do Dado 1 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                pecas_posi[24-d1][0], pecas_capturadas_escuras[pecas_capturadas-1] = pecas_capturadas_escuras[pecas_capturadas-1], pecas_posi[24-d1][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False
                else:
                    Peca_Capturada(d1, d2)
            elif d2_valido:
                print("\n\u001b[4mO valor do Dado 2 permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Pressione enter para realizar a jogada: ")
                input()
                pecas_posi[24-d2][0], pecas_capturadas_escuras[pecas_capturadas-1] = pecas_capturadas_escuras[pecas_capturadas-1], pecas_posi[24-d2][0]
                pecas_capturadas -= 1
                Print_Tabuleiro()
                if pecas_capturadas == 0:
                    return False
                else:
                    Peca_Capturada(d1, d2)
            else:
                print("\n\u001b[4mNenhum dos dois valores permite retornar a peça capturada ao tabuleiro\u001b[0m\n" +
                      "Passe a jogada =( \n")
                jog_1 = True
                jog_2 = False
                Print_Tabuleiro()
                return False
            

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
    dado_1 = Dado()
    
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    dado_2 = Dado()
    
    if dado_1 == dado_2:
        print("Empate nos dados. Repita o lançamento\n")
    else:
        break

if dado_1 > dado_2:
    print("A primeira pessoa que jogou o dado irá iniciar o jogo com as peças brancas")
else:
    print("A segunda pessoa que jogou o dado irá iniciar o jogo com as peças brancas")

while True:
    Jogador_1 = input("\nJogador 1, entre com seu nome: ")
    if Jogador_1.strip():
        break
    else:
        print("Nome não digitado")

while True:
    Jogador_2 = input("\nJogador 2, entre com seu nome: ")
    if Jogador_2.strip():
        break
    else:
        print("Nome não digitado")

print("\n\u001b[4mQue vença o melhor entre", Jogador_1, "e", Jogador_2, "\u001b[0m\n")
Print_Tabuleiro()

while True:
    while jog_1:
        dado_1, dado_2 = Rola_Dado()
        print("\nResultado dos dados: D1 =", dado_1, "D2 =", dado_2)
        Peca_Capturada(dado_1, dado_2)
        Opcoes(dado_1, dado_2)

        while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif pecas_posi[24-casa][0] == PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif pecas_posi[24-casa][0] == PC_ESCURA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                print("Funfou")
                jog_1 = False
                jog_2 = True
                Print_Tabuleiro()
                break
   
    while jog_2:
        dado_1, dado_2 = Rola_Dado()
        print("\nResultado dos dados: D1 =", dado_1, "D2 =", dado_2)
        Peca_Capturada(dado_1, dado_2)
        Opcoes(dado_1, dado_2)

        while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif pecas_posi[24-casa][0] == PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif pecas_posi[24-casa][0] == PC_CLARA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                print("Funfou")
                jog_1 = True
                jog_2 = False
                Print_Tabuleiro()
                break

        
