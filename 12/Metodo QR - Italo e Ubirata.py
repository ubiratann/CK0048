import numpy as np
import math



A = np.array(
       [[40,8,4,2,1], 
       [8,30,12,6,2], 
       [4,12,20,1,2],
       [2,6,1,25,4], 
       [1,2,2,4,5]])

def householderColunaAnterior(colunaAnt, i, n):
    w = np.zeros(n)
    wLinha = np.zeros(n)
    w[i+1:] = colunaAnt[i+1:]

    wLinha[i+1] = - np.sign(w[i+1]) * np.linalg.norm(w) #achei no wikipedia nao sei a explicação :(
    
    m = (1 / np.linalg.norm(w - wLinha) * (w - wLinha)).reshape(-1, 1)

    return np.eye(n) - 2 * np.matmul(m, m.T)


def householder(matriz, n):
    '''Método de Househoulder'''
    h = np.eye(n)
    matrizAntiga = matriz

    for i in range(n-2):
        hColunaI = householderColunaAnterior(matrizAntiga[:, i], i, n )
        matrizNova = np.matmul(np.matmul(hColunaI.T, matrizAntiga), hColunaI)
        matrizAntiga = matrizNova
        h = np.matmul(h, hColunaI)
    
    return matrizNova, h


def gerarMatrizElementoIJ (matriz, i, j, n, erro = 10**-6):

    teta = 0

    # matriz = np.matrix(matriz)
    J = np.eye(n)

    if abs(matriz[i,j]) <= erro:
        return J

    if abs(matriz[j,j]) <= erro:
        if matriz[i,j] < 0:
            teta = (math.pi)/2
        else:
            teta = - (math.pi)/2
    
    else:
        teta = math.atan( -(matriz[i,j]) / matriz[j,j])
    
    J[i,i]  = math.cos(teta)
    J[j,j]  = math.cos(teta)
    J[i,j]  = math.sin(teta)
    J[j,i]  =- math.sin(teta)

    return J


def decomporQR(matriz, n):
    QT = np.eye(n)
    rAntigo = matriz

    for j in range (n - 1):
        for i in range (j+1, n):
            matrizIJ = gerarMatrizElementoIJ(rAntigo, i, j, n)
            rNovo = np.dot(matrizIJ, rAntigo)
            rAntigo = rNovo
            QT = np.dot(matrizIJ, QT)

    Q = np.transpose(QT)
    R = rNovo

    return Q,R


def somarQuadradosDiagonal(matriz, n):
    retorno = 0
    for i in range (n-1):
        for j in range(i + 1, n):
            retorno += math.pow(matriz[i, j], 2)
    return retorno


def QR(matriz, n, erro=10**-6):
    diagonal = np.zeros(n)
    erroMinimo = 100

    P = np.eye(n)
    matrizAntiga = matriz

    while (erroMinimo > erro):
        (Q, R) = decomporQR(matrizAntiga, n)
        matrizNova = np.dot(R,Q)
        matrizAntiga = matrizNova

        P = np.dot(P, Q)

        # item de mostrar a matriz a cada iteração, suja muito o terminal
        # print()
        # print('Matriz Acumulada QR')
        # print(matrizNova)
        # print()

        
        erroMinimo = somarQuadradosDiagonal(matrizNova, n)

    for i in range (n):
        diagonal[i] = matrizNova[i,i]
    
    return P,diagonal

matrizHouseholder, h = householder(A, A.shape[0])
np.set_printoptions(precision=6)
print('H = ')
print(h)
print()
print('A = ')
print(matrizHouseholder)

p, matrizQR= QR(matrizHouseholder, 5)

print('P = ')
print(p)
print('')
print('HP(Autovetores) = ')
print(np.dot(h, p))
print('')
print('Autovalores = ')
print(np.transpose([matrizQR]))


