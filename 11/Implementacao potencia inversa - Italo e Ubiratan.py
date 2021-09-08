import numpy as np


def potenciaInversa(A, v0=np.array([]), tolerancia=1e-10, maxIteracoes=10000):
    '''
    A : Matriz de Entrada
    v0: vetor de entrada
    tolerancia: Erro mínimo
    maxIteracoes: Número máximo de iteracoes desejada
    '''

    if v0.size == 0:
        v0 = np.ones(np.shape(A)[0])

    autValN = 0  # step 3
    vkN = np.copy(v0)  # step 4

    for i in range(maxIteracoes):
        autValV = np.copy(autValN)  # step 5
        vkV = np.copy(vkN)  # step 6
        x1V = np.divide(vkV, (np.sqrt(np.dot(vkV.T, vkV))))  # step 7
        vkN = np.dot(np.linalg.inv(A), x1V)  # step 8
        autValN = np.matmul(x1V.T, vkN)  # step 9

        if abs(np.divide(np.subtract(autValN, autValV), autValN)) < tolerancia:  # step 9
            break

    autValF = 1 / autValN  # step 11
    xn = np.copy(x1V)  # step 12
    return(autValF, xn)


def potenciaInversaDeslocamento(A, u=0, v0=np.array([]), tolerancia=1e-10):

    Ai = np.eye(np.shape(A)[0])  # matriz identidade de A

    if v0.size == 0:  # iniciando o vetor de chutes com 1 em todas as posicoes
        v0 = np.ones(np.shape(A)[0])
    A_ = (np.subtract(A, (u*Ai)))  # step 1

    autValV, x = potenciaInversa(A_, v0, tolerancia)  # step 2

    autValN = autValV+u  # step 3
    xi = x  # step 4
    return autValN, xi


A1 = np.array([
    [5, 2, 1],
    [2, 3, 1],
    [1, 1, 2]
    ], float)


A2 = np.array([
    [-14, 1, -2],
    [1,  -1,  1],
    [-2,  1, -11]
    ], float)


A3 = np.array([
    [40, 8,  4,  2, 1],
    [8, 30, 12,  6, 2],
    [4, 12, 20,  1, 2],
    [2,  6,  1, 25, 4],
    [1,  2,  2,  4, 5]
    ], float)


print(f"::::::::::::::::::::::::::::::::::::::\n MATRIZ A1")
print('Potencia Inversa')
lamb, x = potenciaInversa(A1)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')
print('\nPotencia Inversa Com Deslocamento')
lamb, x = potenciaInversaDeslocamento(A1)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')

print()
print(f"::::::::::::::::::::::::::::::::::::::\n MATRIZ A2")
print('Potencia Inversa')
lamb, x = potenciaInversa(A2)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')
print('\nPotencia Inversa Com Deslocamento')
lamb, x = potenciaInversaDeslocamento(A2)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')

print()
print(f"::::::::::::::::::::::::::::::::::::::\n MATRIZ A3")
print('Potencia Inversa')
lamb, x = potenciaInversa(A3)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')
print('\nPotencia Inversa Com Deslocamento')
lamb, x = potenciaInversaDeslocamento(A3)
print(f' autovalor => {lamb}')
print(f' autovetor => {x}')
