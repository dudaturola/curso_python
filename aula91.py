# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': ' Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

lista = {
    ('a','valor a'),
    ('b','valor a'),
    ('b','valor a'),
}

disctionary_comprehension = {
    chave: valor
    for chave, valor in lista
}# Dictionary Comprehension usa o valor e a chave, esse é o objetivo dele

set_comprehension = {2 ** i for i in range(10)} 
# set comprehension pois o set só pensa em valores
print(set_comprehension)