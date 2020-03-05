def f_central(f,x,delta,ordem):
    if(ordem == 1):
       return  f_central1(f,x,delta)
    return f_central2(f,x,delta)

def f_central1(f, x, delta):
    return (f(x+delta)- f(x-delta))/(2*delta)

def f_central2(f, x, delta):
    return((f(x+delta)-2*f(x)+f(x-delta))/(delta*delta))  