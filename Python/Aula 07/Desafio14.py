c = float(input('\033[4;30;41mInforme a temperatura em °C:\033[m'))
f = float(c * 1.8 + 32)
k = float(c + 273.15)
print('\033[4;30;41mA temperatura em Celsius é: {:.2f}\033[m\n'
      '\033[4;30;41mA temperatura em Fahrenheit é: {:.2f}\033[m\n'
      '\033[4;30;41mA temperatura em Kelvin é: {:.2f}\033[m'.format(c,f,k))
