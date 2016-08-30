class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def rear(self):
        return self.items[0]

    def front(self):
        return self.items[len(self.items) - 1]           
q = Queue()

q.enqueue(4)
q.enqueue(24)
q.enqueue(16)
print(q.size())
print(q.front())
print(q.rear())
