from numpy import delete

class Node:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
def deleteBinarytree(root):
    if root !=None:
        
        deleteBinarytree(root.left,)     # delete node in Postorderform
        
        deleteBinarytree(root.right)
        
        del root  #delete current node


if __name__ == '__main__':
    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)
    deleteBinarytree(root)
    root=None
    print("The tree is finally deleted:")


