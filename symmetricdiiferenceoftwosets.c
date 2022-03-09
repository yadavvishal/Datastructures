#include<stdio.h>
int main()
{
    int i,j,a[100],b[100],n1,n2,k=0;
    scanf("%d",&n1);
    for(i=0;i<n1;i++)
    {
        scanf("%d",&a[i]);
    }
    scanf("%d",&n2);
    for(i=0;i<n2;i++)
    {
        scanf("%d",&b[i]);
    }
    for(i=0;i<n1;i++)
    {
        for(j=0;j<n2;j++)
        {
            if(a[j]==a[i])
            {
                k=k+1;
                break;
            }
        }
        if(k==0)
        {
            printf("%d",a[i]);
        }
    }return 0;
}
