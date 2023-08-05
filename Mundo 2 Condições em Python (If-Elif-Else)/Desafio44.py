'''Elabore um programa que calcule o valor a ser pago por produto, considerando o seu preço normal e condição de pagamento
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

produto = float(input('Insira o valor do produto em Reais: '))
dolar = produto / 4.87
Forma = int(input('Qual a forma de pagamento? \n'
                  '1 - Á vista Dinheiro/Cheque | 10% desconto\n'
                  '2 - Á vista no Cartão       |  5% desconto\n'
                  '3 - Até 2x Cartão           |  0% desconto\n'
                  '4 - 3x ou mais Cartão       | 20% Juros   \n'
                  '---------------------------------------------\n'
                  ''))
print('---------------------------------------------')
desc1 = (10 * produto) / 100
prod1 = produto - desc1
dolar1 = prod1 / 4.87
if Forma == 1:
    print('O valor do produto é R${:.2f}\n'
          'Em Dolares é ${:.2f}\n'
          'O desconto ficou de R${:.2f}\n'
          'O novo valor será de R${:.2f}\n'
          'E em dolares ${:.2f}'.format(produto, dolar, desc1, prod1, dolar1))
elif Forma == 2:
    desc2 = (5 * produto) / 100
    prod2 = produto - desc2
    dolar2 = prod1 / 4.87
    print('O valor do produto é R${:.2f}\n'
          'Em Dolares é ${:.2f}\n'
          'O desconto ficou de R${:.2f}\n'
          'O novo valor será de R${:.2f}\n'
          'E em dolares ${:.2f}'.format(produto, dolar, desc2, prod2, dolar2))
elif Forma == 3:
    print('O valor do produto é R${:.2f}\n'
          'Em Dolar ficou ${:.2f} e não possui desconto.'.format(produto, dolar))
else:
    juros = (20 * produto) / 100
    prod4 = produto + juros
    dolar4 = prod4 / 4.87
    if Forma == 4:
        print('O valor do produto é R${:.2f}\n'
              'Em Dolares é ${:.2f}\n'
              'O juros ficou de R${:.2f}\n'
              'O novo valor será de R${:.2f}\n'
              'E em dolares ${:.2f}'.format(produto, dolar, juros, prod4, dolar4))
