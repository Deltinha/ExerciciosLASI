# Retorne a posição de todos os números de um determinado array, 
# entre 5 e 10. Array de exemplo: [2, 6, 1, 9, 10, 3, 27].

lista = [2, 6, 1, 9, 10, 3, 27]

def buscarNumeros(lista):
    posicoes = []
    for posicao, numero in enumerate(lista):
        if (numero >=5 and numero <=10):
            posicoes.append(posicao+1)
    print(posicoes)
    return posicoes
            

    
buscarNumeros(lista)