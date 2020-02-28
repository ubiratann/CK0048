from forward import *
from backward import *
from central import *


def derivate(f,x,delta,filosofia):
    if filosofia[0] == 'f':
        return (f_forward(f,x,delta))
    if filosofia[0] == 'b':
        return (f_backward(f,x,delta))
    if filosofia[0] == 'c':
        return (f_central(f,x,delta))