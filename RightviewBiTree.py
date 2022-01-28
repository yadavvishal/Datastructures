class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
def RightView(root,level,max_level):
    if(root!=None):
        if(max_level[0]<level):
            print(root.data)
            max_level[0]=level
            
        RightView(root.right,level+1,max_level)
        RightView(root.left,level+1,max_level)
    
if __name__ == '__main__':      
        
    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)     
    max_level=[0]
    print("Rightview of Binary tree are")
    RightView(root,1,max_level)