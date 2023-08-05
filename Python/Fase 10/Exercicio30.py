numero = int(input('\033[4;35;40mDigite um número:\033[m'))
if numero % 2 == 0:
    print('\033[4;35;40mO número {} é par\033[m'.format(numero))
else:
    print('\033[4;35;40mO número {} é impar\033[m'.format(numero))
