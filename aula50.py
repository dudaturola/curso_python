"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))