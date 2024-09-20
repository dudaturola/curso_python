"""
Introdução ao try/except
try-> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""
numero_srt = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    print('STR:', numero_srt)
    numero_float = float(numero_srt)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_srt} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')

# if numero_srt.isdigit():
#     numero_float = float(numero_srt)
#     print(f'O dobro de {numero_srt} é {numero_float*2:.2f}')
# else:
#     print('Isso não pe um número!')
