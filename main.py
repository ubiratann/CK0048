from derivate import derivate
#from parsefunction import parse
from polinomio import gerarpolinomio, gerarfuncao
import math




#x = int(input("Insira o valor de x >> "))
grau = int(input("Insira o grau do polinômio >> "))
poli = gerarpolinomio(grau)
f = gerarfuncao(poli) 
x_par = int(input("Insira o valor de x >> "))
print("Derivada primeira :::::: usando entrada")
print("forward >> %.5f"%derivate(f,x_par,0.1,'f'))
print("backward >> %.5f"%derivate(f,x_par,0.1,'b'))
print("cenral >> %.5f"%derivate(f,x_par,0.1,'c'))
#print("\n")

f = math.sin
x = math.pi/3
delta = 0.1
'''
print("Derivada primeira :::::: Exemplo em sala")
print("%.5f"%derivate(f,x,delta,'f'))
print("%.5f"%derivate(f,x,delta,'b'))
print("%.5f"%derivate(f,x,delta,'c'))

print("Derivada segunda::::::::: Exemplo em sala")
print("%.5f"%derivate(f,x,delta,'f',2))
print("%.5f"%derivate(f,x,delta,'b',2))
print("%.5f"%derivate(f,x,delta,'c',2))
'''
#usando valores do exemplo em sala

#recebendo entradas

