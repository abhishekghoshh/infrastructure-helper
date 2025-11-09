#include<iostream>
using namespace std;

void insert_bit(char* input_bit_array, int k,int length1)
{
	for(int i=length1-1;i>k;i--)
	{
		input_bit_array[i]=input_bit_array[i-1];
	}
	input_bit_array[k]='0';
	
}
void delete_bit(char* input_bit_array, int k,int length1)
{
	for(int i=k;i<length1;i++)
	{
		input_bit_array[i]=input_bit_array[i+1];
	}
	
}

int main()
{
	string flag="111110";
	string input_bit;
	cout<<"Enter your input bits"<<endl;
	cin>>input_bit;
	cout<<endl;
	
	
	int flag_array[]={'1','1','1','1'};
	int length=input_bit.length();
	int length1=length+length/4;
	char input_bit_array[length1],input_bit_array_copy1[length1],input_bit_array_copy2[length1];
	for(int i=0;i<length;i++)
	{
		input_bit_array[i]=input_bit[i];
		input_bit_array_copy1[i]=input_bit[i];
	}
	int match=0;
	for(int i=0;i<length1;i++)
	{
		if(input_bit_array[i]==flag_array[match])
		{
			match++;
			if(match==4)
			{
				//cout<<"match is found"<<endl;
				match=0;
				insert_bit(input_bit_array,i+1,length1);
			}
		}
		else
		{
			match=0;	
		}
	}
	cout<<"The stuffed bit is"<<endl;
	for(int i=0;i<length1;i++)
	{
		cout<<input_bit_array[i];
		input_bit_array_copy2[i]=input_bit_array[i];
	}
	cout<<endl;
	
	
	match=0;
	for(int i=0;i<length1;i++)
	{	
		if(input_bit_array[i]==flag_array[match])
		{
			match++;
			if(match==4)
			{
				//cout<<"match is found"<<endl;
				match=0;
				delete_bit(input_bit_array,i+1,length1);
			}
		}
		else
		{
			match=0;	
		}	
			
	}
	cout<<"The destuffed bit is"<<endl;
	for(int i=0;i<length1;i++)
	{
		cout<<input_bit_array[i];
	}
	cout<<endl;
	
	
	

	
		
	
	return 0;
}
