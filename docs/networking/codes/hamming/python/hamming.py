from math import log
def calc_reduntancy(data_new2,pow_2,m,r):
	redundant={}.fromkeys(pow_2,'x')
	for item in pow_2:
		p=int(log(item,2))+1
		q=2**p
		#print(item,q)
		eqn=''
		for i in range(item-1,m+r,q):
			#print(i+1,i+item)
			try:
				eqn+=data_new2[i:i+item]
			except:
				eqn+=data_new2[i:m+r]
		count_1=eqn.count('1')
		#print(eqn[::-1])
		if count_1%2==0:
			redundant[item]='0'
		else:
			redundant[item]='1'
	return redundant
print("Enter the message")
data=input().strip()
m=len(data)
for r1 in range(1,m):
	if m+r1+1<=2**r1:
		r=r1
		break
print('Number of redundant bit = ',r)
data_new=''
pow_2=[]
for i in range(r):
	pow_2.append(2**i)
redundant={}.fromkeys(pow_2,'x')
j=0
for i in range(r+m,0,-1):
	if i in pow_2:
		data_new+='x'
	else:
		data_new+=data[j]
		j+=1
#print(data_new)
#print(redundant)
data_new2=data_new[::-1]
redundant=calc_reduntancy(data_new2,pow_2,m,r)
data_trans=''
j=0
for i in range(r+m,0,-1):
	if i in pow_2:
		data_trans+=redundant[i]
	else:
		data_trans+=data[j]
		j+=1
print("Redundant bits are---->")
for item in pow_2:
	print('c['+str(item)+'] = ',redundant[item])
print('Transmitting data = ',data_trans)
print("Enter the error position (If no error enter 0)")
error=int(input().strip())
data_trans2=data_trans[::-1]
data_error=''+data_trans2
if error!=0:
	if data_trans2[error-1]=='1':
		error_bit='0'
	else:
		error_bit='1'
	data_error=data_trans2[:error-1]+error_bit+data_trans2[error:]
new_redundant=calc_reduntancy(data_error,pow_2,m,r)
new_red_bit=''
for item in pow_2:
	new_red_bit+=new_redundant[item]
new_red_bit=new_red_bit[::-1]
print("New Redundant bits are----> ",new_red_bit)
pos=int(new_red_bit,2)
print("Error position = ",pos)