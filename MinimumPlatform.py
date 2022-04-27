class Solution:    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i=1
        j=0
        count =1
        while i<n:
            if(arr[i]<=dep[j]):
                count+=1
            else:
                j+=1
            i+=1
        return count

import atexit
import io
import sys

if __name__== '__main__':
    t=int(input())
    for i in range(0,t):
        n=int(input())
        arr=list(map(int, input().strip().split()))
        dep=list(map(int, input().strip().split()))
        obj=Solution
        print(obj.minimumPlatform(n,arr,dep))
