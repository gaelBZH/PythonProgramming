from time import sleep

e = "🌍"
i = 0
b = True
while True:
    print(e*i)
    if b:
        i += 1
    else:
        i -=1
    
    if i == 0 or i == 45:
        b = not b
    
    sleep(0.01)