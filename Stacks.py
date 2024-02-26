class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

# Example
if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.isEmpty())  # true
    s.push(1)
    s.push(2)
    s.push(3)
    print("Stack size:", s.size())
    print("Top element:", s.peek())
    print("Pop:", s.pop())
    print("Stack size after pop:", s.size())
