# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublylinklist():
    def __init__(self):
        self.head=None
        
        
    def InserttoEnd(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
            return
        else:
            trav=self.head
            while trav.next is not None:
                trav=trav.next
                
            newnode=Node(data)
            trav.next=newnode
            newnode.prev=trav
        
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
            
            
root=doublylinklist()
root.InserttoEnd(10)
root.InserttoEnd(20)
root.InserttoEnd(30)
root.InserttoEnd(40)

root.display()


