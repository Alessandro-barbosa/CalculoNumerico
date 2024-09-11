print("")
'''
    2x + 3y + 1z = 9 
    4x + 7y + 3z = 19 
    1x + 1y + 2z = 8 
'''
# matrizA = [[2, 3, 1], [4, 7, 3], [1, 1, 2]]
# B = [9, 19, 8]
matrizA = [[1, 2], [3, -1]]
B = [5, 4]
# x = ['x', 'y']
a = 0
b = 0
pivo = 0
novaLinha = []
tamanho = len(matrizA[0])
for i in range(len(matrizA)):
    pivo = matrizA[a][b]
    if i == 0:
        multiplicadorDeLinha = (matrizA[a + 1][b] / pivo)
    for j in range(len(matrizA)):
        if i > 0 or i < len(matrizA[0]):
            novosValores = (matrizA[i+1][j] - (multiplicadorDeLinha * matrizA[i - 1][j]))
            print(f"novosValores {novosValores}")
print(matrizA)
