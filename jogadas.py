"""
Módulo que trata de tudo relacionado as jogadas de movimento das peças
e suas retiradas

Funções:
    * casa_selecao():

    * retirada_cond():

    * jogada_validade(casa, dado):

    * peca_movimento(casa, movimento, d1, d2):

    * jogada_dados_diff(opcao, d1, d2):

    * jogada_dados_igual(opcao, d1, d2):

    * jogada_opcoes(d1, d2):
"""

# Função das variáveis globais
from re import T
import var_global
import tabuleiro

###############################################
def casa_selecao():
    """Função que verifica se o valor escolhido para a casa da peça a ser movimentada está correto"""
    while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\n\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif var_global.pecas_posi[24-casa][0] == var_global.pc_nula:
                print("\n\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif var_global.jog_1 and var_global.pecas_posi[24-casa][0] == var_global.pc_escura:
                print("\n\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            elif var_global.jog_2 and var_global.pecas_posi[24-casa][0] == var_global.pc_clara:
                print("\n\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                return casa

###############################################
def casa_cont(casa):
    """Função da contagem de peças na casa"""

    quant = 0
    casa_posi = 24-casa

    for cont in range(5):
        if var_global.jog_1 and var_global.pecas_posi[casa_posi][cont] == var_global.pc_clara:
            quant += 1
        elif var_global.jog_2 and var_global.pecas_posi[casa_posi][cont] == var_global.pc_escura:
            quant += 1
        elif var_global.pecas_posi[casa_posi][cont] == var_global.pc_nula:
            break
        elif var_global.pecas_posi[casa_posi][cont].isnumeric():
            quant += var_global.pecas_posi[casa_posi][cont]

    return quant

###############################################
def retirada_cond():
    """Teste da condição para retiradas de peças do jogo"""

    if var_global.jog_1:
        for casa in range(6):
            for linha in range(5):
                if var_global.pecas_posi[casa][linha] == var_global.pc_clara:
                    var_global.pecas_casa_campo_clara += 1
                elif var_global.pecas_posi[casa][linha].isnumeric():
                    var_global.pecas_casa_campo_clara += var_global.pecas_posi[casa][linha]
    else:
        for casa in range(6):
            for linha in range(5):
                if var_global.pecas_posi[23-casa][linha] == var_global.pc_escura:
                    var_global.pecas_casa_campo_escura += 1
                elif var_global.pecas_posi[23-casa][linha].isnumeric():
                    var_global.pecas_casa_campo_escura += var_global.pecas_posi[23-casa][linha]
    return

###############################################
def jogada_validade(casa, dado):
    """Função para verificar se a movimentação da peça do jogador é válida \n
       Duas ou mais peças do adversário: casa fechada\n
       Uma peça do adversário: peça será capturada\n
       Casa sem peças ou com peças do próprio jogador: casa livre"""

    movimento_clara = 24-casa+dado
    movimento_escura = 24-casa-dado

    # Movimento de retirada se casa campo com todas as peças
    if var_global.jog_1 and movimento_clara > 23:
        if var_global.pecas_casa_campo_clara == 15 and var_global.pecas_capturadas_claras[0] == var_global.pc_nula:
            return 5
        else:
            print("\nCondição para as retiradas de peças do jogo não atingida. Tente novamente\n")
            return 2
    elif var_global.jog_2 and movimento_escura < 0:
        if var_global.pecas_casa_campo_escura == 15 and var_global.pecas_capturadas_escuras[0] == var_global.pc_nula:
            return 5
        else:
            print("\nCondição para as retiradas de peças do jogo não atingida. Tente novamente\n")
            return 2
    
    # Movimento válido se casa vazia
    elif var_global.jog_1 and var_global.pecas_posi[movimento_clara][0] == var_global.pc_nula:
        return 1
    elif var_global.jog_2 and var_global.pecas_posi[movimento_escura][0] == var_global.pc_nula:
        return 1
    
    # Movimento inválido se casa bloqueada
    elif var_global.jog_1 and var_global.pecas_posi[movimento_clara][1] == var_global.pc_escura:
        print("\n\u001b[41mJogada inválida:\u001b[0m A opção escolhida leva sua peça\n" +
                "para uma casa bloqueada. Tente novamente\n")
        tabuleiro.print_tabuleiro()
        return 2
    elif var_global.jog_2 and var_global.pecas_posi[movimento_escura][1] == var_global.pc_clara:
        print("\n\u001b[41mJogada inválida:\u001b[0m A opção escolhida leva sua peça\n" +
                "para uma casa bloqueada. Tente novamente\n")
        tabuleiro.print_tabuleiro()
        return 2
    
    # Movimento de captura
    elif var_global.jog_1 and var_global.pecas_posi[movimento_clara][1] == var_global.pc_nula \
         and var_global.pecas_posi[movimento_clara][0] == var_global.pc_escura:
        print("\nA opção escolhida leva sua peça a capturar a peça do adversário\n")
        return 3
    elif var_global.jog_2 and var_global.pecas_posi[movimento_escura][1] == var_global.pc_nula \
         and var_global.pecas_posi[movimento_escura][0] == var_global.pc_clara:
        print("\nA opção escolhida leva sua peça a capturar a peça do adversário\n")
        return 3
    
    # Movimento válido de sobreposição se peças do jogador
    elif var_global.jog_1 and var_global.pecas_posi[movimento_clara][0] == var_global.pc_clara:
        return 4
    elif var_global.jog_2 and var_global.pecas_posi[movimento_escura][0] == var_global.pc_escura:
        return 4

###############################################
def peca_movimento(casa, movimento, dado):
    """Função que irá movimentar a peça conforme a situação"""

    posi_casa = 24-casa
    movimento_clara = 24-casa+dado
    movimento_escura = 24-casa-dado
    quant_ori = casa_cont(casa)

    # Movimento para casa vazia
    if movimento == 1:
        # Jogador 1 e peças na casa de 5 a menos
        if var_global.jog_1 and quant_ori <= 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_clara][0] = var_global.pecas_posi[movimento_clara][0], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 1 e peças na casa mais de 5
        elif var_global.jog_1 and quant_ori > 5:
            var_global.pecas_posi[posi_casa][4] -= 1
            if var_global.pecas_posi[posi_casa][4] == 1:
                var_global.pecas_posi[posi_casa][4], var_global.pecas_extras[posi_casa][0] = var_global.pecas_extras[posi_casa][0], var_global.pecas_posi[posi_casa][4]
                var_global.pecas_posi[posi_casa][4], var_global.pecas_posi[movimento_clara][0] = var_global.pecas_posi[movimento_clara][0], var_global.pecas_posi[posi_casa][4]
            #else:
        # Jogador 2 e peças na casa de 5 a menos
        elif var_global.jog_2 and quant_ori <= 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_escura][0] = var_global.pecas_posi[movimento_escura][0], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 2 e peças na casa mais de 5
        elif var_global.jog_2 and quant_ori > 5:
            var_global.pecas_posi[posi_casa][4] -= 1
            if var_global.pecas_posi[posi_casa][4] == 1:
                var_global.pecas_posi[posi_casa][4], var_global.pecas_extras[posi_casa][0] = var_global.pecas_extras[posi_casa][0], var_global.pecas_posi[posi_casa][4]
                var_global.pecas_posi[posi_casa][4], var_global.pecas_posi[movimento_escura][0] = var_global.pecas_posi[movimento_escura][0], var_global.pecas_posi[posi_casa][4]
            #else:
    
    # Movimento para captura da peça adversária
    elif movimento == 3:
        pecas_capturadas = [0, 0]
        for cont in range(5):
            if var_global.pecas_capturadas_claras[cont] == var_global.pc_clara:
                pecas_capturadas[0] += 1
            if var_global.pecas_capturadas_escuras[cont] == var_global.pc_escura:
                pecas_capturadas[1] += 1

        # Jogador 1 e peças na casa de 5 a menos
        if var_global.jog_1 and quant_ori <= 5:
            var_global.pecas_posi[movimento_clara][0], var_global.pecas_capturadas_escuras[pecas_capturadas[1]] = var_global.pecas_capturadas_escuras[pecas_capturadas[1]], var_global.pecas_posi[movimento_clara][0]
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_clara][0] = var_global.pecas_posi[movimento_clara][0], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 1 e peças na casa mais de 5
        elif var_global.jog_1 and quant_ori > 5:
            var_global.pecas_posi[posi_casa][4] -= 1
            if var_global.pecas_posi[posi_casa][4] == 1:
                var_global.pecas_posi[posi_casa][4], var_global.pecas_extras[posi_casa][0] = var_global.pecas_extras[posi_casa][0], var_global.pecas_posi[posi_casa][4]
                var_global.pecas_posi[movimento_clara][0], var_global.pecas_capturadas_escuras[pecas_capturadas[1]] = var_global.pecas_capturadas_escuras[pecas_capturadas[1]], var_global.pecas_posi[movimento_clara][0]
                var_global.pecas_posi[posi_casa][4], var_global.pecas_posi[movimento_clara][0] = var_global.pecas_posi[movimento_clara][0], var_global.pecas_posi[posi_casa][4]
        # Jogador 2 e peças na casa de 5 a menos
        elif var_global.jog_2 and quant_ori <= 5:
            var_global.pecas_posi[movimento_escura][0], var_global.pecas_capturadas_claras[pecas_capturadas[0]] = var_global.pecas_capturadas_claras[pecas_capturadas[0]], var_global.pecas_posi[movimento_escura][0]
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_escura][0] = var_global.pecas_posi[movimento_escura][0], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 2 e peças na casa mais de 5
        elif var_global.jog_2 and quant_ori > 5:
            var_global.pecas_posi[posi_casa][4] -= 1
            if var_global.pecas_posi[posi_casa][4] == 1:
                var_global.pecas_posi[posi_casa][4], var_global.pecas_extras[posi_casa][0] = var_global.pecas_extras[posi_casa][0], var_global.pecas_posi[posi_casa][4]
                var_global.pecas_posi[movimento_escura][0], var_global.pecas_capturadas_claras[pecas_capturadas[0]] = var_global.pecas_capturadas_claras[pecas_capturadas[0]], var_global.pecas_posi[movimento_escura][0]
                var_global.pecas_posi[posi_casa][4], var_global.pecas_posi[movimento_escura][0] = var_global.pecas_posi[movimento_escura][0], var_global.pecas_posi[posi_casa][4]
    
    # Movimento para sobrepor a peça do jogador
    elif movimento == 4:
        if var_global.jog_1:
            quant_des = casa_cont(casa-dado)
        else:
            quant_des = casa_cont(casa+dado)
        # Jogador 1 e peças na casa de origem e destino menos de 5
        if var_global.jog_1 and quant_ori < 5 and quant_des < 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_clara][quant_des] = var_global.pecas_posi[movimento_clara][quant_des], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 1 e peças na casa de origem menos de 5 e casa de destino com 5 ou mais peças
        elif var_global.jog_1 and quant_ori < 5 and quant_des >= 5:
            if var_global.pecas_posi[movimento_clara][4] == var_global.pc_clara:
                var_global.pecas_sobre_quant[movimento_clara] += 1
        # Jogador 2 e peças na casa de origem e destino menos de 5
        if var_global.jog_2 and quant_ori < 5 and quant_des < 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_posi[movimento_escura][quant_des] = var_global.pecas_posi[movimento_escura][quant_des], var_global.pecas_posi[posi_casa][quant_ori-1]
        # Jogador 2 e peças na casa de origem menos de 5 e casa de destino com 5 ou mais peças
        elif var_global.jog_2 and quant_ori < 5 and quant_des >= 5:
            if var_global.pecas_posi[movimento_escura][4] == var_global.pc_escura:
                var_global.pecas_sobre_quant[movimento_escura] += 1

    # Movimento para retirar a peça do jogador
    elif movimento == 5:
        quant_ret = 0
        if var_global.jog_1:
            for cont in range(15):
                if var_global.pecas_retiradas_claras[cont] == var_global.pc_clara:
                    quant_ret += 1
        else:
            for cont in range(15):
                if var_global.pecas_retiradas_escuras[cont] == var_global.pc_escura:
                    quant_ret += 1

        # Jogador 1 e peças na casa de 5 a menos
        if var_global.jog_1 and quant_ori <= 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_retiradas_claras[quant_ret] = var_global.pecas_retiradas_claras[quant_ret], var_global.pecas_posi[posi_casa][quant_ori-1]
            var_global.pecas_retiradas_claras_quant = quant_ret
        # Jogador 1 e peças na casa de 5 a menos
        elif var_global.jog_2 and quant_ori <= 5:
            var_global.pecas_posi[posi_casa][quant_ori-1], var_global.pecas_retiradas_escuras[quant_ret] = var_global.pecas_retiradas_escuras[quant_ret], var_global.pecas_posi[posi_casa][quant_ori-1]
            var_global.pecas_retiradas_escuras_quant = quant_ret

    return

