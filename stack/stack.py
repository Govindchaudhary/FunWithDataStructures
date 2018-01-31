class stack:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return self.items==[]

   def push(self,item):
      self.items.append(item)    # add item to the last

   def pop(self):
      self.items.pop()  # remove item from last

   def peek(self):
      return self.items[len(self.items)-1]

mystack = stack()
print mystack.isEmpty()
mystack.push('hi')
mystack.push('govind')
mystack.push(7)
print mystack.items
mystack.pop()
print mystack.items
print mystack.peek()


    
       