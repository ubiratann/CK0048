def f_backward(f, x, delta):
    return (f(x) - f(x-delta))/delta