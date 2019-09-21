#first define the node (SLNode) class
class SLNode:
  def __init__(self,value):
    self.value = value
    self.next = None #each new node's next is null until we sepcificy where it points


#create SList class
class SList:
  def __init__(self):
    self.head = None
    self.tail = None #each new list is empty (contain 0 nodes) until we add them to the list

  
list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')