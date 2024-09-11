print("")
'''
    2x + 3y + 1z = 9 
    4x + 7y + 3z = 19 
    1x + 1y + 2z = 8 
'''
matrizA = [[2, 3, 1], [4, 7, 3], [1, 1, 2]]
B = [9, 19, 8]
#matrizA = [[1, 2], [3, -1]]
#B = [5, 4]
# x = ['x', 'y']
#novosValores = (matrizA[i+1][j] - (multiplicadorDeLinha * matrizA[i - 1][j]))
linha = 0
b = 0
novaLinha = []
pivo = matrizA[linha][b]
pivo = float(pivo)
for i in range(len(matrizA)):
    if i < len(matrizA[0]) - 1:
        multiplicadorDeLinha = (matrizA[i + 1][b] / pivo)
    for j in range(len(matrizA)):
        if i == 0:
            novaLinha.append(matrizA[i + 1][j] -
                             (multiplicadorDeLinha * matrizA[i][j]))
    if i < len(matrizA[0]) - 1:
        matrizA[linha + 1] = novaLinha
        linha += 1
        b += 1
        pivo = matrizA[linha][b]
print(novaLinha)
print(matrizA)
