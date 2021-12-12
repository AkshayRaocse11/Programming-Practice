class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack ==  []
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]   
s= Stack()     
while True:
    print("push")
    print("pop")
    print("peek")
    do = input("What operation u want to perform")
    if do == "push":
        ele = int(input("Insert Element into Stack "))
        s.push(ele)
    elif do == 'pop' :
        ele = s.pop()
        if ele == -1:
            print("Stack Empty")
        else:
            print("Deleted element from the stack is ={10}".format(ele))
    elif do == 'peek':
        ele = s.peek()
        if ele == -1:
            print("Stack Empty") 
        else:
            print("Top of the element from the stack is ={}".format(ele)) 
    else:
        break     

# Data structure	Access	Search	Insertion	Deletion
# Stack	O(N)	O(N)	O(1)	O(1)        

