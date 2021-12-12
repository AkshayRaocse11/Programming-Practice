# Stack LIFO QUEUE FIFO
class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    
    def Enqueue(self,ele):
        temp =Node(ele)
        if self.rear == None:
            self.rear = self.front = temp
        self.rear.next = temp
        self.rear = temp
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is EMpty")
            return
        else:
            temp = self.front
            self.front = temp.next
            if self.front == None:
                self.rear = None
    def Display(self):
        p = self.front
        while p!=None:
            print(p.info)
            p = p.next 

            
Q = Queue()
Q.Enqueue(10)
Q.Enqueue(20)
Q.Enqueue(30)
Q.Enqueue(40)
Q.Enqueue(50)
Q.Enqueue(60)
Q.Dequeue()
Q.Display()


        
# TC O(1) FOR ENQUEUE AND DEQUEUE