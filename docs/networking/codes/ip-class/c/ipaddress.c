#include<stdio.h>
#include<string.h>
#include<math.h>

void main()
{
    char ip_ad[20],s[4];
    int i,j=0,n,ip;
    printf("Enter IP Address : ");
    gets(ip_ad);
    for(i=0;i<3;i++)
    {
    	s[j++]=ip_ad[i];
    	if(ip_ad[i+1]=='.')
    		break;
	}
	s[j]='\0';
	n=strlen(s);
	for(i=n-1;i>=0;i--)
		ip+=(pow(10,n-i-1)*(s[i]-'0'));
	if(ip==0 || ip==127 || ip==255)
		printf("\nIP Address is reserved.");
    else if(ip<=126)
        printf("\nClass A Ip Address.");
    else if(ip<=191)
        printf("\nClass B Ip Address.");
    else if(ip<=223)
        printf("\nClass C Ip Address.");
    else if(ip<=239)
        printf("\nClass D Ip Address.");
    else if(ip<=255)
        printf("\nClass E Ip Address.");
    else
    	printf("\nInvalid IP Address.\n");
    getch();
}
