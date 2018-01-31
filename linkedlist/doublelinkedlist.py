class Node(object):
    def __init__(self,data,nextNode,prevNode):
        self.data = data 
        self.nextNode = nextNode
        self.prevNode = prevNode
    
    def __repr__(self):
        return repr(self.data)


class doubleLinkedlist(object):
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
        new_head = Node(data,self.head,None)
        if self.head:
           self.head.prevNode = new_head
        self.head = new_head
           

    def addAtLast(self,data):
         if not self.head:
            self.head = Node(data,self.head,None)
            return
         temp = self.head
         while temp.nextNode:
             temp = temp.nextNode
         temp.nextNode = Node(data,None,temp)
    
    def remove(self,data):
         if not self.head:
             return
         current = self.head
         if(self.head.data==data):
             self.head = self.head.nextNode
             self.head.prevNode = None
             return
         prev = None
         next = self.head.nextNode
         while current and current.data!=data:
             prev = current
             current = current.nextNode
             next = next.nextNode
         if current.nextNode == None:
             prev.nextNode =None
             return
         else:
            prev.nextNode = current.nextNode
            next.prevNode = current.prevNode
            return
           
         
         
             
    
    
myList = doubleLinkedlist()
myList.addAtStart(2)
myList.addAtStart(4)
myList.addAtStart(6)
myList.addAtStart(9)

print myList
myList.remove(4)
print myList


       