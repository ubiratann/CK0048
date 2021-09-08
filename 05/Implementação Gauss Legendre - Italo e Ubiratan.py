from math import sin


def x(xi, xf, a):
    return (xi+xf)/2 + ((xf-xi)/2)*a


def f(x):
    return (sin(2*x) + (4*x*x) + ((3*x)))**2


def aproximador(f, x, a, b, qntPontos, numeroDivisoes):

    if (qntPontos == 2):
        raizes = [-0.577350, 0.577350]
        pesos = [1, 1]

    if (qntPontos == 3):
        raizes = [-0.774597, 0, 0.774597]
        pesos = [0.555556,  0.888889, 0.555556]

    if (qntPontos == 4):
        raizes = [0.861136, 0.339981, -0.339981, -0.861136]
        pesos = [0.347854, 0.652145, 0.652145, 0.347854]

    resultado = 0
    qntDivisoes = (2**numeroDivisoes)
    Dx = (b - a) / qntDivisoes

    acumulador = 0  # resultado parcial
    for i in range(qntDivisoes):
        xi = a + i*Dx
        xf = xi + Dx

        for ak, wk in zip(raizes, pesos):
            acumulador += f(x(xi, xf, ak))*wk
    resultado = (xf-xi)/2 * acumulador

    return resultado


def calcular(f, x, qntPontos, limInferior=0, limSuperior=1):
    erro = 10**(-6)

    valorAnterior = aproximador(f, x, limInferior, limSuperior, qntPontos, 0)
    valorAtual = aproximador(f, x, limInferior, limSuperior, qntPontos, 1)
    iteracoes = 1
    while(abs(valorAnterior-valorAtual) > erro):
        iteracoes += 1
        valorAnterior = valorAtual
        valorAtual = aproximador(
            f, x, limInferior, limSuperior, qntPontos, iteracoes)

    return (iteracoes, valorAtual)


for k in range(2, 5):
    i = calcular(f, x, k, 0, 1)
    print()
    print(f"Aproximação usando {k} pontos = {i[1]}")
    print(f"Foram usadas {2** i[0]} partições")
