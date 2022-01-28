class Node:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

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
            
print("The height of Binary tree:",height(root))