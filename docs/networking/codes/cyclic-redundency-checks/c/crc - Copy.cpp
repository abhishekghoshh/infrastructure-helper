#include<iostream>
#include<string>
#include<cmath>
using namespace std;

void division(int* div,string pol,int pol_length)
{
	int i=0;
	for(int j=pol_length-1;j>=0;j--)
	{
		div[j]=(div[j]+(pol[i]-'0'))%2;
		i++;
	}
	
}
void shift(int *div,int *crc,int i,int pol_length)
{
	for(int j=pol_length-1;j>=1;j--)
	{
		div[j]=div[j-1];
	}
	div[0]=crc[i-pol_length];
}
void show(int* arr,int length)
{
	for(int i=length-1;i>=0;i--)
	cout<<arr[i];
	cout<<endl;
}
void CRC(int *crc,int *div,string pol,int pol_length,int length)
{
	//CRC operation starts from here
	int j=0;
	for(int i=pol_length-1;i>=0;i--)
	{
		div[i]=crc[length-1-j];	j++;	
	}
	
	//cout<<endl<<"The starting div is";
	//show(div,pol_length);
	
	for(int i=length-1;i>=pol_length-1;i--)
	{
		//cout<<endl<<"i is "<<i<<endl;
		if(div[pol_length-1]==0)
		{
			if(i==pol_length-1)
			break;
			//cout<<endl<<"after shifting div is";
			shift(div,crc,i,pol_length);
			//show(div,pol_length);
			continue;
		}
		//cout<<endl<<"after dividing div is";
		division(div,pol,pol_length);
		//show(div,pol_length);
		if(i>pol_length-1)
		{
			//cout<<endl<<"after shifting div is";
			shift(div,crc,i,pol_length);
			//show(div,pol_length);
		}
	}
	cout<<endl<<"The reminder is ";
	show(div,pol_length);
	//CRC operation ends here
}
int main()
{
	string data,pol,crc_data;
	cout<<endl<<"Enter your data : ";
	cin>>data;
	crc_data=data;
	int data_length=data.length();
	cout<<endl<<"Enter your polynomial : ";
	cin>>pol;
	int pol_length=pol.length();
	for(int i=1;i<pol_length;i++)
	crc_data=crc_data+"0";

	int length=crc_data.length(),j;
	int crc[length],copy_crc[length],div[pol_length];
	
	for(int i=0;i<length;i++)
	{
		crc[i]=crc_data[length-i-1]-'0';
	}
	cout<<endl<<"CRC is now ";
	show(crc,length);
	
	//at firct we calculate the reminder to calculate the crc code
	CRC(div,crc,pol,pol_length,length);
	
	for(int i=pol_length-2;i>=0;i--)
	crc[i]=div[i];
	
	cout<<endl<<"The data with crc is ";
	show(crc,length);
	
	
	//again we calculate the reminder
	CRC(div,crc,pol,pol_length,length);
	
	
	//error starts from here
	int crc_copy[length],div_copy[pol_length];
	
	for(int i =length-1;i>=0;i--)
	crc_copy[i]=crc[i];
	
	cout<<endl<<"The error bit postion is ";
	int pos;
	cin>>pos;
	crc_copy[pos]=(crc_copy[pos]+1)%2;
	cout<<endl<<"The actual transmitted data is ";
	show(crc_copy,length);
	
	//reminder of the error transmitted data
	CRC(div_copy,crc_copy,pol,pol_length,length);
	
	return 0;
}
