"""
Iterando string com while
"""
#       012345678910
nome = 'Duda Campos' #Iteráveis
#     1110987654321

tamanho_nome = len(nome)


indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    indice += 1
    novo_nome += letra

print(novo_nome)