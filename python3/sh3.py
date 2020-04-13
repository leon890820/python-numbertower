n=int(input())
num=[[None]*n for i in range(n)]
s,t=0,0
ds,dt=[0,1,0,-1],[1,0,-1,0]
dir=0
m=n//2+(1 if n%2 else 0)
#填數字
for i in range(n*n):
    num[s][t]=i+1
    s+=ds[dir]
    t+=dt[dir]
    if s+t==n-1 or (s>=m and s==t) or (s<m and s==t+1):
        dir+=1
        if dir==4:dir=0
#印出來
for i in range(n):
    for j in range(n):
        print("{:>3}".format(num[i][j]),end=' ')
    print()
