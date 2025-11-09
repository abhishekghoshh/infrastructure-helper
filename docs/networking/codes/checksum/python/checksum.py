from math import ceil
print("Ënter the message")
mssg=input().strip()
print("Enter slice length")
sl=int(input().strip())
def check_sum_calc(mssg,cs,m):
	n=len(mssg)
	slice_num=ceil(n/m)
	slices=[]
	cs=int(cs,2)
	extra=m-n%m
	mssg+=('0'*extra)
	for i in range(0,(slice_num-1)*m+1,m):
	    slices.append(mssg[i:i+m])
	print("Slices are - ")
	arr=[]
	for item in slices:
		print(item)
		arr.append(int(item,2))
	arr.append(cs)
	check_sum=bin(sum(arr))[2:]
	if len(check_sum)>4:
		extra=len(check_sum)-m
		check_sum=check_sum[extra:]
	inv_cs=''
	for c in check_sum:
		if c=='1':
			inv_cs+='0'
		else:
			inv_cs+='1'
	return (check_sum,inv_cs)
check_sum,inv_cs=check_sum_calc(mssg,'0',sl)
print("Check sum before inversion =",check_sum)
print("Check sum after inversion =",inv_cs)
print("Transmitted message = ",mssg+inv_cs)   
check_sum_new,inv_cs_new=check_sum_calc(mssg,inv_cs,sl)
print("New check sum =",inv_cs_new,"So there is no error")
