"""
Enumerate - enumera iteráveis (índices)
"""
# [(1, 'Maria'), (2, 'Isa'), (3, 'Duncam'), (4, 'Jujuba'), (5, 'Cajuzinha')]
lista = ['Maria','Isa', 'Duncam', 'Jujuba']
lista.append('Cajuzinha')

# lista_enumerada = list(enumerate(lista, start=1))

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])               #jeito mais facil

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for item in enumerate(lista):
#     print('for da tupla')
#     for valor in item:
#         print(valor)
