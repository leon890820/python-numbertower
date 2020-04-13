n=int(input())
m=[[None]*(i+1) for i in range(n)]
for i in range(n):
    for j in range(i+1):
         if j==0 or i==j:
             m[i][j]=1
         else:
             m[i][j]=m[i-1][j-1]+m[i-1][j]
for i in range(n):
    print(" "*2*(n-i),end='')
    for j in range(i+1):
        print("{:>4}".format(str(m[i][j])),end=' ')
    print()
































'''
n=int(input())
num=[[None]*(i+1) for i in range(n)]
s=0
t=0
for i in range(int((n*(n+1))/2)):
 num[s][t]=i+1
 if s==n-1:
   t+=1
   s=t
 else:
   s+=1
for i in range(n):
 for j in range(i+1):
   print(“{:>2}”.format(num[i][j]),end=' ')
 print()
''' 
 

