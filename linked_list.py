class Node:

    def __init__(self, value):
        self.new_node = {
            'value': value,
            'next': None
        }

class LinkedList:

    def __init__(self, value):
        self.head = Node(value).new_node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).new_node
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.values
        

    def prepend(self, value):
        new_node = Node(value).new_node
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self.values()

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self.values()
        if index >= self.length:
            self.append(value)
            return self.values()
        values = self.values()
        i = 0
        inserted = False
        while i < len(values):
            if i == 0:
                self.head = Node(values[i]).new_node
                self.tail = self.head
                self.length = 1
                i += 1
            elif i == index and inserted == False:
                self.append(value)
                inserted = True
            else:
                self.append(values[i])
                i += 1
        return self.values()

    def values(self):
        values = []
        currentNode = self.head
        while currentNode:
            values.append(currentNode['value'])
            currentNode = currentNode['next']
        return values


myLinkedList = LinkedList(10)
print(myLinkedList.values())
myLinkedList.append(5)
print(myLinkedList.values())
myLinkedList.append(30)
print(myLinkedList.values())
myLinkedList.prepend(100)
print(myLinkedList.values())
myLinkedList.insert(2, 9999)
print(myLinkedList.values())
