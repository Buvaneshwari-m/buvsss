m=int(input())
b=0
j=m
while j>0:
   digit=j%10
   b+=digit**3
   j//=10
if m==b:
   print("yes")
else:
   print("no")
