print("Enter the flag pattern")
flag=input().strip()
print("Enter the data")
data=input().strip()
stuffed_data=''
count=''
no_of_1=flag.count('1')
estimate='1'*(no_of_1-1)
for c in data:
	if c=='1':
		count+='1'
	else:
		count=''
	stuffed_data+=c
	if count==estimate:
		stuffed_data+='0'
		count=''
print("Stuffed data = ",stuffed_data)
print("Want to see the de-stuffed data? press 1 for Yes , 2 for No")
opt=int(input().strip())
if opt==1:
	destuffed=''
	i=0
	n=len(stuffed_data)
	count=''
	while i<n:
		if stuffed_data[i]=='1':
			count+='1'
		else:
			count=''
		destuffed+=stuffed_data[i]
		if count==estimate:
			count=''
			i+=1
		i+=1
	print("De-stuffed data = ",destuffed)
else:
	print("Exiting")