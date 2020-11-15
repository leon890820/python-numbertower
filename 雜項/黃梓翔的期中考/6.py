w="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m,n=eval(input())
a,b,c=4*(n-1)-1,n,3*n-3
for i in range(n):
    print(w[i%m],end='')
print()
for i in range(n-2):
    print(w[a%m]+" "*(n-2)+w[b%m])
    a-=1
    b+=1
for i in range(n):
    print(w[c%m],end='')
    c-=1

