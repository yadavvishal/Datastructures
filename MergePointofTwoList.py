def findMergeNode(head1, head2):
    trav=head1
    temp=head2
    while 1:
        if trav==temp:
            break
        trav=trav.next
        temp=temp.next
        if trav==None:
            trav=head2
        if temp==None:
            temp=head1
    return trav.data
