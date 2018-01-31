class Node(object):
    def __init__(self,data,nextNode):
        self.data = data 
        self.nextNode = nextNode
    
    def __repr__(self):
        return repr(self.data)


class singleLinkedlist(object):
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes =[]
        current = self.head
        while current:
           nodes.append(repr(current))
           current = current.nextNode
        return '[' + ' ,' .join(nodes) + ']'
    
    def addAtStart(self,data):
        self.head = Node(data,self.head)

    def addAtLast(self,data):
         if not self.head:
            self.head = Node(data,self.head)
            return
         temp = self.head
         while temp.nextNode:
             temp = temp.nextNode
         temp.nextNode = Node(data,None)
    
    def remove(self,data):
         if not self.head:
             return
         current = self.head
         if(self.head.data==data):
             self.head = self.head.nextNode
             return
         prev = None
         while current and current.data!=data:
             prev = current
             current = current.nextNode
         if current.nextNode == None:
             prev.nextNode =None
             return
         else:
            prev.nextNode = current.nextNode
            return
    
    def reverse(self):
       prev = None
       current = self.head
       temp =None
       while current:
           temp = current.nextNode
           current.nextNode=prev
           prev = current
           current = temp
           
       self.head = prev
    
myList = singleLinkedlist()
myList.addAtLast(2)
myList.addAtLast(5)
myList.addAtLast(9)
myList.addAtLast(8)
print myList
myList.reverse()
print myList
       
       