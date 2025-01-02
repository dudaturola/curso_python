# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# usamos as - {} - ou a classe dict para criar
# dicionários.
# Imutáveis = str, int, float, bool, tuple
# Mutável = dict, list

pessoa = {
    'nome' : 'Maria Eduarda',
    'sobrenome' : ' Campos Turola',
    'idade' : 21,
    'altura' : 1.67,
    'endereço' : [
        {'rua' : 'tal tal', 'numero':123},
        {'rua' : 'outra rua', 'numero':321}
    ]
}
print(pessoa['idade'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])