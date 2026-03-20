def f():
    global x
    x = x+1

x = 10
print(x)
f()
print(x)