print("Ënter the IP address  ")
ip=input().strip().split('.')
k=int(ip[0])
if k==0 or k==127 or k==255:
	print("IP address is reserved")
elif 1<=k<=126:
	print("IP address is of Class A")
elif k<=191:
	print("IP address is of Class B")
elif k<=223:
	print("IP address is of Class C")
elif k<=239:
	print("IP address is of Class D")
elif k<=254:
	print("IP address is of Class E")
else:
	print("Invalid IP address")