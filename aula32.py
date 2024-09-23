""" 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 
letras ou menos escreva "Seu nome é curto"; se tiver 5 e 6, escreva
"Seu nome é normal"; maior que 6 escreva " seu nome é muito grande"
"""
numero = input('Digite um número: ')

try:
    numero = int(numero) # Se conseguir, é um número inteiro

    if numero % 2 == 0:
        print('O número que digitou é par!')
    else:
        print('O número que digitou é ímpar!')

except ValueError: # Caso a conversão falhe, significa que a entrada não é um número inteiro
    print('O número digitado não é inteiro.')



hora = input('Digite a hora: ')

try:
    hora = int(hora)
    
    if 0 <= hora <=11:
        print('Bom dia!')
    elif 12<= hora <=17:
        print('Boa tarde!')
    else:
        print('Boa noite!')

except ValueError:
    print('Digite um número inteiro')



nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) == 5 or 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
