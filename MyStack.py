class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (len(self.items) == 0)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

stack1 = Stack()

stack1.push(4)

print(stack1.items)