###############################################
def jogada_dados_diff(opcao, d1, d2):
    """Função que verifica se a peça pode ser deslocada conforme o valor do dado ou não.
       Se for válida, a peça será deslocada"""
    movimento = [0, 0]
    # Mover uma peça: usando D1 primeiro e depois D2
    if opcao == 1:
        # Validade das duas jogadas
        casa = casa_selecao()
        movimento[0] = jogada_validade(casa, d1)
        if movimento[0] == 2:
            return False
        else:
            if var_global.jog_1:
                movimento[1] = jogada_validade(casa-d1, d2)
            else:
                movimento[1] = jogada_validade(casa+d1, d2)
        # Se um dos dois movimentos for inválido
        if movimento[1] == 2:
            return False
        # Se não há movimentos inválidos
        else:
            peca_movimento(casa, movimento[0], d1)
            if var_global.jog_1:
                peca_movimento(casa-d1, movimento[1], d2)
            else:
                peca_movimento(casa+d1, movimento[1], d2)
            tabuleiro.print_tabuleiro()
            return True

    # Mover uma peça: usando D2 primeiro e depois D1
    elif opcao == 2:
        # Validade das duas jogadas
        casa = casa_selecao()
        movimento[0] = jogada_validade(casa, d2)
        if movimento[0] == 2:
            return False
        else:
            if var_global.jog_1:
                movimento[1] = jogada_validade(casa-d2, d1)
            else:
                movimento[1] = jogada_validade(casa+d2, d1)
        # Se um dos dois movimentos for inválido
        if movimento[1] == 2:
            return False
        # Se não há movimentos inválidos
        else:
            peca_movimento(casa, movimento[0], d2)
            if var_global.jog_1:
                peca_movimento(casa-d2, movimento[1], d1)
            else:
                peca_movimento(casa+d2, movimento[1], d1)
            tabuleiro.print_tabuleiro()
            return True

    # Mover duas peças: a primeira com D1 e a segunda com D2
    elif opcao == 3:
        # Peça 1
        casa_1 = casa_selecao()
        movimento[0] = jogada_validade(casa_1, d1)
        # Testa jogada inválida com D1 e retorna à função Opções caso verdade
        if movimento[0] == 2:
            return False
        else:
            peca_movimento(casa_1, movimento[0], d1)
            var_global.dado_usado = 1
            var_global.cont_jogadas += 1
            tabuleiro.print_tabuleiro()
        # Testa se a peça é a mesma. Se for, chama exceção
        while True:
            try:
                # Peça 2
                casa_2 = casa_selecao()
                movimento[1] = jogada_validade(casa_2, d2)
                if movimento[1] == 2:
                    return False
                elif var_global.jog_1:
                    if (casa_2 + d1) == casa_1:
                        raise ValueError
                elif var_global.jog_2:
                    if (casa_2 - d1) == casa_1:
                        raise ValueError
                peca_movimento(casa_2, movimento[1], d2)
                tabuleiro.print_tabuleiro()
                return True
            except ValueError:
                print("\nA peça selecionada foi a mesma. Você deve selecionar outra peça.\n")

    # Mover duas peças: a primeira com D2 e a segunda com D1
    elif opcao == 4:
        # Peça 1
        casa_1 = casa_selecao()
        movimento[0] = jogada_validade(casa_1, d2)
        # Testa jogada inválida com D2 e retorna à função Opções caso verdade
        if movimento[0] == 2:
            return False
        else:
            peca_movimento(casa_1, movimento[0], d2)
            var_global.dado_usado = 2
            var_global.cont_jogadas += 1
            tabuleiro.print_tabuleiro()
        # Testa se a peça é a mesma. Se for, chama exceção
        while True:
            try:
                # Peça 2
                casa_2 = casa_selecao()
                movimento[1] = jogada_validade(casa_2, d1)
                if movimento[1] == 2:
                    return False
                elif var_global.jog_1:
                    if (casa_2 + d2) == casa_1:
                        raise ValueError
                elif var_global.jog_2:
                    if (casa_2 - d2) == casa_1:
                        raise ValueError
                peca_movimento(casa_2, movimento[1], d1)
                tabuleiro.print_tabuleiro()
                return True
            except ValueError:
                print("\nA peça selecionada foi a mesma. Você deve selecionar outra peça.\n")

    # Mover uma peça: usando somente D1
    elif opcao == 5:
        # Validade da jogada única
        casa = casa_selecao()
        movimento[0] = jogada_validade(casa, d1)
        if movimento[0] == 2:
            return False
        else:
            peca_movimento(casa, movimento[0], d1)
            tabuleiro.print_tabuleiro()
            return True

    # Mover uma peça: usando somente D2
    elif opcao == 6:
        # Validade da jogada única
        casa = casa_selecao()
        movimento[0] = jogada_validade(casa, d2)
        if movimento[0] == 2:
            return False
        else:
            peca_movimento(casa, movimento[0], d2)
            tabuleiro.print_tabuleiro()
            return True

