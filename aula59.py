# Desempacotamento em camadas
# de métodos e funçoes
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #0         1
    ['Maria', 'Helena', ], # 0
    #0
    ['Elaine', ], # 1
    # 0          1      2
    ['Luiz', 'Joao', 'Eduarda', ], # 2
]

# p, b, c, *_, ap, u = lista
# print(p, u)

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
