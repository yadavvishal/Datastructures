class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def SpiralTravBiTree(root):
    if(root==None):
        return
    stack1=[]  ## Empty stack for levels to be printed from right to left
    
    stack2=[]  ## Empty stack for levels to be printed from left to right

    stack1.append(root)
    
    while not len(stack1)==0 or not len(stack2)==0:  ## keep printing while any of the stacks has some nodes
        
        while not len(stack1)==0:
            
            ## Print nodes of current level from stack1 and append nodes of next level to stack2
            temp= stack1[-1]
            stack1.pop()
            print(temp.data, end=" ")
        
            ## Left is appended before right
            
            if (temp.right):
                stack2.append(temp.right)
            
            if (temp.left):
                stack2.append(temp.left)
    
        while not len(stack2) ==0:
            
            ## Print nodes of current level from stack2 and append nodes of next level to stack1
            temp=stack2[-1] 
            stack2.pop()
            print(temp.data, end =" ")  
            
            ## Letf is appended before right 
            
            if(temp.left):
                stack1.append(temp.left)
            if(temp.right):
                stack1.append(temp.right)
                
                    
    
    
if __name__ == '__main__':      
        
    root=Node(15)
    root.left=Node(10)
    root.right=Node(20)
    root.left.left=Node(8)
    root.left.right=Node(12)
    root.right.left=Node(16)
    root.right.right=Node(25)
    
    print("Spiral order traversal of binary trees are:")
    SpiralTravBiTree(root)