n=int(input())
num=0
for i in range(3):
    for k in range(n):
        for j in range(3):
            for l in range(n):
                if i==0 :
                    num=(1 if j==0 else 2)
                elif i==2:
                    num=(4 if j==0 else 5)
                else:
                    num==3
                if i==j or i+j==2:
                    print(num,end='')
                else:
                    print(' ',end='')
        print()
