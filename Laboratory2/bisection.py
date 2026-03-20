def bisection(f, a, b, precision=10e-7):
    x = (a+b)/2
    while abs(f(x)) > precision:
        if (f(x) * f(a) > 0):
            a = x
        else:
            b = x
        x = (a+b)/2
    return x

print(bisection(lambda x : x - 5, 0, 12))