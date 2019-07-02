m=int(input())
b=0
j=m
while j>0
   digit=j%5
   b+=digit**2
   j//=5
if m==b:
   print("yes")
else:
   print("no")
