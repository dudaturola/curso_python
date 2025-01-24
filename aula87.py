# Empacotamento e desempacotamento de dicionarios
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# (a1, a2),(b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)
#     print()

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 21,
    'altura': 1.67,
}

pessoa_completa = {**pessoa, **dados_pessoa}


# print(pessoa, dados_pessoa)
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

# mostro_argumentos_nomeados(nome='Duda', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    
}
mostro_argumentos_nomeados(**configuracoes)