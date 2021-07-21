import math


def intervaloFechado(limIferior, limSuperior, grauPolinomio):
    h = (limSuperior-limIferior)/(grauPolinomio)
    pontos = []
    for i in range(grauPolinomio+1):
        pontos.append(limIferior + h*i)
    return (h, pontos)


def intervaloAberto(limIferior, limSuperior, grauPolinomio):
    h = (limSuperior-limIferior)/(grauPolinomio + 2)
    pontos = []
    for i in range(grauPolinomio+1):
        pontos.append(limIferior + h*(i+1))
    return (h, pontos)


def aproximador(funcao, a, b, numDivisoes, grau, fechado):

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
    calcularPontos = intervaloAberto

    total = 0
    qntDivisoes = (2**numDivisoes)
    Dx = (b - a) / qntDivisoes

    for i in range(qntDivisoes):
        xi = a + i*Dx
        xf = xi + Dx
        h, pontos = calcularPontos(xi, xf, grau)

        acumulador = 0
        for j in range(len(pesos)):
            acumulador += pesos[j] * funcao(pontos[j])

        total += acumulador * ((h*multiplicador) / divisor)
    return total


def newcotes(funcao, grau, fechado, limIferior=0, limSuperior=1):

    erro = 10**(-6)

    anterior = aproximador(funcao, limIferior, limSuperior, 0, grau, fechado)
    atual = aproximador(funcao, limIferior, limSuperior, 1, grau, fechado)
    iteracoes = 1

    while(abs(anterior - atual) > erro):
        if iteracoes == 10:
            break
        iteracoes += 1
        anterior = atual
        atual = aproximador(funcao, limIferior, limSuperior,
                            iteracoes, grau, fechado)

    return atual


def derivadaSimples():

    def xs(a, b):
        return lambda z: (a+b)/2 + (b-a) * math.tanh(z)/2

    def dxs(a, b):
        return lambda z: (b-a) / (2 * math.cosh(z)*math.cosh(z))

    return xs, dxs


def derivadaComposta():

    def xs(a, b):
        return lambda z: (a+b)/2 + (b-a) * math.tanh(math.pi/2*math.sinh(z))/2

    def dxs(a, b):
        pi2 = (math.pi/2)
        return lambda z: ((b-a)/2)*(pi2*(math.cosh(z)/(math.cosh(pi2*math.sinh(z))**2)))

    return xs, dxs


def q1Simples(limite):
    xs, dxs = derivadaSimples()

    def f(s):
        a = -1
        b = 1
        denominador = math.pow(math.pow(xs(a, b)(s), 2), (1/3))
        denominador = 0.00000000001 if denominador == 0 else denominador
        return (1 / denominador) * dxs(a, b)(s)

    a = limite*-1
    b = limite

    return newcotes(f, 2, False, a, b)


def q1Composta(limite):
    xs, dxs = derivadaComposta()

    def f(s):
        a = -1
        b = 1
        denominador = math.pow(math.pow(xs(a, b)(s), 2), (1/3))
        denominador = 0.00000000001 if denominador == 0 else denominador
        return (1 / denominador) * dxs(a, b)(s)

    a = limite*-1
    b = limite

    return newcotes(f, 2, False, a, b)


def q2Simples(limite):
    xs, dxs = derivadaSimples()

    a = limite*-1
    b = limite

    def f(s):
        a = -2
        b = 0

        denominador = math.sqrt(4-(xs(a, b)(s) ** 2))
        denominador = 0.00000000001 if denominador == 0 else denominador
        return (1 / denominador) * dxs(a, b)(s)

    return newcotes(f, 2, False, a, b)


def q2Composta(limite):
    xs, dxs = derivadaComposta()

    a = limite*-1
    b = limite

    def f(s):
        a = -2
        b = 0

        denominador = math.sqrt(4-(xs(a, b)(s) ** 2))
        denominador = 0.00000000001 if denominador == 0 else denominador
        return (1 / denominador) * dxs(a, b)(s)

    return newcotes(f, 2, False, a, b)


print('Derivada simples Q1: ')
for i in range(2, 5):
    print(f' N={i} ; Valor={q1Simples(i)}')
print()
print('Derivada composta Q1: ')
for i in range(2, 5):
    print(f'N={i} ; Valor={q1Composta(i)}')

print()
print('Derivada simples Q2: ')
for i in range(2, 5):
    print(f'N={i} ; Valor={q2Simples(i)}')

print()
print('Derivada composta Q2: ')
for i in range(2, 5):
    print(f'N={i} ; Valor={q2Composta(i)}')
