N,L=int(input()),int(input())
N1=[[None]*2 for i in range(N)]
for i in range(N):
    for j in range(2):
        N1[i][j]=int(input())
N1.sort()
print(N1)
N2=[None for i in range(N*2+1)]
N2[-1]=L+10
k=0
for i in range(N):
    N2[k]=N1[i][0]-N1[i][1]
    k+=1
    N2[k]=N1[i][0]+N1[i][1]
    k+=1
print(N2)
for i in range(N):
    if N2[2*i]<0:N2[2*i]=0
    if N2[2*i+1]>L:N2[2*i+1]=L
    if N2[2*i+1]>N2[2*i+2]:N2[2*i+1]=N2[2*i+2]
sum=0
for i in range(N):
    sum+=(N2[2*i+1]-N2[2*i])
print(sum/L*100,'%')
    
