class deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
       return self.items==[]

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)
    
    def removeRear(self):
        self.items.pop()

    def size(self):
        return len(self.items)


mydeque = deque()
mydeque.addFront('hi')
mydeque.addFront('govind')
mydeque.addRear('hello')
mydeque.addRear('baby')
print mydeque.items

mydeque.removeFront()
print mydeque.items

mydeque.removeRear()
print mydeque.items



    
