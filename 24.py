hastun=int(input())
vj=list(map(int,input().split()[:hastun]))
vj.sort()
for f in vj:
	print(f,end=" ")
