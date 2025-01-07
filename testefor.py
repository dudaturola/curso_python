familia = [
    {
        'Integrante' : 'Duncan',
        'Tipo' : 'Gato',
        'Idade' : 3,
    },

    {
        'Integrante' : 'Duda',
        'Tipo' : 'Pessoa',
        'Idade' : 21,
    },
    {
        'Integrante' : 'Isa',
        'Tipo' : 'Pessoa',
        'Idade' : 22,
    },
    {
        'Integrante' : 'Jujuba',
        'Tipo' : 'Gato',
        'Idade' : 3,
    },
    ]

qtd_acertos = 0
print('Jogo de advinhar informações sobre nossa familia :)')
for i,pessoa in enumerate(familia):
    opcoes = pessoa['Integrante']
    print(f'{i})',opcoes)

    acertou = False
    resposta_int = None
    qtd_opcoes = len(familia)

resposta = input('Escolha um integrante da familia: ')

if resposta.isdigit():
    resposta_int = int(resposta)
if resposta_int is not None:
    if resposta_int >= 0 and resposta_int <qtd_opcoes:
            if familia[resposta_int] == pessoa['Integrante']:
                acertou = True


    






