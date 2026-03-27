def make_adder(y):
    def adder(x, y=y):
        return x + y
    return adder

add42 = make_adder(42)
add10 = make_adder(10)

print(add42(1), add10(1))