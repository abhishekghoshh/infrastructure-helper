#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
void check_sum(char *csum);
char data[50],cs[40];
int n,m;
void main()
{
	char s[50];
	int error,i,sum=0;
	printf("Enter the message: ");
	gets(data);
	m=strlen(data);
	printf("Enter slice length: ");
	scanf("%d",&n);
	check_sum("0");
	printf("\nCheck sum = %s",cs);
	printf("\nEnter the error position from MSB(If no error enter 0) = ");
	scanf("%d",&error);
	if(error!=0)
	{
		if(data[error-1]=='0')
			data[error-1]='1';
		else
			data[error-1]='0';
	}
	check_sum(cs);
	printf("\nCheck sum = %s",cs);
	for(i=0;i<strlen(cs);i++)
	sum+=pow(2,strlen(cs)-1-i)*(cs[i]-'0');
	if(sum==0)
	printf("\nThere is no error.");
	else
	printf("\nThere is an error.");
	getch();
}
void check_sum(char *csum)
{
	int i,extra,arr[20],j,temp,k=m,sum=0,count=0,q;
	for(i=0;i<strlen(csum);i++)
	sum+=pow(2,strlen(csum)-1-i)*(csum[i]-'0');
	extra=n-m%n;
	for(i=1;i<=extra;i++)
	data[k++]='0';
	for(i=0;i<m+extra;i+=n)
	{
		temp=0;
		for(j=i;j<i+n;j++)
		temp+=(pow(2,n-1-j%n)*(data[j]-'0'));
		sum+=temp;
	}
	for(q=sum;q!=0 && count<n;q/=2)
	cs[count++]=((q+1)%2)+'0';
	cs[count]='\0';
	strrev(cs);
}
