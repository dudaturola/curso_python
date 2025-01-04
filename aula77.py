# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Maria Eduarda'
pessoa['sobrenome'] = 'Campos Turola'
lista = []

print(pessoa[chave])
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('Não existe!!')
else:
    print(pessoa['sobrenome'])