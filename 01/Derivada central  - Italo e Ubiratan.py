import math

def f(x):
    return math.sqrt(((math.e ** (3*x)) + 4 * (x**2)))

def derivada(f, x, delta):
    '''
    Fórmula de derivada segunda desenvolvida usando expansões de Taylor
    '''
    return(-(f(x - 2 * delta)) + 16*(f(x - delta)) - 30*f(x) + 16 * f(x + delta) - f(x + 2 *delta)) / (12 * (delta**2))


def derivar(f, x, delta, erro=10**-6):

    derivadaAtual = derivada(f, x, delta)

    erroCalculado = 1

    while erroCalculado > erro:
        
        derivadaAnterior = derivadaAtual
        delta /= 2
        derivadaAtual = derivada(f, x, delta)

        erroCalculado = abs((derivadaAtual - derivadaAnterior) / derivadaAtual)
    
    return delta, derivadaAtual



particao, dx = derivar(f, 2, 0.5)
print(f'Tamanho da última partição: {particao}\nDerivada: {dx}')
