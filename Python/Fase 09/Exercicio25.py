'''nome = str(input('Insira seu nome completo: ')).strip()
nome = nome.title()
tem_silva = 'Silva' in nome.split.()
print('Seu nome é: {}\nContém Silva? {}'.format(nome, tem_silva))'''

'''Refiz dessa forma e gostei
nome = str(input('Digite seu nome completo: ').strip())
print('Seu nome é: {} e é {} para Silva'.format(nome.title(), 'SILVA' in nome.upper()))'''
'''
Outra forma de fazer é essa porém gostei mais da minha
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva?: {}'.format('SILVA' in nome.upper()))
'''




nome = str(input('\033[4;30;41mDigite seu nome completo:\033[m ')).strip()
print('\033[4;30;41mSeu nome é: {} e é {} para Silva\033[m'.format(nome.title(), 'SILVA' in nome.upper()))









