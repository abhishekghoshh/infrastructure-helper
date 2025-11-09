#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int check(int bit,int pos,int length)
{
	int arr[length];
	for(int i=0;i<length;i++)
	{
		arr[i]=bit%2;
		bit=bit/2;
	}
	if(arr[pos]==1)
	return 1;
	
	return 0;
}


int main()
{
	string m;
	cout<<"The bit stream is ";
	cin>>m;
	cout<<endl;
	int length=m.length(),r=0;
	
	while(1)
	{
		if(pow(2,r)>=length+r+1)
		break;
		r++;
	}
	cout<<"The no of redundent bit is "<<r<<endl;
	int size=pow(2,r);
	
	int message[size],i=0,parity[r][size/2],message_copy[size],error[r];
	
	while(i<size)
	{
		message[i]=message_copy[i]=0;
		i++;
	}
	
	int k=0,j;
	
	for(i=0;i<r;i++)
	{
		for(j=0;j<size;j++)
		{
			if(check(j,i,r)==1)
			{
				parity[i][k]=j;
				k++;	
			}
		}
		k=0;
	}
	
		
	j=length,k=0;
	int bit;
	
	for(i=1;i<length+r+1;i++)
	{
		if(i==pow(2,k))
		{
			k++;
			continue;
		}
		else
		{
			j--;
			message[i] = m[j]-'0';
			//cout<<i<<"->"<<message[i]<<endl;
		}
	}
	cout<<endl;
	
	/*for(i=length+r;i>=1;i--)
	{
		cout<<message[i];
	}	
	cout<<endl;*/
	
	int sum=0,pos;	
	for(i=0;i<r;i++)
	{
		for(j=0;j<size/2;j++)
		{
			sum=sum+message[parity[i][j]];
		}
		pos=pow(2,i);
		if(sum%2==1)
		message[pos]=1;
		sum=0;
	}
	cout<<"Transmitting bit stream is ";
	for(i=length+r;i>=1;i--)
	{
		cout<<message[i];
		message_copy[i]=message[i];
	}	
	cout<<endl;
	
	pos;
	cout<<endl<<"The bit which introduced error is ";
	cin>>pos;
	message_copy[pos]=(message_copy[pos]+1)%2;
	
	cout<<endl<<"Now the receiveing bit stream is ";
	for(i=length+r;i>=1;i--)
	{
		cout<<message_copy[i];
	}	
	cout<<endl;
	cout<<endl<<"Now again at the receiver side the parity bits will be calculated"<<endl;
	sum=0;
	int x;
	for(i=0;i<r;i++)
	{
		for(j=0;j<size/2;j++)
		{
			sum=sum+message_copy[parity[i][j]];
		}
		error[i]=sum%2;
		
		sum=0;
		
	}
	cout<<endl<<"So in the receiver side error bit will be calculated and the bit position will be ";
	for(i=r-1;i>=0;i--)
	cout<<error[i];
	
	
	return 0;
	
}
