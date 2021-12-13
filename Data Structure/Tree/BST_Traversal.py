
#binary search tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def buildBst(self,root,ele):
        if root == None:
           return Node(ele) 
        if ele < root.data:
            root.left = self.buildBst(root.left,ele)
        else:
            root.right = self.buildBst(root.right,ele)
        return root

    def inorder(self,root):
        if root == None:
            return "Empty Tree"
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def iterativeInOrder(self,root):
        current = root
        stack =[]             
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                break
    
    def preorder(self,root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def iterativePreOrder(self,root):
        if root is None:
            return
        stack =[]
        stack.append(root)
        while stack:
            current = stack.pop()
            print(current.data)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)    
                
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)   
        print(root.data)      

    def iterPostOrder1(self,root):
        if root is None:
            return
        recursiveStack, result = [] ,[]
        recursiveStack.append(root)
        while recursiveStack:
            current = recursiveStack.pop()
            result.append(current)
            if current.left:
                recursiveStack.append(current.left)
            if current.right:
                recursiveStack.append(current.right)     
        while result:
            current = result.pop()           
            print(current.data)
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        prev = None
        stack.append(root)
        while stack:
            current = stack[-1]
            if prev == None or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    result.append(current.data)
                    stack.pop()
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
            else:
                result.append(current.data)
                stack.pop()
 
            prev = current
        return result

            


    




        
    


root = None
b= BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)

b.inorder(root)
print("***** inorder")
b.iterativeInOrder(root)
print("***** iterativeInOrder")
b.preorder(root)
print("***** preorder")
b.iterativePreOrder(root)
print("***** iterativePreOrder")
b.postorder(root)
print("***** postorder")
b.iterPostOrder1(root)
print("***** iterPostOrder1")
b.postorderTraversal(root)
print("***** postorderTraversal")

# recursive and iterative tc - O(n) and sc o(h) 0(n)
