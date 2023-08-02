
#PARA REALIZAR COM STRING PRECISAR UTILIZAR IF E ELSE. NÃO APRENDI AINDA
num = int(input('\033[4;30;45mDigite um numero de 0 a 9999: \033[m'))
n = str(num)
print('\033[4;30;45mAnalisando o número: {}\033[m'.format(num))
print('\033[4;30;45mUnidade: {}\033[m'.format(n[-1]))
print('\033[4;30;45mDezena: {}\033[m'.format(n[-2]))
print('\033[4;30;45mCentena: {}\033[m'.format(n[-3]))
print('\033[4;30;45mMilhar: {}\033[m'.format(n[-4]))
print('\033[4;30;45mMilhar: {}\033[m'.format(n[-4]))

'''num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('o seu número é {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''