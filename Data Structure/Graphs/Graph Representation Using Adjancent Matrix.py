class Graph:
    def __init__(self,size):
        self.adjancent_matrix = []
        for i in range(size):
            self.adjancent_matrix.append([0 for j in range(size)])
    
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Both vertices are same")
            return 
        self.adjancent_matrix[v1][v2]=1
        self.adjancent_matrix[v2][v1]=1

    def remove_edge(self,v1,v2):
        if self.adjancent_matrix[v1][v2] ==0:
            return print("There is no edge between them")
        self.adjancent_matrix[v1][v2]=0
        self.adjancent_matrix[v2][v1]=0  

    def print_matrix(self)  :
        for row in self.adjancent_matrix:
            print(row)

g= Graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,1)
g.add_edge(3,1)
g.print_matrix()
print("********")
g.remove_edge(2,3)
g.print_matrix()
        
#O(n^2)

