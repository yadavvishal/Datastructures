class Node:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
        
def CountleafNode(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return CountleafNode(root.left) + CountleafNode(root.right)
        
        
root=Node(15)
root.left=Node(10)
root.right=Node(20)
root.left.left=Node(8)
root.left.right=Node(12)
root.right.left=Node(16)
root.right.right=Node(25)
            
print("No.of Leaf nodes are:",CountleafNode(root))