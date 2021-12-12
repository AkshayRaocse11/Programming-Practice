class Node:

    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class CircularQueue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def Enqueue(self,ele):
        temp = Node(ele)    

        if self.front == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.rear.next = self.front

    def Dequeue(self):
        if self.front == None:
            print("queue is empty")
            return -1
        temp = self.front
        if self.front == self.rear:
            self.front=self.rear=None
        else:
            self.front = temp.next
            self.rear.next = self.front
        return temp.info
    
    def Display(self):
        current = self.front
        while current.next != self.front:
            print(current.info)
            current = current.next
        print(current.info)

c = CircularQueue()
c.Enqueue(10)
c.Enqueue(210)
c.Enqueue(130)
c.Enqueue(104)
c.Enqueue(102)
c.Display()
print("*****")
c.Dequeue()
c.Dequeue()
val = c.Dequeue()
print("*****")
c.Display()

if val == -1:
    print("queue is empty")
else:
    print("Deleted element is = {}".format(val))

# tc O(1) 
        



    