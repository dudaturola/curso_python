"""
Exercicios 
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou nao) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}]
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios."
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome não tem espaço.')
        
    print(f'Seu nome contém {len(nome)} caracteres.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou espaços vazios!')






    