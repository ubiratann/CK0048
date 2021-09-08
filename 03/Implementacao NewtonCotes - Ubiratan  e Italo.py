import math


def funcao(x):
    return (math.sin(2*x) + (4*x*x) + ((3*x)))**2


def hFechado(limiteInf, limiteSup, grau):
    h = (limiteSup-limiteInf)/(grau)
    pontos = []
    for i in range(grau+1):
        pontos.append(limiteInf + h*i)
    return (h, pontos)


def hAberto(limiteInf, limiteSup, grau):
    h = (limiteSup-limiteInf)/(grau + 2)
    pontos = []
    for i in range(grau+1):
        pontos.append(limiteInf + h*(i+1))
    return (h, pontos)


def aproximador(funcao, a, b, numDivisoes, grau, fechado):
    if(fechado):
        if (grau == 1):
            pesos = [1, 1]
            divisor = 2
            multiplicador = 1

        if (grau == 2):
            pesos = [1, 4, 1]
            divisor = 3
            multiplicador = 1

        if (grau == 3):
            pesos = [1, 3, 3, 1]
            divisor = 8
            multiplicador = 3

        if (grau == 4):
            pesos = [14, 64, 24, 64, 14]
            divisor = 45
            multiplicador = 1
        calcularPontos = hFechado
    else:
        if (grau == 1):
            pesos = [1, 1]
            multiplicador = 3
            divisor = 2

        if (grau == 2):
            pesos = [2, -1, 2]
            multiplicador = 4
            divisor = 3

        if (grau == 3):
            pesos = [11, 1, 1, 11]
            multiplicador = 5
            divisor = 24

        if (grau == 4):
            pesos = [33, -42, 78, -42, 33]
            multiplicador = 1
            divisor = 10
        calcularPontos = hAberto

    soma_total = 0
    quantDivisoes = (2**numDivisoes)
    Dx = (b - a) / quantDivisoes

    for i in range(quantDivisoes):
        xi = a + i*Dx
        xf = xi + Dx
        h, pontos = calcularPontos(xi, xf, grau)

        soma_parcial = 0
        for j in range(len(pesos)):
            soma_parcial += pesos[j] * funcao(pontos[j])

        soma_total += soma_parcial * ((h*multiplicador) / divisor)
    return soma_total


def newcotes(funcao, grau, fechado, limiteInf=0, limiteSup=1):
    erro = 10**(-6)

    valor_anterior = aproximador(
        funcao, limiteInf, limiteSup, 0, grau, fechado)
    valor_atual = aproximador(funcao, limiteInf, limiteSup, 1, grau, fechado)
    iteracoes = 1
    while(abs(valor_anterior - valor_atual) > erro):
        iteracoes += 1
        valor_anterior = valor_atual
        valor_atual = aproximador(
            funcao, limiteInf, limiteSup, iteracoes, grau, fechado)

    return (iteracoes, valor_atual)


print("Aproximacao com filosofia fechada de grau 4")
for k in range(4):
    i = newcotes(funcao, k+1, True, 0, 1)
    print("Aproximação com polinomio de grau {}= {}".format(k+1, i[1]))
    print("Numero de particoes = 2^{}\n".format(i[0]))

print("")
print("Aproximacao com filosofia aberta de grau 4")
for j in range(4):
    i = newcotes(funcao, j+1, False, 0, 1)
    print("Aproximação com polinomio de grau {}= {}".format(j+1, i[1]))
    print("Numero de particoes = 2^{}\n".format(i[0]))
