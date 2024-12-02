class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({{'value': {self.value}, 'next': {self.next}}})"


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):
        return str(self.top)

    def peek(self):
        if self.length > 0:
            return self.top.value
        return None

    def push(self, value):
        if self.length == 0:
            self.top = Node(value)
            self.bottom = self.top
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length > 0:
            value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return value
        return None

    def isEmpty(self):
        pass


myStack = Stack()
myStack.push("First")
print(myStack.top.value)
myStack.push("Second")
print(myStack.top.value)
myStack.push("Third")
print(myStack.top.value)

print()
print(myStack)
print()

print(myStack.peek())

print(myStack.pop())
print(myStack.top.value)
print(myStack.pop())
print(myStack.top.value)
print(myStack.pop())

print()
print(myStack)
print()