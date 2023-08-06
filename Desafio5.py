n = int(input('\033[0;31;45mInsira um número:\033[m '))
s = n + 1
a = n - 1
print('\033[4;30;45mAnalisando o valor {}, O sucessor é {} e o antecessor é {}0\033[m'.format(n,s,a))
#as variaveis podem ser substituidas por >>
#print('O sucessor é {} eo antecessor é {}'.format(n,(n+1),(n-1)))