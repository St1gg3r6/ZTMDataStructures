class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value


class LinkedList:

    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return self.values()
    
    def prepend(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.values()

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)
        newNode = Node(value)
        prevNode = self.find(index - 1)
        tempPointer = prevNode.next
        newNode.prev = prevNode
        prevNode.next = newNode
        tempPointer.prev = newNode
        newNode.next = tempPointer
        self.length += 1
        return self.values()

    def remove(self, index):
        prevNode = self.find(index - 1)
        nodeToRemove = prevNode.next
        nextNode = nodeToRemove.next
        nextNode.prev = prevNode
        prevNode.next = nodeToRemove.next
        self.length -= 1
        return self.values()
    
    def reverse(self):
        if self.length == 1:
            return self.values()
        items = self.values()
        penultimate = self.length - 2
        self.__init__(items[-1])
        for index in range(penultimate, -1, -1):
            self.append(items[index])
        return self.values()
    
    def find(self, index):
        if index >= self.length:
            return self.tail
        if index == 0:
            return self.head
        count = 0
        currentNode = self.head
        while count != index:
            currentNode = currentNode.next
            count += 1
        return currentNode

    def values(self):
        values = []
        currentNode = self.head
        while currentNode:
            values.append(currentNode.value)
            currentNode = currentNode.next
        return values


myLinkedList = LinkedList(10)
print(myLinkedList.values())
print(myLinkedList.append(20))
print(myLinkedList.append(10))
print(myLinkedList.prepend(5))
print(myLinkedList.insert(2, 30))
print(myLinkedList.remove(2))
print(myLinkedList.insert(100, 100))
print(myLinkedList.reverse())
for i in range(myLinkedList.length):
    try:
        print(f'Previous Value: {myLinkedList.find(i).prev.value}')
    except:
        print('Previous Value: None')
    try:
        print(f'Next Value: {myLinkedList.find(i).next.value}')
    except:
        print('Next Value: None')