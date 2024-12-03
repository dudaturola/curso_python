"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
Replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retomar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
# def Print(a, b , c):
#     print('Várias')

# def imprimir(a, b, c):
#     print(a,b,c)

# imprimir(1,2,3)


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao()
