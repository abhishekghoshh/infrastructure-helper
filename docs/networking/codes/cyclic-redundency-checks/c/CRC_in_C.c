#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<malloc.h>
char *calc_crc(char temp_crc[]);
char div[16],data[100],dcrc[120],*crcval,new_dcrc[120],new_crc[15],crc[15];
int len,ldiv;
void main()
{
	char temp_crc[15];
	int i,err;
	printf("Enter the divisor = ");
	gets(div);
	printf("Enter the message = ");
	gets(data);
	ldiv=strlen(div);
	len=strlen(data);
	for(i=0;i<ldiv-1;i++)
		temp_crc[i]='0';
	temp_crc[ldiv-1]='\0';
	crcval=calc_crc(temp_crc);
	strcpy(crc,crcval);
	strcpy(new_dcrc,data);
	strcat(new_dcrc,crc);
	printf("Data with crc = %s\n",new_dcrc);
	printf("Enter the error bit (If no error enter 0) = ");
	scanf("%d",&err);
	if(err!=0)
	{
		if(data[err-1]=='0')
			data[err-1]='1';
		else
			data[err-1]='0';
	}
	crcval=calc_crc(crc);
	if(!strcmp(crcval,temp_crc))
		printf("CRC is zero , so there is no error");
	else
		printf("CRC is non zero , so there is an error");
	getch();
}
char *calc_crc(char temp_crc[])
{
	char rem[15],temp[15];
	int i,n=len+ldiv-1,lrem,j,start,k,extra;
	strcpy(dcrc,data);
	strcat(dcrc,temp_crc);
	printf("data = %s\n",dcrc);
	for(i=0;i<ldiv-1;i++)
		rem[i]=data[i];
	rem[i]='\0';
	for(i=ldiv-1;i<n;i++)
	{
		lrem=strlen(rem);
		for(j=0;j<lrem;j++)
			if(rem[j]=='1')
				break;
		start=0;
		for(k=j;k<lrem;k++)
			rem[start++]=rem[k];
		rem[start++]=dcrc[i];
		rem[start]='\0';
		if(strlen(rem)==ldiv)
		{
			for(k=0;k<ldiv;k++)
			{
				if(rem[k]==div[k])
					rem[k]='0';
				else
					rem[k]='1';
			}
		}
	}
	extra=ldiv-1-strlen(rem);
	for(j=0;j<extra;j++)
		temp[j]='0';
	temp[j]='\0';
	strcat(temp,rem);
	printf("CRC = %s\n",temp);
	return temp;
}
