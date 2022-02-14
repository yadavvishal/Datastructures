from heapq import heapify

def heapify(array,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    
    if(l<n and array[i]<array[l]):
        largest=l
    if(r<n and array[i]<array[r]):
        largest=r
        
    if(largest!=i):
        
        ## Swaping two elements
        array[i],array[largest]=array[largest],array[i]
        heapify(array,n,largest)
        
    
def insert(array,newNum):
    size=len(array)
    if(size==0):
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2-1),-1,-1):
            heapify(array,size,i) 
            
def delete( array, num):
    size=len(array)
    i=0
    for i in range(0,size):
        if(num==array[i]):
            break
    ## swapping two elements
    array[i],array[size-1]=array[size-1],array[i]
    array.remove(num)
    
    for i in range((len(array)//2)-1,-1,-1):
        heapify(array,len(array),i)



array=[]
insert(array,3)
insert(array,4)
insert(array,9)
insert(array,5)
insert(array,2)

print("Max heap array:",str(array))
delete(array,4)
print("Max heap array:",str(array))


