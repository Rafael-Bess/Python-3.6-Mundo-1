s =float(input('\033[4;31;40mQual o seu salario? R$\033[m'))
d=int(input('\033[4;31;40mQuantos % de aumento:\033[m'))
a = (s * d / 100)
ns = (s+a)
print('\033[4;31;40mO seu novo sálario é: {:.2f}\033[m'.format(ns))

