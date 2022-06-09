"""
Programa principal para a chamada dos módulos, construção
do tabuleiro, movimentação das peças e suas retiradas do
jogo gamão
"""

from def_cores import *

def main():
    # Funções escritas para o programa
    import var_global
    import tabuleiro
    import retorno
    import dado_lancamento
    import jogadas

    # Desenvolvimento do jogo    
    print(COR_NEGRITO + COR_FUNDO_CIANO + " Bem vindo ao jogo do gamão "+ COR_RESETALL +"\n")

    # Seleção do primeiro jogador, o qual terá as peças claras (brancas)
    print(COR_SUBLINHADO + "Escolha um entre os dois jogadores para lançar primeiro o dado.\n" + \
                    "Aquele que obtiver o maior número será o primeiro jogador"+ COR_RESETALL +"\n")
    while True:
        print("Pressione enter para a rolagem do dado:", end = '')
        input()
        var_global.dado_1 = dado_lancamento.print_dado()
        
        print("Pressione enter para a rolagem do dado:", end = '')
        input()
        var_global.dado_2 = dado_lancamento.print_dado()
        
        if var_global.dado_1 == var_global.dado_2:
            print(COR_SUBLINHADO + "Empate nos dados. Repita o lançamento"+ COR_RESETALL +"\n")
        else:
            break

    # Obtenção do nome do primeiro jogador
    print(COR_SUBLINHADO + "A pessoa que jogou o dado e que teve o maior valor será o\n"
                + "primeiro jogador e jogará com as peças brancas"+ COR_RESETALL)
    while True:
        var_global.jogador_1 = input("\nJogador 1, entre com seu nome: ")
        if var_global.jogador_1.strip():
            break
        else:
            print("Nome não digitado")

    # Obtenção do nome do segundo jogador
    print("\n" + COR_SUBLINHADO + "A pessoa que jogou o dado e que teve o menor valor será o\n"
                + "segundo jogador e jogará com as peças pretas"+ COR_RESETALL)
    while True:
        var_global.jogador_2 = input("\nJogador 2, entre com seu nome: ")
        if var_global.jogador_2.strip():
            break
        else:
            print("Nome não digitado")

    print("\n" + COR_SUBLINHADO + "Que vença o melhor entre " + var_global.jogador_1 + " e " + var_global.jogador_2 + COR_RESETALL +"\n")

    tabuleiro.print_tabuleiro(var_global.pecas_posi, var_global.pecas_retiradas_escuras, var_global.pecas_retiradas_claras, var_global.pecas_capturadas_escuras, var_global.pecas_capturadas_claras, var_global.CS_CLARA, var_global.CS_ESCURA, var_global.CS_MEIO)


    # Laço para a realização do jogo, alternando sempre entre Jogador 1 e Jogador 2
    while True:
        # Jogador 1
        while var_global.jog_1:
            dado_lancamento.rola_dado(var_global.jogador_1)
            var_global.dado_usado = 0
            var_global.cont_jogadas = 0
            if retorno.peca_capturada(var_global.dado_1, var_global.dado_2):
                jogadas.jogada_opcoes(var_global.dado_1, var_global.dado_2)
            if var_global.pecas_retiradas_claras_quant == 15:
                break
            else:
                var_global.jog_1 = False
                var_global.jog_2 = True
        #Jogador 2
        while var_global.jog_2:
            dado_lancamento.rola_dado(var_global.jogador_2)
            var_global.dado_usado = 0
            var_global.cont_jogadas = 0
            if retorno.peca_capturada(var_global.dado_1, var_global.dado_2):
                jogadas.jogada_opcoes(var_global.dado_1, var_global.dado_2)
            if var_global.pecas_retiradas_escuras_quant == 15:
                break
            else:
                var_global.jog_1 = True
                var_global.jog_2 = False

        if var_global.pecas_retiradas_claras_quant == 15 or var_global.pecas_retiradas_escuras_quant == 15:
            break

    print("\n   \\o/ Fim de jogo \\o/")
    if var_global.jog_1:
        print("Parabéns, " + var_global.jogador_1 + "!!!")
    else:
        print("Parabéns, " + var_global.jogador_2 + "!!!")
    print("   ☜(⌒▽⌒)☞")
    
    return

main()