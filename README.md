# Pux_Py
Inicie jogo com `python gamao.py`

# TODO list
- Eliminar necessidade de variáveis globais
    - Via Programação Orientada a Objeto ou Programação Funcional, por ex
- Ter testes automatizados para confirmar se as regras estão sendo seguidas

## Premissas
- Garantir testabilidade
- Não ter efeito colateral/estado global
    - Torna clara relação entrada -> saída
    - Facilita testabilidade

# Bugs
- Função 'peca_capturada' em 'retorno.py'
    - Não funciona para condição casa_cond == 1, l 113-114