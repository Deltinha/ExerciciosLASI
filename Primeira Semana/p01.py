# Faça um Programa que pergunte quanto você ganha por hora e o número de 
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
# mês.

def calculaSalario ():
    valorDaHora = float(input('Quando ganha por hora? \n'))
    horasTrabalhadas = float(input('Quantas horas trabalha por mês? \n'))
    
    salario = valorDaHora * horasTrabalhadas

    print('Seu salário é de',salario, 'reais')
 
calculaSalario()
