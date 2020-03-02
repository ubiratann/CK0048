from derivate import derivate
#from parsefunction import parse
import math


f = math.sin
x = math.pi/3
delta = 0.1

print("Derivada primeira ::::::")
print("%.5f"%derivate(f,x,delta,'f'))
print("%.5f"%derivate(f,x,delta,'b'))
print("%.5f"%derivate(f,x,delta,'c'))

print("Derivada segunda:::::::::")
print("%.5f"%derivate(f,x,delta,'f',2))
print("%.5f"%derivate(f,x,delta,'b',2))
print("%.5f"%derivate(f,x,delta,'c',2))

#usando valores do exemplo em sala

#recebendo entradas

