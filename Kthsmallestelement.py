class Solution:
    def kthsmallest(self,arr,l,r,k):
        arr.sort()
        return arr[k-1]
    
if __name__ == '__main__':
    import random
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        obj=Solution()
        print(obj.kthsmallest(arr,0,n-1,k))

