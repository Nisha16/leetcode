	
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear(16)
d.addFront(24)
d.addFront(6)
print(d.size())
print(d.isEmpty())
d.addRear(12)
print(d.removeRear())
print(d.removeFront())