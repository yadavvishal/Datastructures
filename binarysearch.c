#include<stdio.h>
int main()
{	
	int data,a[10],n,i,l,r,mid,found=0;
	printf("enter the size of an array :");
	scanf("%d",&n);
	printf("enter the elements of an array:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("enter data to be search:");
	scanf("%d",&data);
	l=0;
	r=n-1;
	do
		{
			mid=(l+r)/2;
			if(data<a[mid])
				{
					r=mid-1;
					
					found=0;
				}
					
			else if(data>a[mid])
				{
					l=mid+1;
					found=0;
				}
			else if(a[mid]==data)
				{
					printf("%d found at location :%d\n",data,mid);
					found=1;
					break;
				}	
		}
	while(data!=a[mid] && l<=a[mid]);
		if(found==1)
		{
			printf("search is successful:\n");
		}
		else
		{
			printf("search is not successful\n:");
		}

		
	}
			






