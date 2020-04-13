N,L=int(input()),int(input())
N1=[[None]*2 for i in range(N)]
for i in range(N):
    for j in range(2):
        N1[i][j]=int(input())
N1.sort()
N2=[None for i in range(N*2)]
k=0
for i in range(N):
    N2[k]=N1[i][0]-N1[i][1]
    k+=1
    N2[k]=N1[i][0]+N1[i][1]
    k+=1
sum=0
print(N2)
N3=[None for i in range(N)]
N3[-1]=L-N2[-1]
for i in range(N-1):
    N3[i]=N2[2*(i+1)]-N2[2*(i+1)-1]
N3.sort()
print(N3[-1] if N3[-1]>=0 else 0)
    
    
