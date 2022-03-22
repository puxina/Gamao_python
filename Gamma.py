# Funções escritas para o programa
import Var
import Tabuleiro
import Retorno
import Rolagem
import Jogadas
import Dado

# Chamada das variáreis globais com inicialização dos valores
Var.init()

# Desenvolvimento do jogo    
print("\u001b[1m\u001b[46;1m Bem vindo ao jogo do gamão \u001b[0m\n")

# Seleção do primeiro jogador, o qual terá as peças claras (brancas)
print("\u001b[4mEscolha um entre os dois jogadores para lançar primeiro o dado.\n" + \
                "Aquele que obtiver o maior número será o primeiro jogador e terá as peças brancas\u001b[0m\n")
while True:
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Var.dado_1 = Dado.Print_Dado()
    
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    Var.dado_2 = Dado.Print_Dado()
    
    if Var.dado_1 == Var.dado_2:
        print("\u001b[4mEmpate nos dados. Repita o lançamento\u001b[0m\n")
    else:
        break
if Var.dado_1 > Var.dado_2:
    print("\u001b[4mA primeira pessoa que jogou o dado irá iniciar o jogo com as peças brancas\u001b[0m")
else:
    print("\u001b[4mA segunda pessoa que jogou o dado irá iniciar o jogo com as peças brancas\u001b[0m")

# Obtenção dos nomes dos jogadores
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
        Rolagem.Rola_Dado(Var.jogador_1)
        Var.dado_usado = 0
        Var.cont_jogadas = 0
        if Retorno.Peca_Capturada(Var.dado_1, Var.dado_2):
            Jogadas.Jogada_Opcoes(Var.dado_1, Var.dado_2)
        Var.jog_1 = False
        Var.jog_2 = True
    #Jogador 2
    while Var.jog_2:
        Rolagem.Rola_Dado(Var.jogador_2)
        Var.dado_usado = 0
        Var.cont_jogadas = 0
        if Retorno.Peca_Capturada(Var.dado_1, Var.dado_2):
            Jogadas.Jogada_Opcoes(Var.dado_1, Var.dado_2)
        Var.jog_1 = True
        Var.jog_2 = False