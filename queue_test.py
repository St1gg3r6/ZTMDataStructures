class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({{'value': {self.value}, 'next': {self.next}}})"
    

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        return str(self.first)
    
    def peek(self):
        if self.length > 0:
            return self.first.value
        return None
    
    def enqueue(self, value):
        if self.length == 0:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            new_node.next = self.first
            self.first = new_node
        self.length += 1

    def dequeue(self):
        if self.length >= 1:
            value = self.first.value
            self.first = self.first.next
            if self.length == 1:
                self.first = None
                self.last = None
            self.length -= 1
            return value
        return None
    

myqueue = Queue()
vals = ["First", "Second", "Third"]
for val in vals:
    myqueue.enqueue(val)
    print(myqueue)
print()
for val in vals:
    myqueue.dequeue()
    print(myqueue)

    