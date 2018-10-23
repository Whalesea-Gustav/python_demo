class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(nameList, num):
    q1 = Queue()

    for name in nameList:
        q1.enqueue(name)

    while q1.size() > 1:

        for i in range(num):
            q1.enqueue(q1.dequeue())

        q1.dequeue()

    return q1.dequeue()


