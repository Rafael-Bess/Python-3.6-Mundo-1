'''
print ('\033[4;30;45mOlá, Mundo!\033[m')
Para parar o back (45) usar \033[m
Foto das cores no discord Silent Heaven
'''

nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'corirada': '\033[4;30;45m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

'''
print ('\033[4;30;46mOlá, Mundo!\033[m')
a = 3
b = 5
print ('Os valores são \033[4;30;46m{}\033[m e \033[4;30;46m{}\033[m!!'.format(a, b))
Utilizamos \033[4;30;45m antes dos colchetes {} e para fechar 
e a letra 'E' não ficar com a cor e nem os '!!' Utiliza-se\033[m
'''
