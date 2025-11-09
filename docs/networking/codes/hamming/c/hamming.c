#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
void calc_redundancy(char *data_new2,int m,int r);
char red[10];
int arr[30];
void main()
{
	char data[50],dred[80],dnew[80],derror[80],new_red_bit[15],temp[80];
	int m,r,r1,i,j=0,k=0,error,pos=0;
	printf("Enter the message: ");
	gets(data);
	m=strlen(data);
	for(r1=1;r1<m;r1++)
	{
		if (m+r1+1<=pow(2,r1))
		{
			r=r1;
			break;
		}
	}
	printf("Number of redundant bit = %d",r);
	for(i=0;i<r;i++)
		arr[j++]=pow(2,i);
	j=r-1;
	for(i=r+m;i>0;i--)
	{
		if(i==arr[j])
			{
				dred[r+m-i]='x';
				j--;
			}			
		else
			dred[r+m-i]=data[k++];
	}
	dred[r+m]='\0';
	printf("\n\nData with redundant : %s",dred);
	strcpy(dnew,dred);
	strrev(dnew);
	calc_redundancy(dnew,m,r);
	printf("\nRedundant bits are----> %s",red);
	printf("\n\nData with redundant : %s",dnew);
	printf("\nEnter the error position from MSB(If no error enter 0) = ");
	scanf("%d",&error);
	strcpy(derror,dnew);
	strrev(derror);
	if(error!=0)
	{
		if(derror[error-1]=='0')
			derror[error-1]='1';
		else
			derror[error-1]='0';
	}
	strcpy(temp,derror);
	printf("\nReceived data with error: %s",strrev(temp));
	calc_redundancy(derror,m,r);
	k=0;
	strcpy(new_red_bit,red);
	for(i=0;i<r;i++)
	{
		pos+=pow(2,i)*(new_red_bit[r-i-1]-'0');
	}
	printf("\nNew Redundant bits are----> %s\n",new_red_bit);
	printf("\nError position = %d",pos);
	if(derror[pos-1]=='0')
		derror[pos-1]='1';
	else
		derror[pos-1]='0';
	printf("\nReceived data after correction: %s",strrev(derror));
	getch();
}
void calc_redundancy(char *data_new2,int m,int r)
{
	int i,p,q,j,k,count_1,b,h=0;
	char eqn[80];
	for(b=0;b<r;b++)
	{
		p=b+1;
		q=pow(2,p);	
		eqn[0]='\0';
		k=0;
		for(i=arr[b]-1;i<m+r;i+=q)
		{
			if(i+arr[b]<=m+r)
			{
				for(j=i;j<i+arr[b];j++)
				eqn[k++]=data_new2[j];
			}
			else
			{
				for(j=i;j<m+r;j++)
				eqn[k++]=data_new2[j];
			}
		}
		eqn[k]='\0';
		count_1=0;
		for(i=0;i<strlen(eqn);i++)
		{
			if(eqn[i]=='1')
			count_1++;
		}
		if (count_1%2==0)
		{
			data_new2[(int)(q/2)-1]='0';
			red[h++]='0';
		}	
		else
		{
			data_new2[(int)(q/2)-1]='1';
			red[h++]='1';
		}
		red[h]='\0';
	}
	strrev(data_new2);
	strrev(red);
}
