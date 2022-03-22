# Função das variáveis globais
from re import T
import Var

# Função
def Casa_Selecao():
    """Função que verifica se o valor escolhido para a casa da peça a ser movimentada está correto"""
    while True:
            casa = int(input("Selecione a casa correspondente a peça que você deseja mover: "))
            
            if casa == 0 or casa > 24:
                print("\u001b[41mValor inválido:\u001b[0m Fora da faixa de 1 até 24. Repita a operação.\n")
            elif Var.pecas_posi[24-casa][0] == Var.PC_NULA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou uma casa vazia. Tente novamente\n")
            elif Var.jog_1 and Var.pecas_posi[24-casa][0] == Var.PC_ESCURA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            elif Var.jog_2 and Var.pecas_posi[24-casa][0] == Var.PC_CLARA:
                print("\u001b[41mJogada inválida:\u001b[0m Você selecionou a casa do adversário. Tente novamente\n")
            else:
                print("RITMO, É RITMO DE FESTA\n")
                return casa

# Função
def Jogada_Valida(v1, v2, v3):
    """Função que verifica se a peça pode ser deslocada conforme o valor do dado ou não.
       Se for válida, a peça será deslocada"""
    return print("MAR OI, LOMBARDI!!!\n")

# Função
def Jogada_Opcoes(d1, d2):
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
    
    # Possibilidades em caso de dois dados diferentes
    else:
        while True:
            # Opções para quando não há peça capturada e irá usar os dois dados
            if Var.dado_usado == 0:
                # Tratamento de exceção quando usuário entra com opção inválida
                try:
                    print("\n\u001b[4mSelecione uma das opções de jogadas disponíveis abaixo:\u001b[0m\n")
                    print("1 - Mover uma peça: usando D1 primeiro e depois D2")
                    print("2 - Mover uma peça: usando D2 primeiro e depois D1")
                    print("3 - Mover duas peças: a primeira com D1 e a segunda com D2")
                    print("4 - Mover duas peças: a primeira com D2 e a segunda com D1\n")
                    opcao = int(input("Opção: "))
                    # Valor de opção fora da faixa válida -> Chamada da exceção
                    if opcao < 1 or opcao > 4:
                        raise ValueError
                    else:
                        # Movimento de uma peça usando D1 primeiro e depois D2
                        if opcao == 1:
                            casa = Casa_Selecao()
                            Jogada_Valida(casa, d1, d2)
                            return
                        # Movimento de uma peça usando D2 primeiro e depois D1
                        elif opcao == 2:
                            casa = Casa_Selecao()
                            Jogada_Valida(casa, d2, d1)
                            return
                        # Movimento de duas peças usando D1 para a primeira e D2 para a segunda
                        elif opcao == 3:
                            # Peça 1
                            casa_1 = Casa_Selecao()
                            Jogada_Valida(casa_1, d1, 0)
                            while True:
                                try:
                                    # Peça 2
                                    casa_2 = Casa_Selecao()
                                    # Testa se a peça é a mesma. Se for, chama exceção
                                    if (casa_2 + d1) == casa_1:
                                        raise ValueError
                                    else:
                                        Jogada_Valida(casa_1, d2, 0)
                                        return
                                except ValueError:
                                    print("\nA peça selecionada foi a mesma. Você deve selecionar outra peça.\n")
                        else:
                            # Peça 1
                            casa_1 = Casa_Selecao()
                            Jogada_Valida(casa_1, d2, 0)
                            while True:
                                try:
                                    # Peça 2
                                    casa_2 = Casa_Selecao()
                                    # Testa se a peça é a mesma. Se for, chama exceção
                                    if (casa_2 + d2) == casa_1:
                                        raise ValueError
                                    else:
                                        Jogada_Valida(casa_1, d1, 0)
                                        return
                                except ValueError:
                                    print("\nA peça selecionada foi a mesma. Você deve selecionar outra peça.\n")
                # Exceção
                except ValueError:
                    print("\u001b[41mOpção inválida.\u001b[0m Repita a operação.")
            
            # Opção para quando há somente uma peça capturada e irá usar D1 para movimentar
            elif Var.dado_usado == 2:
                print("\n\u001b[4mSó resta D1 para jogar. Aperte enter para continuar.\u001b[0m\n")
                input()
                # Peça 1
                casa = Casa_Selecao()
                Jogada_Valida(casa, d1, 0)
                return
            
            # Opção para quando há somente uma peça capturada e irá usar D2 para movimentar
            elif Var.dado_usado == 1:
                print("\n\u001b[4mSó resta D2 para jogar. Aperte enter para continuar.\u001b[0m\n")
                input()
                # Peça 1
                casa = Casa_Selecao()
                Jogada_Valida(casa, d2, 0)
                return