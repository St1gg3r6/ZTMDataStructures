class HashTable:

    def __init__(self, size):
        self.size = size
        self.data = [None for i in range(self.size)]

    def _hash(self, key):
        hash = 0
        for i, char in enumerate(key):
            hash = (hash + ord(char) * i) % self.size
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        if address not in self.data:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_data = self.data[address]
        if current_data:
            for i in range(len(current_data)):
                if current_data[i][0] == key:
                    return current_data[i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(self.size):
            if self.data[i]:
                keys.append(self.data[i][0][0])
        return keys

    def items(self):
        items = []
        for i in range(self.size):
            if self.data[i]:
                items.append((i, self.data[i]))
        return items


myHash = HashTable(50)

myHash.set('grapes', 10000)
print(myHash.get('grapes'))
myHash.set('apples', 9)
print(myHash.get('apples'))
print(myHash.keys())
myHash.set('grapfs', 20000)
myHash.set('ab', 10)
myHash.set('ba', 15)
print(myHash.keys())
print(myHash.items())