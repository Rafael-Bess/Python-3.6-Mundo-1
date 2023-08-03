nome = str(input('Qual é seu Nome?:'))
p = 'PARABÉNS'
if nome == 'rafael'.lower():
    print('Você tem o nome mais foda do mundo'.format(nome.title()))
elif nome == 'Pedro'.lower() or nome == 'Enzo'.lower() or nome == 'Lucas'.lower():
    print('Você é foda')
else:
    print('Seu nome é Comum?'.format(nome))
