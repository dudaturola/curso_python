"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|' ,'x + y + z= ', x + y + z)

soma(1, 2, 3) #argumento posicional
soma(x=2, y=3 ,z=5) # argumento nomeado
soma(3, y=6, z=5) #comeca posicional e termina nomeado

print(1,2,3, sep='-')