# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# dever ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Duda', 'sobrenome':'Campos'},
    {'nome': 'Isa', 'sobrenome':'Pimenta'},
    {'nome': 'Duncan', 'sobrenome':'Cat'},
    {'nome': 'Jujuba', 'sobrenome':'Cat'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])


exibir(l1)
exibir(l2)