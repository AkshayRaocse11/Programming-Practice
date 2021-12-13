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

    def search(self,root,ele):
        if root is None or root.data == ele:
            return root
        if root.data > ele:
            return self.search(root.left,ele)
        return self.search(root.right,ele)

    def min_ele(self,root):
        current = root
        while current.left is not None:
            current = current.left
        return current.data
    def max_ele(self,root):
        current = root
        while current.right is not None:
            current = current.right
        return current.data        




        
    


root = None
b= BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)

b.inorder(root)

search_ele = b.search(root,30)

if search_ele == None:
    print("No element Found")
else:
    print("Elemnt found in the bst={}".format(search_ele.data))

min_ele = b.min_ele(root)
max_ele = b.max_ele(root)
if min_ele == None:
    print("No element Found")
else:
    print("Elemnt found Min is  the bst={}".format(min_ele))
    print("Elemnt found Max is  the bst={}".format(max_ele))


