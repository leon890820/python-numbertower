w="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input())
ci=0
cj=0
for i in range(n):
    for j in range(n+2):
        if j-i==1:
            print("\\",end='')
        elif j-i<1:
            print(w[ci%26],end='')
            ci+=1
        else:
            print(w[cj%26],end='')
            cj+=1
    print()
