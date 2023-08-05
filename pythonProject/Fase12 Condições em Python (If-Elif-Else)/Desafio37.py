'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
1 para binário
2 para Octal
3 para hexadecimal
'''
num = int(input('Insira um número qualquer: '))
forma = int(input('Qual será a forma de conversão utilizada?\n'
                  '1 - Conversão para Binário\n'
                  '2 - Conversão para Octal\n'
                  '3 - Conversão para Hexadecimal\n'
                  'Digite a forma utilizada: '))
if forma == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)))
elif forma == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)))
elif forma == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)))
else:
    print('Forma não encontrada')