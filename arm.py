j,b=map(int,input().split())

for i in range(j+1,b):
  fin=i
  fd=0
  while (i>0):
    dt=i%10
    fd=fd+(dt**3)
    i=i//10
    if(fd==fin):
      print(fd,end=" ")
