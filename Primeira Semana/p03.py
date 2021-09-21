# Faça um algoritmo para ler o saldo de 10 (dez) clientes de um banco. Calcular e 
# imprimir:  
# • o saldo médio dos clientes 
# • a porcentagem de clientes com saldo devedor 
# • o número de clientes com saldo credor

def obterSaldos():
    nDevedores = 0
    nCredores = 0
    saldoTotal = 0
    
    for i in range(10):
        
        saldoClientei = float(input('Insira o saldo do cliente nº{} '.format(i)))

        saldoTotal += saldoClientei

        if saldoClientei < 0:
            nDevedores += 1
        elif saldoClientei > 0:
            nCredores += 1
        
    if saldoTotal != 0:
        saldoMedio = round(saldoTotal/10,2)
    else:
        saldoMedio = 0
    
    if nDevedores > 0:
        pctDevedores = round(100*(10/nDevedores))
    else:
        pctDevedores = 0

    print('O saldo médio é de ', saldoMedio, 'reais')
    print('A porcentagem de devedores é', pctDevedores,'%')
    print('O número de credores é', nCredores)

obterSaldos()