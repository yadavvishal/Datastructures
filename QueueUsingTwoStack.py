q=int(input())
stackpush=[]
stackdelete=[]
for i in range(q):
    t=list(input().split())
    
    # enqueue
    if t[0]=='1':
        stackpush.append(t[1])
    #dequeue   
    elif t[0]=='2':
        if not stackdelete:
            while stackpush:
                stackdelete.append(stackpush.pop())
                
        stackdelete.pop()
            
    else:
              
        if not stackdelete:
            while stackpush:
                stackdelete.append(stackpush.pop())
        print(stackdelete[-1])
