def f():
    x = "I am local"
    print(x)

x = "I am global"
f()
print(x)

x = "Global value"
def g():
    print(x) # does not find it in local, try to find in global
g()