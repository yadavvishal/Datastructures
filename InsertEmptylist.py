# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List       
class doublylinkedlist:
    def __init__(self):
        self.head=None
        
    # Insert Element to Empty list   
    def InserttoEmptyList(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("The list is not empty")
            
            
    def display(self):
        if self.head is None:
            print("The List is Empyt:")
            return
        else:
            trav=self.head
            while trav is not None:
                print("Element is:",trav.item)
                trav=trav.next
        print("\n")
            
# Create a root        
root=doublylinkedlist()
root.InserttoEmptyList(10)

root.display()