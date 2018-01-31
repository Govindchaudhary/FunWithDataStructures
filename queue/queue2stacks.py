class Queue2stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,item):
        self.stack1.insert(0,item)
        
    
    def dequeue(self):
        while len(self.stack1)!=0:
            element = self.stack1.pop(0)
            self.stack2.insert(0,element)
        
        element = self.stack2.pop(0)
        return element
    
myQueue = Queue2stacks()
for i in xrange(5):
    myQueue.enqueue(i)

for j in xrange(5):
    print myQueue.dequeue()
    


       