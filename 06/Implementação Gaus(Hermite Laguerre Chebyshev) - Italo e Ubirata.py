from math import sin, pi


def f(x):
    return (sin(2*x) + (4*x*x) + ((3*x)))**2


def aproximador(f, pesos, raizes):
    '''
        Função de aproximação
        pesos: vetor com pesos da aproximação
        raizes: vetor com raizes da aproximação
    '''

    resultado = 0
    for k in range(len(pesos)):
        resultado += pesos[k]*f(raizes[k])

    return resultado


def quadraturaHermite(f, n):
    '''
        Função que retorna quadratura de Gaus Hermite
        f: função
        n: numero de pontos usados
    '''

    raizes = [[-0.70710, 0.70710], [-1.22474, 0, 1.22474],
              [1.65068, 0.52464, -0.52464, -1.65068]]

    pesos = [[0.88622, 0.88622], [0.29540, 1.18163, 0.29540],
             [0.08131, 0.80492, 0.80492, 0.08131]]

    return(aproximador(f, pesos[n], raizes[n]))


def quadraturaLaguerre(f, n):
    '''
        Função que retorna quadratura de Gaus Laguerre
        f: função
        n: numero de pontos usados
    '''
    raizes = [[0.58578, 3.41421], [0.41577, 2.29428, 6.28994],
              [0.32254, 1.74576, 4.53662, 9.39507]]

    pesos = [[0.85355, 0.14644], [0.71109, 0.27851, 0.01038],
             [0.60328, 0.35742, 0.03888, 0.00053]]

    return(aproximador(f, pesos[n], raizes[n]))


def quadraturaChebyshev(f, n):
    '''
        Função que retorna quadratura de Gaus Chebyshev
        f: função
        n: numero de pontos usados
    '''
    raizes = [[0.70710, -0.70710], [-0.86602, 0, 0.86602],
              [0.92387, 0.38268, 0.38268, -0.92387]]

    pesos = [[pi/2, pi/2], [pi/3, pi/3, pi/3],
             [pi/4, pi/4, pi/4, pi/4]]

    return(aproximador(f, pesos[n], raizes[n]))


for k in range(0, 3):
    print(f'Quadratura de Gauss-Hermite usando {k+2} pontos = ' +
          f'{quadraturaHermite(f, k)}.')
print()

for k in range(0, 3):
    print(f'Quadratura de Gauss-Laguerre usando {k+2} pontos = ' +
          f'{quadraturaLaguerre(f, k)}.')
print()

for k in range(0, 3):
    print(f'Quadratura de Gauss-Chebyshev usando {k+2} pontos = ' +
          f'{quadraturaChebyshev(f, k)}.')
