def f_backward(f,x,delta,ordem):
    if(ordem == 1):
        return f_backward1(f,x,delta)
    return  f_backward2(f,x,delta)

def f_backward1(f, x, delta):
    return (f(x) - f(x-delta))/delta

def f_backward2(f, x, delta):
        return(( f(x)- 2*f(x-delta) + f(x - (2*delta)))/(delta*delta))