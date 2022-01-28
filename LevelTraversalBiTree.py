class Node:
    def __init__(self,data): 
        self.root=data
        self.left=None
        self.right=None
        
def levelordertraversal(root):
    if(root==None):
        return
    queue=[]
    queue.append(root)
    
    while(len(queue)>0):
        count=len(queue)
        while(count >0):
            temp= queue.pop(0)
            print(temp.root, end=' ')
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
            count=count-1
        print("")
    
if __name__ == '__main__':
     
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25) 
    
    levelordertraversal(root)  