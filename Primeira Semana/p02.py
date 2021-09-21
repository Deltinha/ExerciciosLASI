# Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem 
# compradas e os respectivos preços em 2 situações: 
# • comprar apenas latas de 18 litros; 
# • comprar apenas galões de 3,6 litros; 

import math

def precoEmGaloes(litrosAGastar):
    return math.ceil(litrosAGastar/3.6)*25

def precoEmLatas(litrosAGastar):
    return math.ceil(litrosAGastar/18)*80

def calcularOrcamento():
    areaAPintar = float(input('Insira a área a ser pintada em m²: '))
    litrosAGastar = areaAPintar / 6

    print('Você deve comprar no mínimo', round(litrosAGastar, 2), 'litros de tinta.\nA opções são:')
    print(precoEmGaloes(litrosAGastar), 'reais em galões de 3.6 litros;');
    print(precoEmLatas(litrosAGastar), 'reais em latas de 18 litros.');

calcularOrcamento()