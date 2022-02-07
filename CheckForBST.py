class Node:
     
    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def isBST(root,l=None,r=None):
    if (root==None):
        return True
        
    if(l!=None and root.data<=l.data):
        return False
        
    if(r!=None and root.data>=r.data):
        return False
        
    return isBST(root.left,l,root) and isBST(root.right,root,r)
        
        
        
if __name__ == '__main__':      
        
    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)


if (isBST(root,None,None)):
    print("This is Binary Search Tree")
else:
    print("Not Binary Search Tree")
