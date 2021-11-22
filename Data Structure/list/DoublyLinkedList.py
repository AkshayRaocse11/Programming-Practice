class Node:
    def __init__(self,info,prev=None,next=None):
        self.prev = prev
        self.info = info
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next =   self.head
            self.head.prev = newNode
            self.head = newNode
    def insert_at_end(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current=current.next
            current.next = newNode
            newNode.prev = current
    def delete_node(self,ele):
        if self.head == None:
            print("List Empty")
            return
        if self.head.next == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp=None
                return
        temp = self.head.next
        while temp.next !=None:
            if temp.info == ele:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return
            temp = temp.next
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        



    def display(self):
        current = self.head
        while current!= None:
            print(current.info)
            current = current.next
LL = LinkedList()
LL.insert_at_start(10)
LL.insert_at_start(60)
LL.insert_at_end(10)
LL.insert_at_start(70)
LL.insert_at_start(80)
LL.insert_at_end(100)
LL.display()
print("delete start")
LL.delete_node(70)
LL.display()
print("delete end")
LL.delete_node(100)
LL.display()
print("delete Mid")
LL.delete_node(80)
LL.display()
print("delete None")
LL.delete_node(80)
LL.display()
# Data structure	Access	Search	Insertion	Deletion             
# Doubly Linked List  O(N)	O(N)	O(1)(if tail pointer)	O(1)            
        
