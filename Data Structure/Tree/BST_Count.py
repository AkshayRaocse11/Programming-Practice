
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

    def countNode(self,root):
        if root is None:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)

    def leafNodeCount(self,root):
        if root is None:
            return 0        
        if root.left is None and root.right is None :
            return 1 
        else:
            return self.countNode(root.left) + self.countNode(root.right)

    def iterativeCount(self,root):
        if root is None:
            return
        stack =[]
        stack.append(root)
        count = 0
        while stack:
            current = stack.pop()
            count = count + 1
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)    
        return count

    def maxDepth(self,root):
        if root is None:
            return 0
        else: 
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return 1 + max(ldepth,rdepth)
    def iterativeMaxDepth(self,root):
        stack = []           
        if root:
            stack.append((1,root))
        depth = 0
        while stack:
            current_depth , root = stack.pop()
            if root:
                depth = max(depth,current_depth)
                stack.append((current_depth+1,root.left))
                stack.append((current_depth+1,root.right))
        return depth

                

root = None
b= BST()
for ele in [10,5,25,2,7,30,11,11]:
    root = b.buildBst(root,ele)
count = b.countNode(root)
print(count)
Leafcount = b.leafNodeCount(root)
print(Leafcount)
iterativeCount = b.iterativeCount(root)
print(iterativeCount)
maxDepth = b.maxDepth(root)
print(maxDepth)
iterativeMaxDepth = b.iterativeMaxDepth(root)
print(iterativeMaxDepth)
# recursive and iterative tc - O(n) and sc o(h) 0(n)
