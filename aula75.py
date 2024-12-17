# Exercicios 
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebio como parâmetro.

def duplicar(numero):
    return f'o {numero} duplicado é {numero * 2}'

def triplicar(numero):
    return f'o {numero} triplicado é {numero * 3}'

def quadruplicar(numero):
    return f'o {numero} quadruplicado é {numero * 4}'

duplica = duplicar(3)
print(duplica)

duplica = duplicar(9)
print(duplica)

duplica = duplicar(6)
print(duplica)

triplica = triplicar(5)
print(triplica)

quadruplica = quadruplicar(6)
print(quadruplica)