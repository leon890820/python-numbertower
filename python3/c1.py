n=int(input())
import random
c1=0
c2=0
c3=0

r=0
x=[[random.randint(0,1) for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        c1+=x[i][j]
        c2+=x[j][i]
    if c1==n or c2==n :
        r=1
        break
    c1=0
    c2=0
for i in range(n):
    c1+=x[i][i]
    c2+=x[n-i-1][i]
    if c1==n or c2==n:
        r=1
for i in range(n):
    for j in range(n):
        print(x[i][j],end=' ')
    print()
print("yes" if r==1 else "no",end='')    
  
        

