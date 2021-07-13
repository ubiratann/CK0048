import math

def funcao(x):
    return ( math.sin(2*x) + (4*x*x) + ((3*x)) )**2

def h_fechado(limite_inferior, limite_superior, grau_polinomio):
    h = (limite_superior-limite_inferior)/(grau_polinomio)
    pontos = []
    for i in range(grau_polinomio+1):
        pontos.append(limite_inferior + h*i)
    return (h, pontos)

def h_aberto(limite_inferior, limite_superior, grau_polinomio):
    h = (limite_superior-limite_inferior)/(grau_polinomio +2)
    pontos = []
    for i in range(grau_polinomio+1):
        pontos.append(limite_inferior + h*(i+1))
    return (h, pontos)

def aproximador(funcao, a, b, n_divisoes,grau,fechado):
    if(fechado):
        if (grau == 1):
            pesos = [1,1]
            divisor = 2
            multiplicador = 1

        if (grau == 2):
            pesos = [1,4,1]
            divisor = 3
            multiplicador = 1

        if (grau == 3):
            pesos = [1,3,3,1]
            divisor = 8
            multiplicador = 3

        if (grau == 4):
            pesos = [14, 64, 24, 64, 14]
            divisor = 45
            multiplicador = 1
        calcularPontos = h_fechado
    else:
        if (grau == 1):
            pesos = [1,1]
            multiplicador = 3
            divisor = 2

        if (grau == 2):
            pesos = [2,-1,2]
            multiplicador = 4
            divisor = 3

        if (grau == 3):
            pesos = [11,1,1,11]
            multiplicador = 5
            divisor = 24

        if (grau == 4):
            pesos = [33,-42,78,-42,33]
            multiplicador = 1
            divisor = 10
        calcularPontos = h_aberto

    soma_total = 0
    quantidade_divisoes = (2**n_divisoes)
    Dx = (b - a) / quantidade_divisoes

    for i in range(quantidade_divisoes):
        xi = a + i*Dx
        xf = xi + Dx
        h, pontos = calcularPontos(xi, xf,grau)

        soma_parcial = 0
        for j in range(len(pesos)):
            soma_parcial += pesos[j] * funcao(pontos[j])

        soma_total += soma_parcial * ((h*multiplicador) / divisor)
    return soma_total


def newcotes(funcao,grau,fechado, limite_Inf=0, limite_Sup=1 ):
    erro = 10**(-6)

    valor_anterior = aproximador(funcao, limite_Inf, limite_Sup, 0,grau, fechado)
    valor_atual = aproximador(funcao, limite_Inf, limite_Sup, 1,grau, fechado)
    iteracoes = 1
    while( abs(valor_anterior - valor_atual) > erro):
        iteracoes+=1
        valor_anterior = valor_atual
        valor_atual = aproximador(funcao, limite_Inf, limite_Sup, iteracoes, grau,fechado)

    return (iteracoes, valor_atual)



print("Aproximacao com filosofia fechada de grau 4")
for k in range (4):
    i=  newcotes(funcao, k+1,True,limite_Inf=0, limite_Sup=1)
    print("Aproximação com polinomio de grau {}= {}".format(k+1,i[1]))
    print("Numero de particoes = 2^{}\n".format(i[0]))

print("")
print("Aproximacao com filosofia aberta de grau 4")
for j in range (4):
    i =  newcotes(funcao, j+1,True,limite_Inf=0, limite_Sup=1)
    print("Aproximação com polinomio de grau {}= {}".format(j+1,i[1]))
    print("Numero de particoes = 2^{}\n".format(i[0]))
