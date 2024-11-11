"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar, ler, alternar, apagar = listas[i] (CRUD)
"""
#         0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(70) #append = adiciona um valor
lista.pop() #pop = remove o ultimo valor
lista.append(80)
print(lista)
lista.insert(0, 5)
"""o insert primeiro seleciona o indice, no caso o 0; 
depois oq quer colocar no lugar, no caso o 5"""

#lista.clear() #limpa a lista
print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) 
print(lista_a)
"""a função extend extende a lista, no caso pedi para incrementar a b"""
  