"""
Tipo tupla - Uma lista imutável
"""
# nomes = ['Maria', 'Jujuba', 'Dancam'] #  lista
nomes = ['Maria', 'Jujuba', 'Dancam'] #  tupla ( tupla nao tem chaves)
nomes[1] = 'outro'
_, _, nome, *resto = nomes
print(nomes)
print(nome)
nomes = tuple(nomes)
