"""
Crie uma função que encontra o primeiro duplicado considerando o segundo
numero como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do numero duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o númeri duplicado em si.
    Exemplo:
        [1,2,3,3,2,1] -> 1,2 e 3 são duplicados(retorne 3)
        [1,2,3,4,5,6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados na lista, retorne -1
"""

def encontrar_primeiro_duplicado(lista):
    print(lista)
    numeros_vistos = set()
    
    for numero in lista:
        if numero in numeros_vistos:
            return numero
        numeros_vistos.add(numero)

    return -1
listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8, 7],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
]
for i, lista in enumerate(listas):
    resultado = encontrar_primeiro_duplicado(lista)
    print(f'Lista {i + 1}: primeiro duplicado = {resultado}')