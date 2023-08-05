nome = str(input('Insira seu nome: ')).title()
dtnasci = int(input('Insira sua data de nascimento: '))
calculo = int(2023 - dtnasci)
if calculo <= 9:
    print('Prazer {} Você é da categoria Mirim'.format(nome))
elif calculo >= 9 and calculo <= 14:
    print('Prazer {} você é da categoria Infantil'.format(nome))
elif calculo >= 14 and calculo <= 19:
    print('Prazer {} você é da categoria Junior'.format(nome))
else:
    print('Prazer {} você é da categoria Master'.format(nome))
