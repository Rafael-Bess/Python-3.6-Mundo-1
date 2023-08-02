r = float(input('\033[4;31;40mInsira o valor em sua carteira: R$:\033[m'))
d = r / 3.27
print('\033[4;31;40mCom {:.2f} Reais você pode comprar {:.2f} Dólares\033[m'.format(r, d))
#Coloquei o f porém não sei o porque utilizar o :. e o F o 2 é a limitação de casas decimais que desejo por exemplo: R$23,(20)> casas decimais
