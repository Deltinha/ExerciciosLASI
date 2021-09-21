# Desenvolva um algoritmo que calcule e imprima o valor de A dado por:  

#     A = N + ( N - 1 ) / 2 + ( N - 2 ) / 3 + ... + 1 / N

# Onde N é um número inteiro positivo que deve ser lido inicialmente. 

def iterarSoma(N):
    A = 0
    for i in range(N):
        A += (N - i) / (i + 1)

    return A

def calcularA():
    N = int(input('Insira um número inteiro positivo: '))
    
    print('O valor de A é',round(iterarSoma(N), 2))

calcularA()