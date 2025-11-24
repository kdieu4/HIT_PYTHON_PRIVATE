
class MyStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    def push(self, value: int):
        if self.is_full():
            print("Stack is full!")
            return
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]


stack = MyStack(5)
stack.push(1)
stack.push(9)
stack.push(1)
print(f"Is full? {stack.is_full()}")
print(f"Pop: {stack.pop()}")

print(f"Top: {stack.top()}")
