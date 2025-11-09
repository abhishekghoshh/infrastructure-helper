def shortest_path(c,n,s,m):
	v=[]
	d=[]
	for i in range(1,n+2):
		temp=[0]*(m+1)
		temp2=[0]*(m+1)
		v.append(temp)
		d.append(temp2)
	v[0][s]=0
	d[0][s]=s
	v[s][s]=0
	for i in range(1,m+1):
		if i!=s:
			v[0][i]=99
			d[0][i]=99
			v[1][i]=c[s][i]
			if c[s][i]==99:
				d[1][i]=99
			else:
				d[1][i]=s
		v[i][s]=0
		d[i][s]=s
	flag=True
	q=n-2
	#print(v)
	for t in range(2,n+1):
		#print(v)
		if flag:
			flag=False
			for i in range(1,m+1):
				if i==s:
					continue
				v[t][i]=99
				d[t][i]=d[t-1][i]
				for j in range(1,m+1):
					if j==i or c[j][i]==99 or v[t-1][j]==99:
						continue
					temp=v[t-1][j]+c[j][i]
					if temp<v[t][i]:
						v[t][i]=temp
						d[t][i]=j
				if v[t][i]!=v[t-1][i]:
					flag=True
		else:
                    q=t-2
                    break
	return (q,d,v)
print("Enter number vertex")
vtx=input().strip()
vtx=int(vtx)
n=20
print("Enter source")
s=input().strip()
s=ord(s)-64
print("Enter destination")
des=input().strip()
des=ord(des)-64
c=[]
print("Enter the cost matrix")
print("   ",end="")
for i in range(vtx):
	print(chr(i+65),end=" ")
print()
temp=[0]*(vtx+1)
c.append(temp)
for i in range(vtx):
	print(chr(i+65),end="  ")
	temp=list(map(int,input().strip().split()))
	for j in range(vtx):
            if temp[j]==0:
                temp[j]=99
	c.append([0]+temp)
p,d,v=shortest_path(c,n,s,vtx)
#print(s)
print("Length of shortest path between",chr(s+64)," and",chr(des+64),"is =",v[p][des],end="")
prev=des
#print(prev)
path=[0]*(n+1)
for i in range(p,0,-1):
	if d[i][prev]!=prev and d[i][prev]!=99 and d[i][prev]!=s:
		path[i]=d[i][prev]
		prev=d[i][prev]
		j=i
	else:
		i-=1
		j=i
		break
path[j+1]=s
print()
print("Shortest path is = ",end="")
for k in range(j+1,p+1):
	print(path[k],"--->",end="")
print(des)

