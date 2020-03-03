from forward import f_forward
from backward import f_backward
from central import f_central


def derivate(f,x,delta,filosofia,ordem =1):
    if filosofia[0] == 'f':
        return (f_forward(f,x,delta,ordem))
    if filosofia[0] == 'b':
        return (f_backward(f,x,delta,ordem))
    if filosofia[0] == 'c':
        return (f_central(f,x,delta,ordem))