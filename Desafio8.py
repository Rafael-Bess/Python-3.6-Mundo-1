m = float(input('Insira quantos Metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
c = m * 100
mi = m * 1000
cores = {'l': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'corirada': '\033[4;30;45m'}
print('A medida em Quilômetros é: {}{}{}\n'
      'A medida em Hectômetro é: {}{}{}\n'
      'A medida em Decâmetro é: {}{}{}\n'
      'A medida em Metros é: {}{}{}\n'
      'A medida em Decimetro é: {}{}{}\n'
      'A medida em Centímetros é: {}{}{}\n'
      'A medida em Milímetros é: {}{}{}'.format(cores['corirada'], km, cores['l'],
                                                cores['corirada'], hm, cores['l'],
                                                cores['corirada'], dam, cores['l'],
                                                cores['corirada'], m, cores['l'],
                                                cores['corirada'], dm, cores['l'],
                                                cores['corirada'], c, cores['l'],
                                                cores['corirada'], mi, cores['l']))
