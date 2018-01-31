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
   def size(self):
       return len(self.items)

def HasOpening(char,mystack):
    
    if char == ')' and mystack.peek()=='(':
       return True 
    if char == '}' and mystack.peek()=='{':
       return True 
    if char == ']' and mystack.peek()=='[':
       return True
    else:
        return False 

def isOpening(char):
   if char== '{' or char=='(' or char=='[':
       return True
   else:
      return False

def isClosing(char):
   if char== '}' or char==')' or char==']':
       return True
   else:
      return False

def balanced(string):
   mystack = stack()
   if len(string)%2 !=0 :
      return False
   for char in string:
      if isOpening(char):
          mystack.push(char)
         
          
      elif isClosing(char) and mystack.isEmpty():
          return False
      elif isClosing(char) and not HasOpening(char,mystack):
          return False
      elif isClosing(char) and HasOpening(char,mystack) :
          mystack.pop()
   if mystack.isEmpty():
        return True

print balanced('[](){([[[]]])}')
    
          
         