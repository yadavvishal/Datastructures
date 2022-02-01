def removeDuplicates(llist):
    trav=llist
    
    while trav.next!=None:
        if trav.data==trav.next.data:
            trav.next=trav.next.next
        else:
            trav=trav.next
    
    return llist
