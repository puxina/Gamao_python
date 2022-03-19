# Funções escritas para o programa
import Var
import Tabuleiro
import Captura
import Rolagem
import Jogadas
import Dado

Var.init()

# Desenvolvimento do jogo    
print("\u001b[1m\u001b[46;1m Bem vindo ao jogo do gamão \u001b[0m\n")

# Seleção do primeiro jogador, o qual terá as peças claras (amarelas)
print("Escolha um entre os dois jogadores para lançar primeiro o dado.\nAquele que obtiver o maior número será o primeiro jogador\n")
while True:
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Var.dado_1 = Dado.Print_Dado()
    
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Var.dado_2 = Dado.Print_Dado()
    
    if Var.dado_1 == Var.dado_2:
        print("Empate nos dados. Repita o lançamento\n")
    else:
        break

if Var.dado_1 > Var.dado_2:
    print("A primeira pessoa que jogou o dado irá iniciar o jogo com as peças brancas")
else:
    print("A segunda pessoa que jogou o dado irá iniciar o jogo com as peças brancas")

while True:
    Var.jogador_1 = input("\nJogador 1, entre com seu nome: ")
    if Var.jogador_1.strip():
        break
    else:
        print("Nome não digitado")

while True:
    Var.jogador_2 = input("\nJogador 2, entre com seu nome: ")
    if Var.jogador_2.strip():
        break
    else:
        print("Nome não digitado")

print("\n\u001b[4mQue vença o melhor entre", Var.jogador_1, "e", Var.jogador_2, "\u001b[0m\n")
Tabuleiro.Print_Tabuleiro()

# Laço para a realização do jogo, alternando sempre entre Jogador 1 e Jogador 2
while True:
    # Jogador 1
    while Var.jog_1:
        Var.dado_1, Var.dado_2 = Rolagem.Rola_Dado(Var.jogador_1)
        print("\nResultado dos dados: D1 =", Var.dado_1, "D2 =", Var.dado_2)
        if Captura.Peca_Capturada(Var.dado_1, Var.dado_2):
            Jogadas.Opcoes(Var.dado_1, Var.dado_2)
        else:
            Var.jog_1 = False
            Var.jog_2 = True
            break
        
        while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif Var.pecas_posi[24-casa][0] == Var.PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif Var.pecas_posi[24-casa][0] == Var.PC_ESCURA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                print("RITMO, É RITMO DE FESTA\n")
                Var.jog_1 = False
                Var.jog_2 = True
                Tabuleiro.Print_Tabuleiro()
                break
    #Jogador 2
    while Var.jog_2:
        Var.dado_1, Var.dado_2 = Rolagem.Rola_Dado(Var.jogador_2)
        print("\nResultado dos dados: D1 =", Var.dado_1, "D2 =", Var.dado_2)
        if Captura.Peca_Capturada(Var.dado_1, Var.dado_2):
            Jogadas.Opcoes(Var.dado_1, Var.dado_2)
        else:
            Var.jog_1 = True
            Var.jog_2 = False
            break

        while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif Var.pecas_posi[24-casa][0] == Var.PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif Var.pecas_posi[24-casa][0] == Var.PC_CLARA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                print("MAR OI LOMBARDI\n")
                Var.jog_1 = True
                Var.jog_2 = False
                Tabuleiro.Print_Tabuleiro()
                break

        
