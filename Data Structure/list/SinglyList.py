class Node:
    #constructor
    def __init__(self,info,link=None):
        self.info = info
        self.link = link
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self,info):
        #create new node at start
        newNode = Node(info)
        if self.head!= None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode
    def insert_at_end(self,info):
        #create new node at start
        newNode = Node(info)
        if self.head!= None:
            current = self.head
            while current.link !=None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode
    def delete_node(self,ele):
        if self.head == None:
            print("List Empty")
            return
        if self.head == ele:
            temp = self.head
            self.head = temp.link
            temp=None
            return
        current = self.head
        while current.link !=None:
            if current.link.info == ele:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link
        print("Elemnt Not Found in List")
    def display(self):
        current = self.head
        while current!= None:
            print(current.info)
            current = current.link




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
# Singly Linked list	O(N)	O(N)	O(1)	O(1)