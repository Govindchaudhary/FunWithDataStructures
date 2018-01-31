class queue(object):
   def __init__(self):
      self.items = []
   
   def isEmpty(self):
      return self.items==[]

   def enqueue(self,item):
      self.items.insert(0,item)  #insert at begining
   
   def dequeue(self):
       self.items.pop()    # removal from end
   
   def size(self):
       return len(self.items)

myQueue = queue()
print myQueue.isEmpty()
myQueue.enqueue('hi')
myQueue.enqueue('govind')
myQueue.enqueue(7)

print myQueue.size()
print myQueue.items
myQueue.dequeue()
print myQueue.items