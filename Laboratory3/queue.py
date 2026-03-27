class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def show(self):
        print(self.data[0])

    def __str__(self):
        return "(" + str(self.data).replace(", ", " -> ")[1:-1] + ")"

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(q)
q.show()
print(len(q))

print(q.dequeue())
q.enqueue(7)
print(q)