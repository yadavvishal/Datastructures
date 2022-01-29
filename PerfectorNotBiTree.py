class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def PerfectorNotBT(root):
    
    length=height(root)
    return length & (length+1)==0     ## Bitwise operator used 
                          
    
                                   ## Perfect Bianry has 2^h-1 nodes ,,   h is height of Bianry tree
def height(root):
    if root is None:
        return 0
    else:
        return 1+max(height(root.left),height(root.right))
    

if __name__ == '__main__':  

    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)
    
    PerfectorNotBT(root)
    if  PerfectorNotBT(root):
        print("This is perfect Tree")
    else:
        print("This is not perfect tree") 