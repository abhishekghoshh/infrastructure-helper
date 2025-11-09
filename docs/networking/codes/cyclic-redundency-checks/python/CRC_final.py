def xor(a,b):
	result=''
	n=len(a)
	for i in range(n):
		if a[i]==b[i]:
			result+='0'
		else:
			result+='1'
	return result
def crc_calc(m,crc,div,len_div):
	mssg=m+crc
	n=len(mssg)
	reminder=mssg[:len_div-1]
	for i in range(len_div-1,n):
		reminder=reminder.lstrip('0')
		reminder+=mssg[i]
		if len(reminder)==len_div:
			reminder=xor(reminder,div)
	crc=reminder.lstrip('0')
	return crc
def finalize(crc,l):
	k=l-len(crc)
	p='0'*k
	crc=p+crc
	return crc
print("Enter the message")
m=input().strip()
print("Enter the divisor")
div=input().strip()
len_div=len(div)
crc='0'*(len_div-1)
crc=crc_calc(m,crc,div,len_div)
crc=finalize(crc,len_div-1)
print('CRC = ',crc)
print("Message signal = ",m+crc)
print("Enter the error position (If no error enter 0)")
error=int(input().strip())
if error==0:
	error_m=m
else:
	if m[error-1]=='1':
		error_bit='0'
	else:
		error_bit='1'
	error_m=m[:error-1]+error_bit+m[error:]
crc=crc_calc(error_m,crc,div,len_div)
crc=finalize(crc,len_div-1)
print("New CRC = ",crc)
new=crc.strip('0')
if not new:
	print('No error')
else:
	print("CRC is non-zero...So there is an error")
