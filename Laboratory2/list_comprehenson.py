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