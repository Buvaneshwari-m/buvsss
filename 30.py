has,a=list(map(int,input().split()))
fas,ro=list(map(int,input().split()))
t=int((has*60)+a)
o=int((fas*60)+ro)
y=abs(t-o)
ro=0
m=0
while(y>59):
  y=y-60
  ro+=1
k=y
print(ro,k)

