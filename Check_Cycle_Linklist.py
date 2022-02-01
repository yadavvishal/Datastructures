def has_cycle(head):
    
    temp=trav=head
    while trav!=None and trav.next!=None:
        temp=temp.next
        trav=trav.next.next
        
        if(temp==trav):
            return 1
        
    return 0   
