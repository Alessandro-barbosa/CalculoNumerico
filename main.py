import numpy as np

print("")
'''
    2x + 3y + 1z = 9 
    4x + 7y + 3z = 19 
    1x + 1y + 2z = 8 
'''


def triangularSuperior():
    # matrizA = [[2, 3, 1], [4, 7, 3], [1, 1, 2]]
    # B = [9, 19, 8]
    matrizA = [[3, 2, 4], [1, 1, 2], [4, 3, -2]]
    B = [1, 2, 3]
    # matrizA = [[2, -3], [4, 1]]
    # matrizA = [[1, 2], [3, -1]]
    # B = [5, 4]
    # x = ['x', 'y']
    # novosValores = (matrizA[i+1][j] - (multiplicadorDeLinha * matrizA[i - 1][j]))
    linha = 0
    b = 0
    coluna = 0
    novaLinha = []
    # pivo começa com matriz[1][1]
    pivo = matrizA[linha][b]
    mlinhas = []
    # multiplicador de linha coluna 0
    coluna = 0
    for i in range(1, len(matrizA)):
        multiplicadorDeLinha = (matrizA[coluna][i] / pivo)
        mlinhas.append(multiplicadorDeLinha)
        #print(multiplicadorDeLinha)
    a = 0
    print(f"multiplicadores: {mlinhas
    }")
    for i in range(1, len(matrizA)):
        for j in range(len(matrizA)):
            novaLinha.append(matrizA[i - 1][j] - (mlinhas[a] * matrizA[i][j]))
    print(f"Linhas {novaLinha}")
    matrizA[i-1] = novaLinha[i - 1]
    a += 1
    print(matrizA)


    '''
    for i in range(0, len(matrizA)):
        if i < len(matrizA[coluna]) - 1:
            multiplicadorDeLinha = (matrizA[i + 1][coluna] / pivo)
        for j in range(len(matrizA)):
            if i == 0:
                # linhas calculadas
                novaLinha.append(matrizA[i + 1][j] - (multiplicadorDeLinha * matrizA[i][j]))
        if i < len(matrizA[0]) - 1:
            # trocas de linhas
            matrizA[linha + 1] = novaLinha
            linha += 1
            b += 1
            pivo = matrizA[linha][b]

    print("Matriz triangular Superior: ")
    for i in range(len(matrizA)):
        for j in range(len(matrizA)):
            print(matrizA[i][j], end=" ")
        print()
    '''


triangularSuperior()
s
