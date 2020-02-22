from forward import *
from backward import *
from central import *
import math


print("forward -> %.5f"%(f_forward(math.sin,(math.pi/3),0.1)))
print("backward -> %.5f"%(f_backward(math.sin,(math.pi/3),0.1)))
print("central -> %.5f"%(f_central(math.sin,(math.pi/3),0.1)))