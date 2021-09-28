# Construa uma função que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato DD de mesPorExtenso de AAAA. Valide a data e 
# retorne NULL caso a data seja inválida.

import re

def receberData():
    data = str(input('Insira uma data no formado DD/MM/AAAA\n'))
    validarData(data)

def retornarData(data):
    dataPorExtenso = f'{data[0]} de {data[1]} de {data[2]}'
    print(dataPorExtenso)
    return dataPorExtenso
    
def separarData(data):
    sliceDay = slice(2)
    sliceMonth = slice(3,5)
    sliceYear = slice(6,11)

    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

    dia = data[sliceDay]
    mes = int(data[sliceMonth].lstrip("0"))
    ano = data[sliceYear]
    mesPorExtenso = meses[mes - 1]

    dataList = [dia,mesPorExtenso,ano]
    retornarData(dataList)

def validarData(data):
    if (re.search("^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$",data) == None):
        print('Formato errado.')
        return None
    else:
        separarData(data)

receberData()
