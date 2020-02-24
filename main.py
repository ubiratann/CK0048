from forward import *
from backward import *
from central import *
#from parsefunction import parse
from math import *
import parser

#usando valores do exemplo em sala
print("forward -> %.5f"%(f_forward(sin,( pi/3),0.1)))
print("backward -> %.5f"%(f_backward(sin,(pi/3),0.1)))
print("central -> %.5f"%(f_central(sin,(pi/3),0.1)))

#recebendo entradas

flag = True
while(flag == True):
    filo = 0
    while(5<filo or filo<1):
        print("<<< Escolha a filosofia que deseja --- ou encerre o programa >>>")
        print("(1)Forward\n(2)Backward\n(3)Central\n(4)Encerrar")
        filo = int(input("Insira a filosofia que deseja ->"))
        if (5<filo or filo<1) :
            print("entrada inválida!!!")
    
    if (4> filo and filo>0):
        f = str(input("Insira a funcao que deseja usar ->"))
        

    else:
        exit()