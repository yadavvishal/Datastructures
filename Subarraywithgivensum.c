#include<stdio.h>
int main()
{
    int i,j,k,a[10],n,sum=0,target;
    printf("Enter the number of input:");
    scanf("%d",&n);
    printf("Enter the target:");
    scanf("%d",&target);
    printf("Enter the numbers:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);

    }printf("Subarray with given sum are:");
    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
            for(k=i;k<=j;k++)
            {
                sum=sum+a[k];
            }
            if(sum==target)
            {
                for(k=i;k<=j;k++)
                {
                    printf("%d ",a[k]);
                }
                printf("\n");
            }sum=0;


        }
    }
    return 0;
}

