"""
Faça uma lista de comprar com listas
o usuário deve ter a possibilidade de inserir, 
apagar e listar
valores da sua lista
não permita que o programa quebre com erros 
de índices inexistentes na lista.
"""

compras = ['arroz', 'feijão', 'leite', 'mussarela', 'ovo']


while True:

    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'a': 
        indice = input('Escolha o ínice para apagar: ')
        if indice in compras:
            apagar = compras.remove(indice)
            continue

    if opcao == 'i':
        valor_adicionado = input('Digite o valor: ')
        compras.append(valor_adicionado)
        continue

    if opcao == 'l':
        for indices, itens in enumerate(compras, start=1):
            print(indices, itens)
            continue