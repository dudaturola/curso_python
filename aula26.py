"""
Formatação básica de string
s - string
d - int
f - float
.<número de dígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o numero a aparecer antes do zero
Sinal - + ou -
Ex.: 0>-100,,1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.48151312:+,.1f}')
print(f'O hexadecial de 1500 é {1500:08X}')