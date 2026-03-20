# Standard
L1 = [2**i for i in range(10)]
L2 = [x**2 for x in range(10)]
print(L1)
print(L2)

# With Conditions
L3 = [x for x in range(10) if x%2==0]
print(L3)

# Iterate another List
L4 = [i+1 for i in L3]
print(L4)

# Plot
from math import log as ln
xs = [0.1 * i for i in range(1, 50)]
ys = [ln(x) for x in xs]
#print(ys)

# Words
words = input("words : ").split()
data = [(w, w.upper(), w.capitalize(), w.lower(), len(w)) for w in words]
print(data)