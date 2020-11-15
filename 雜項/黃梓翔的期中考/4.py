n=int(input())

for i in range(-n+1,n):
    for j in range(-n+1,n):
        if(abs(i+j)>=n or abs(i-j)>=n):
            print(" ",end='')
        else:
            print(n-abs(i)-abs(j),end='')
    print()