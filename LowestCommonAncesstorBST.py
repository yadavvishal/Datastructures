class Node:
    
    ## Constructor to create a new node
    def __init__(self,data): 
        self.data=data
        self.left=None
        self.right=None
    ## recursion use
        
def lca(root,n1,n2):
    if(root==None):
        return None
    
    if(root.data>n1 and root.data>n2):
        return lca(root.left,n1,n2)
    
    if(root.data<n1 and root.data<n2):
        return lca(root.right,n1,n2)
    
    return root
    

        

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)    
 
n1=int(input())
n2=int(input())

output=lca(root,n1,n2)
print(output.data)