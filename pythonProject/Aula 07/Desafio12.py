p = float(input('\033[0;30;46mInsira o valor do produto:\033[m'))
r = ((5/100)*p)
d = (p-r)
print('\033[0;34;40mO valor do produto com 5% de desconto é: {}\033[m'.format(d))
