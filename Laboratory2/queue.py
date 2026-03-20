q = []

def add(name):
    q.append(name)
    print(f'"{name}" has been added to the queue.')

def next():
    return q.pop(0)

def length():
    return len(q)

def show():
    print("\n")
    print("="*5, f"Queue (len={length()}):", "="*5)
    for i in range(len(q)):
        print(q[i])
    print("="*26, "\n")



if __name__ == "__main__":
    add("Michel")
    add("Jean")
    add("Paul")
    show()
    print(f"The next is {next()}.")
    add("Patrick")
    print(f"\tbah alors... On attend pas Patrick ?")
    show()
