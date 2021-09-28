#include<stdio.h>
int main()
{
	int i,a[100],n;
	printf("Enter the number of input:");
	scanf("%d",&n);
	printf("Enter the numbers:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);	
	}
	int sum=0;
	int leftsum=0;
	for(i=0;i<n;i++)
	{
		sum+=a[i];
	}
	for(i=0;i<n;i++)
	{
		sum=sum-a[i];
		if(sum==leftsum)
		{
			printf("Index is:%d\n",i);	
		}
		leftsum=leftsum+a[i];
	}
	return 0;
		
}

