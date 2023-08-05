a=float(input('\033[4;31;40mDigite a altura da parede em metros:\033[m'))
c=float(input('\033[1;30;45mDigite a comprimento da parede em metros::\033[m'))
r= a*c
qt=(r/(2**2))
print('\033[1;30;45mSua área é de {:.2f}m²\033[m\n'
      '\033[1;30;45mA quantidade de tinta utilizada será {:.3f}ML\033[m'.format(r,qt))
