'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
o programa vai perguntar o
valor da casa,
o salário do comprador
em quantos anos ele vai pagar.


Calcule o valor da prestãção Mensal,
Sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
'''

valor = float(input('insira o valor da casa R$: '))
salario = float(input('Insira o seu salário R$: '))
anos = int(input('Insira quantos anos serão pagos: '))
meses = int(anos * 12)
prestacao = int(valor / meses)
porcentagem = int((salario * 30) / 100)
    if  prestacao <= porcentagem:
        print('É possivel realizar a compra da casa')
    else:
        print('Não é possivel liberar o emprestimo.')
