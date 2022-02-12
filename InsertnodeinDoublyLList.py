def sortedInsert(llist, data):
    ## create a newnode
     node = DoublyLinkedListNode(data)
     
     if llist==None:
        llist=node
        
     elif data<llist.data:
        node.next=llist
        llist.prev=node
        llist=node
     else:
        trav=llist
        
        while trav.next!=None and trav.data<data:
            trav=trav.next
        if trav.next==None and trav.data<data:
            trav.next=node
            node.prev=trav
        else:
            previous=trav.prev
            previous.next=node
            
            node.prev=previous
            node.next=trav
            trav.prev=node
     return llist