###############################################
def jogada_opcoes(d1, d2):
    """Função para indicar as várias opções disponíveis do uso dos dados ao jogador"""
    if d1 == d2 and var_global.cont_jogadas == 0:
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
    
    # Possibilidades em caso de dois dados diferentes
    else:
        while True:
            # Opções para quando não há peça capturada e irá usar os dois dados
            if var_global.dado_usado == 0:
                # Tratamento de exceção quando usuário entra com opção inválida
                try:
                    print("\u001b[4m", end = "")
                    if var_global.jog_1:
                        print(var_global.jogador_1, end = "")
                    else:
                        print(var_global.jogador_2, end = "")
                    print(", selecione uma das opções de jogadas disponíveis abaixo:\u001b[0m\n")
                    print("1 - Mover uma peça: usando D1 = " + str(d1) + " primeiro e depois D2 = " + str(d2))
                    print("2 - Mover uma peça: usando D2 = " + str(d2) + " primeiro e depois D1 = " + str(d1))
                    print("3 - Mover duas peças: a primeira com D1 = " + str(d1) + " e a segunda com D2 = " + str(d2))
                    print("4 - Mover duas peças: a primeira com D2 = " + str(d2) + " e a segunda com D1 = " + str(d1) + "\n")
                    opcao = int(input("Opção: "))
                    # Valor de opção fora da faixa válida -> Chamada da exceção
                    if opcao < 1 or opcao > 4:
                        raise ValueError
                    else:
                        # Movimento de uma peça usando D1 primeiro e depois D2
                        if opcao == 1:
                            if jogada_dados_diff(opcao, d1, d2):
                                return
                            else:
                                jogada_opcoes(d1, d2)
                                return
                        # Movimento de uma peça usando D2 primeiro e depois D1
                        elif opcao == 2:
                            if jogada_dados_diff(opcao, d1, d2):
                                return
                            else:
                                jogada_opcoes(d1, d2)
                                return
                        # Movimento de duas peças usando D1 para a primeira e D2 para a segunda
                        elif opcao == 3:
                            if jogada_dados_diff(opcao, d1, d2):
                                return
                            else:
                                jogada_opcoes(d1, d2)
                                return
                        else:
                            if jogada_dados_diff(opcao, d1, d2):
                                return
                            else:
                                jogada_opcoes(d1, d2)
                                return
                # Exceção
                except ValueError:
                    print("\n\u001b[41mOpção inválida.\u001b[0m Repita a operação.\n")
            
            # Opção para quando há somente uma peça capturada e irá usar D1 para movimentar
            elif var_global.dado_usado == 2:
                print("\u001b[4m", end = "")
                if var_global.jog_1:
                    print(var_global.jogador_1, end = "")
                else:
                    print(var_global.jogador_2, end = "")
                print(", lhe resta somente um movimento com o dado D1 = " + str(d1) + "\u001b[0m\n")
                opcao = 5
                if jogada_dados_diff(opcao, d1, d2):
                    return
                else:
                    jogada_opcoes(d1, d2)
                    return
            
            # Opção para quando há somente uma peça capturada e irá usar D2 para movimentar
            elif var_global.dado_usado == 1:
                print("\u001b[4m", end = "")
                if var_global.jog_1:
                    print(var_global.jogador_1, end = "")
                else:
                    print(var_global.jogador_2, end = "")
                print(", lhe resta somente um movimento com o dado D2 = " + str(d2) + "\u001b[0m\n")
                opcao = 6
                if jogada_dados_diff(opcao, d1, d2):
                    return
                else:
                    jogada_opcoes(d1, d2)
                    return