def dfs(start,visited,r,c,vtx):
	visited[start]=True
	r.append(start)
	for i in range(1,vtx+1):
		if c[start][i] and not visited[i]:
			visited,r=dfs(i,visited,r,c,vtx)
	return (visited,r)
print("Enter number vertex")
vtx=input().strip()
vtx=int(vtx)
n=20
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
            if temp[j]==99:
                temp[j]=0
	c.append([0]+temp)
visited=[False]*(vtx+1)
comp=1
visited,r=dfs(1,visited,[],c,vtx)
flag=False
for i in range(1,vtx+1):
	if not visited[i]:
		flag=True
		k=i
		break
if flag:
	print("The graph is disconnected")
	print("Vertices under component",comp,"---->",end="")
	r.sort()
	for v in r:
		print(chr(v+64),end=" ")
	for i in range(k,vtx+1):
		if not visited[i]:
			visited,r=dfs(i,visited,[],c,vtx)
			comp+=1
			print()
			print("Vertices under component",comp,"---->",end="")
			r.sort()
			for v in r:
				print(chr(v+64),end=" ")
else:
	print("The graph is connected")