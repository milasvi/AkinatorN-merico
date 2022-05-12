print('Bem-vinde ao AkinatorNúmerico!')

while True:
    num = input('Digite algo e eu direi se é número ou não.')
    r = num.isnumeric()
    if r == False:
        print('Não é número.')
    elif r == True:
        print('É número.')
    resposta = input('Deseja continuar? [S/N]')
    while resposta != 'S' and resposta != 'N':
        resposta = input('Digite apenas [S/N], ok?')
    if resposta == 'N':
        print('Finalizando...')
        break







