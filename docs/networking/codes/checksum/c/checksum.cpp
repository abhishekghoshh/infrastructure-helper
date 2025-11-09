#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int decimal(int* arr,int div)
{
	int sum=0,addr=4*div;
	sum=arr[addr]+arr[addr+1]*2+arr[addr+2]*4+arr[addr+3]*8;
	return sum;
}
void binary(int *arr,int sum)
{
	for(int i=0;i<8;i++)
	{
		arr[i]=sum%2;
		sum=sum/2;
	}
}
void addCarry(int* arr)
{
	int sum,carry;
	while(arr[4]!=0)
	{
		sum=0,carry=0;
		for(int i=0;i<4;i++)
		{
			sum=arr[i]+arr[i+4]+carry;
			arr[i]=sum%2;
			carry=sum/2;
		}
		for(int i=4;i<8;i++)
		arr[i]=0;
		
		arr[4]=carry;	
	}
	
}
void complement(int* arr)
{
	for(int i=0;i<4;i++)
	{
		if(arr[i]==1)
		arr[i]=0;
		else
		arr[i]=1;
	}		
}
void show(int *arr)
{
	cout<<"Checksum is now  ";
	for(int i=7;i>=0;i--)
	cout<<arr[i];
	cout<<endl;
}

int main()
{
	string data;
	cout<<"Enter your data and the length of the data should be multiple of four ";
	cin>>data;
	int length=data.length();
	cout<<"the length is "<<length<<" bit"<<endl;
	int div=length/4;
	int data_array[length],sum[9],copy_data[length],copy_sum[9],add;
	
	for(int i=0;i<length;i++)
	{
		data_array[i]=copy_data[i]=data[length-i-1]-'0';
	}
	for(int i=8;i>=0;i--)
	{
		sum[i]=copy_sum[i]=0;
	}
	
	//checksum start
	add=0;
	for(int i=0;i<div;i++)
	{
		add=add+decimal(data_array,i);	
	}
	binary(sum,add);
	show(sum);
	addCarry(sum);
	show(sum);
	complement(sum);
	cout<<"This is final checksum"<<endl;
	show(sum);
	//checksum end
	
	cout<<endl<<"The error bit postion is ";
	int pos;
	cin>>pos;
	cout<<endl;
	copy_data[pos]=(copy_data[pos]+1)%2;
	
	cout<<"The actual data is ";
	for(int i=length-1;i>=0;i--)
	cout<<data_array[i];
	cout<<endl;	
	
	cout<<"Transmitted data is ";
	for(int i=length-1;i>=0;i--)
	cout<<copy_data[i];
	cout<<endl;	
	
	//checksum start
	add=0;
	for(int i=0;i<div;i++)
	{
		add=add+decimal(copy_data,i);	
	}
	binary(copy_sum,add);
	show(copy_sum);
	addCarry(copy_sum);
	show(copy_sum);
	complement(copy_sum);
	cout<<"This is final checksum"<<endl;
	show(copy_sum);
	//checksum end	

	
	
	return 0;
}
