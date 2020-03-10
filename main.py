from derivacao.derivada import derivada
from derivacao.polinomio import gerarpolinomio, gerarfuncao
import math


#x = int(input("Insira o valor de x >> "))
grau = int(input("Insira o grau do polinômio >> "))
poli = gerarpolinomio(grau)
f = gerarfuncao(poli) 
x_par = int(input("Insira o valor de x >> "))

z = 1 
while(z <3):
  print("Derivada de %d° ordem :::::: usando entrada"%z)
  print("forward >> %.5f"%derivada(f,x_par,0.1,'f',z))
  print("backward >> %.5f"%derivada(f,x_par,0.1,'b',z))
  print("cenral >> %.5f"%derivada(f,x_par,0.1,'c',z))
  z +=1


'''

######## usando valores do exemplo em sala

f = math.sin
x = math.pi/3
delta = 0.1

print("Derivada primeira :::::: Exemplo em sala")
print("%.5f"%derivate(f,x,delta,'f'))
print("%.5f"%derivate(f,x,delta,'b'))
print("%.5f"%derivate(f,x,delta,'c'))

print("Derivada segunda::::::::: Exemplo em sala")
print("%.5f"%derivate(f,x,delta,'f',2))
print("%.5f"%derivate(f,x,delta,'b',2))
print("%.5f"%derivate(f,x,delta,'c',2))
'''


