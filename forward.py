def f_forward(f,x,delta,ordem):
    if (ordem == 1):
        return f_forward1(f,x,delta)
    return f_forward2(f,x,delta)

def f_forward1(f, x, delta):
    return (f(x+delta)- f(x))/delta

def f_forward2(f,x,delta):
        return(( f(x + (2*delta))- 2*f(x+delta) + f(x))/(delta*delta))