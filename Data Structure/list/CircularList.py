class Node:
    #constructor
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,info):
        #create new node at start
        newNode = Node(info)
        if self.head == None:
            self.head = newNode 
            self.head.next = self.head       
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            self.head = newNode
    def insert_at_end(self,info): 
        newNode = Node(info) 
        if self.head == None:
            self.head = newNode 
            self.head.next = self.head  
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
    def delete_node(self,ele):
        if self.head == None:
            print("nO ELEMENTS FOUND")
            return
        if self.head.info == ele:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head 
        while current.next!=self.head:
            if current.next.info == ele:
                temp = current.next
                current.next = temp.next
                temp =None
                return
            current = current.next
        print("Elemnt Not Found in List")
    def display(self):
        current = self.head
        while current.next!=self.head:
            print(current.info)
            current = current.next     
        print(current.info)      

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


