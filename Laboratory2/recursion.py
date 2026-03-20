def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
    
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_acc(n, prev=1, prev2=0):
    if n == 0 :
        return prev2
    return fibonacci_acc(n-1, prev2, prev2 + prev)