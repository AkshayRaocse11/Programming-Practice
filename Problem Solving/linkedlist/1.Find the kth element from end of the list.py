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
    def count(self):
        current = self.head
        count=0
        while current!= None:
            current = current.link
            count+=1
        return count
    def kth_node_brute_force(self,k):
        n= self.count()
        x=n-k
        temp=self.head
        count=0
        for i in range(x):
            temp=temp.link
            count+=1
        return temp.info
    def kth_node(self,k):
        start= self.head
        end=self.head
        for i in range(k):
            end = end.link
        while end is not None:
            start =start.link
            end = end.link
        return start.info
    def kthnode(llist,k):
        temp1=llist.head
        temp2=llist.head
        for i in range(k):
            temp1=temp1.link
        while temp1 is not None:
            temp1=temp1.link
            temp2=temp2.link
        return temp2.info        

        
    def display(self):
        current = self.head
        while current!= None:
            print(current.info)
            current = current.link        
    


    

    




LL = LinkedList()
LL.insert_at_start(10)
LL.insert_at_start(60)
LL.insert_at_end(40)
LL.insert_at_start(70)
LL.insert_at_start(80)
LL.insert_at_end(100)
print(LL.count())
print(LL.kth_node_brute_force(2))
print(LL.kth_node(2))
print(LL.kthnode(2))
# Data structure	Access	Search	Insertion	Deletion                      
# Singly Linked list	O(N)	O(N)	O(1)	O(1)