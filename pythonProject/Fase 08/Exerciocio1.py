from math import sqrt
num = int(input('Insira um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a: {:.2f}'.format(num, raiz))

#print('A raiz de {} é igual a: {:.2f}.format(num, math.ceilraiz))

#caso eu traga a biblioteca math com o from não precisa usar o math.sqrt caso eu eu traga apenas usando import math, ai eu preciso referencialo utilizando math.sqrt