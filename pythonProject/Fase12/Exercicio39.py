nome = str(input('Digite seu nome: ')).title()
dtnasci = int(input('Digite o Ano do seu nascimento: '))
dtatual = int(input('Digite o ano atual: '))
idade = int(dtatual - dtnasci)
atual = int(dtnasci + 18)
falta = (atual - idade - dtnasci)
if idade == 17 or idade == 16:
    print('{} Você já tem {} e pode realizar a inscrição para o alistamento obrigatório\n'
          'faltam {} para expirar'.format(nome, idade, falta))
elif idade == 18:
    print('{} Você precisa se Comparecer a junta militar para o alistamento obrigatório'.format(nome))
else:
    print('Seu prazo de alistamento expirou ou você não possui 16 anos,\n'
          'data de expiração {} '.format(atual))
