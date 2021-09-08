import numpy as np

A1 = np.array([
        [5, 2, 1],
        [2, 3, 1],
        [1, 1, 2]
        ], float)

A2 = np.array([
        [40, 8, 4, 2, 1],
        [8, 30, 12, 6, 2],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5],
        ], float)


def potencia(A, v0=np.array([]), tolerancia=1e-10, max_iteracoes=100000):

    if v0.size == 0:
        v0 = np.ones(np.shape(A)[0])

    vkN = np.copy(v0)

    autValN = 0
    for num_iteracoes in range(max_iteracoes):

        autValV = autValN  # step 4

        vkV = np.copy(vkN)  # step 5

        x1velho = np.divide(vkV, (np.sqrt(np.matmul(vkV.T, vkV))))  # step 6

        vkN = np.matmul(A, x1velho) # step 7

        autValN = np.matmul(x1velho.T, vkN) # step 8

        if abs(np.divide(np.subtract(autValN, autValV), autValN)) < tolerancia:  # step 9
            return autValN, x1velho


(r1, r2) = (potencia(A1))
print(f"autovalor => {r1}\nautovetor => {r2.T}")

(r1, r2) = (potencia(A2))
print(f"autovalor => {r1}\nautovetor => {r2.T}")
