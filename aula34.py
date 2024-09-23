"""
Repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou!')