#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char flag[10],db[50],stb[70],dstb[50];
	int count=0,i,l,cf=0;
	printf("Enter the flag: ");
	gets(flag);
	for(i=0;i<strlen(flag);i++)
	{
		if(flag[i]=='1')
		cf++;
	}
	printf("\n\nEnter the data bit for transmission: ");
	gets(db);
	l=strlen(db);
	int sbit=0;
	for(i=0;i<l;i++)
	{
		if(db[i]=='1')
			count++;
		else
			count=0;
		stb[i+sbit]=db[i];
		if(count==cf-1)
		{
			stb[i+sbit+1]='0';
			count=0;
			sbit++;
		}		
	}
	stb[i+sbit]='\0';
	printf("\nStuffed transmitted data: %s\n",stb);
	fflush(stdin);
	l=strlen(stb);
	sbit=0,count=0;
	for(i=0;i<l;i++)
	{
		if(stb[i]=='1')
			count++;
		else
			count=0;
		dstb[i-sbit]=stb[i];
		if(count==cf-1)
		{
			i++;
			count=0;
			sbit++;
		}		
	}
	dstb[i-sbit]='\0';
	printf("\n\nDe-Stuffed received data: %s",dstb);
	getch();
}
