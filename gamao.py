# Funções escritas para o programa
import var_global
import tabuleiro
import retorno
import rolagem
import jogadas
import dado

# Chamada das variáreis globais com inicialização dos valores
var_global.init()

# Desenvolvimento do jogo    
print("\u001b[1m\u001b[46;1m Bem vindo ao jogo do gamão \u001b[0m\n")

# Seleção do primeiro jogador, o qual terá as peças claras (brancas)
print("\u001b[4mEscolha um entre os dois jogadores para lançar primeiro o dado.\n" + \
                "Aquele que obtiver o maior número será o primeiro jogador\u001b[0m\n")
while True:
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    var_global.dado_1 = dado.print_dado()
    
    print("Pressione enter para a rolagem do dado:", end = '')
    input()
    var_global.dado_2 = dado.print_dado()
    
    if var_global.dado_1 == var_global.dado_2:
        print("\u001b[4mEmpate nos dados. Repita o lançamento\u001b[0m\n")
    else:
        break

# Obtenção do nome do primeiro jogador
print("\u001b[4mA pessoa que jogou o dado e que teve o maior valor será o\n"
             + "primeiro jogador e jogará com as peças brancas\u001b[0m")
while True:
    var_global.jogador_1 = input("\nJogador 1, entre com seu nome: ")
    if var_global.jogador_1.strip():
        break
    else:
        print("Nome não digitado")

# Obtenção do nome do segundo jogador
print("\n\u001b[4mA pessoa que jogou o dado e que teve o menor valor será o\n"
             + "segundo jogador e jogará com as peças pretas\u001b[0m")
while True:
    var_global.jogador_2 = input("\nJogador 2, entre com seu nome: ")
    if var_global.jogador_2.strip():
        break
    else:
        print("Nome não digitado")

print("\n\u001b[4mQue vença o melhor entre " + var_global.jogador_1 + " e " + var_global.jogador_2 + "\u001b[0m\n")

tabuleiro.print_tabuleiro()

# Laço para a realização do jogo, alternando sempre entre Jogador 1 e Jogador 2
while True:
    # Jogador 1
    while var_global.jog_1:
        rolagem.rola_dado(var_global.jogador_1)
        var_global.dado_usado = 0
        var_global.cont_jogadas = 0
        if retorno.peca_capturada(var_global.dado_1, var_global.dado_2):
            jogadas.jogada_opcoes(var_global.dado_1, var_global.dado_2)
        var_global.jog_1 = False
        var_global.jog_2 = True
    #Jogador 2
    while var_global.jog_2:
        rolagem.rola_dado(var_global.jogador_2)
        var_global.dado_usado = 0
        var_global.cont_jogadas = 0
        if retorno.peca_capturada(var_global.dado_1, var_global.dado_2):
            jogadas.jogada_opcoes(var_global.dado_1, var_global.dado_2)
        var_global.jog_1 = True
        var_global.jog_2 = False