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
    def isPalindrome(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        current = self.head
        orignal = self.head
        while current.link !=None:
            arr.append(current.info)
            current = current.link
        arr.append(current.info)
        i=len(arr)-1
        while orignal.link !=None:

            if orignal.info != arr[i]:
                return False
            orignal = orignal.link
            i-=1
            
        return True        
    def display(self):
        current = self.head
        while current!= None:
            print(current.info)
            current = current.link




LL = LinkedList()
LL.insert_at_start(1)
LL.insert_at_end(2)
LL.insert_at_end(2)

print(LL.isPalindrome())
# Data structure	Access	Search	Insertion	Deletion                      
# Singly Linked list	O(N)	O(N)	O(1)	O(1)